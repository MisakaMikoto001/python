# ============================================================
# 异步爬虫 —— 使用 aiohttp + asyncio 并发抓取多个网站标题
# 核心概念：协程(coroutine)、事件循环(event loop)、异步I/O
# ============================================================

# asyncio: Python 内置的异步 I/O 框架，提供事件循环、协程、Task 等支持
import asyncio
# re: 正则表达式模块，用于从 HTML 中提取 <title> 标签内容
import re
# aiohttp: 第三方异步 HTTP 客户端库，支持 async/await 语法
#   ClientSession: 会话对象，复用连接池，类似 requests.Session()
#   TCPConnector: 底层 TCP 连接器，可配置 SSL 验证、连接数等
from aiohttp import ClientSession, TCPConnector
# time: 用于计时，对比同步与异步的性能差异
import time

# ------------------------------------------------------------
# 预编译正则表达式（提升性能，避免每次请求都重新编译）
# <title.*?>  : 匹配 <title> 或 <title lang="zh"> 等带属性的标签
# (.*?)       : 非贪婪匹配标题文本（捕获组，group(1) 可获取）
# re.DOTALL   : 让 . 也能匹配换行符，防止标题跨行时匹配失败
# ------------------------------------------------------------
TITLE_PATTERN = re.compile(r'<title.*?>(.*?)</title>', re.DOTALL)

# ------------------------------------------------------------
# 请求头：模拟浏览器访问，避免被网站反爬虫拦截
# User-Agent       : 告诉服务器"我是 Chrome 浏览器"
# Accept           : 告诉服务器我能接收哪些类型的内容
# Accept-Language  : 告诉服务器我偏好中文页面
# ------------------------------------------------------------
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}


# ============================================================
# async def: 声明一个异步函数（协程函数）
# 调用该函数不会立即执行函数体，而是返回一个 coroutine 对象
# 只有被 await 或被 asyncio.run() 调度时才会真正执行
# ============================================================
async def fetch_page_title(url):
    # 记录单个请求的开始时间，用于计算每个 URL 的耗时
    start = time.time()
    try:
        # ------------------------------------------------------------
        # async with: 异步上下文管理器
        #   - 进入时自动调用 __aenter__()，退出时自动调用 __aexit__()
        #   - 确保会话和响应对象在使用完毕后正确关闭，释放资源
        #
        # ClientSession(connector=TCPConnector(ssl=False)):
        #   - headers=HEADERS: 每次请求都带上预设的请求头
        #   - connector=TCPConnector(ssl=False): 跳过 SSL 证书验证
        #     （新版 aiohttp 不再支持 session.get(url, ssl=False) 写法）
        # ------------------------------------------------------------
        async with ClientSession(headers=HEADERS, connector=TCPConnector(ssl=False)) as session:
            # session.get(url): 发起异步 GET 请求，返回响应对象
            async with session.get(url) as resp:
                # 检查 HTTP 状态码是否为 200（成功）
                if resp.status == 200:
                    # await resp.text(): 异步读取响应体文本
                    #   await 会让出 CPU 控制权，事件循环可调度其他协程执行
                    #   这是异步爬虫性能高的关键：I/O 等待时不阻塞线程
                    html_code = await resp.text()
                    # 用正则表达式在 HTML 中搜索 <title>...</title>
                    matcher = TITLE_PATTERN.search(html_code)
                    # 如果匹配成功，提取标题文本并去除首尾空白
                    if matcher:
                        # matcher.group(1): 获取第一个捕获组的内容（即标题文本）
                        title = matcher.group(1).strip()
                        print(f'{url} -> {title}')
                    else:
                        # 匹配失败（如页面无 title 标签、或格式不标准）
                        print(f'{url} -> 未找到标题')
    except Exception as e:
        # 捕获所有异常（网络错误、超时、解析失败等）
        # 单个请求失败不影响其他任务，保证异步并发的鲁棒性
        print(f'{url} -> 请求失败: {e}')
    finally:
        # finally 块无论成功或失败都会执行，保证耗时统计一定输出
        # time.time() - start: 计算该请求从发起到完成的实际耗时
        print(f'{url} -> 请求耗时: {time.time() - start :.2f}')


# ============================================================
# async def main(): 主协程函数，负责调度所有子任务
# ============================================================
async def main():
    # 记录整体开始时间，用于计算所有任务的总耗时
    start = time.time()
    # 待抓取的 URL 列表（可根据需要增删）
    url = [
        'https://www.douban.com/',       # 豆瓣首页
        'https://movie.douban.com/',     # 豆瓣电影
        'https://www.python.org/',       # Python 官网
        'https://www.cnblogs.com/',      # 博客园
        'https://www.jd.com/',           # 京东
        'https://www.taobao.com/',       # 淘宝
        'https://www.baidu.com/',        # 百度
        'https://www.sogou.com/',        # 搜狗
        'https://www.sohu.com'           # 搜狐
    ]

    # ------------------------------------------------------------
    # asyncio.create_task(): 将协程包装为 Task 对象并注册到事件循环
    #   - Python 3.13 中 asyncio.wait() 必须传入 Task，不能直接传协程
    #   - Task 创建后即开始调度执行（无需手动 start）
    # ------------------------------------------------------------
    tasks = [asyncio.create_task(fetch_page_title(url)) for url in url]
    # ------------------------------------------------------------
    # await asyncio.wait(tasks): 等待所有 Task 完成
    #   - 这里是真正的"并发点"：所有协程在同一事件循环中交替执行
    #   - 当某个协程 await 时（如等待网络响应），CPU 自动切换到其他协程
    #   - 总耗时 ≈ 最慢那个请求的耗时，而非所有请求耗时之和
    #   - 也可用 asyncio.gather(*tasks) 实现同样效果
    # ------------------------------------------------------------
    await asyncio.wait(tasks)
    # 所有任务完成后，输出总耗时
    print(f'所有任务耗时: {time.time() - start :.4f}')


# ============================================================
# 程序入口
# ============================================================
if __name__ == '__main__':
    # ------------------------------------------------------------
    # asyncio.run(main()): Python 3.7+ 推荐的启动方式
    #   1. 自动创建事件循环 (Event Loop)
    #   2. 将 main() 协程包装为 Task 并调度执行
    #   3. 运行完毕后自动关闭事件循环，清理资源
    #   替代了旧版的 loop = get_event_loop() + run_until_complete() + close()
    # ------------------------------------------------------------
    asyncio.run(main())