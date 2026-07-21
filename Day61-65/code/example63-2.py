"""
并发在爬虫中的应用 —— 爬虫属于典型的 I/O 密集型任务
分别使用 单线程、多线程、异步协程 三种方式下载图片，对比性能差异
"""
import os
import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import asyncio
import aiohttp
from aiohttp import ClientSession, TCPConnector

# ============================================================
# 使用 Lorem Picsum 免费图库 API（无需认证，永不失效）
# 获取图片列表：https://picsum.photos/v2/list?page=1&limit=30
# 返回 JSON 数组，每个元素包含 download_url 字段
# ============================================================
API_URL = 'https://picsum.photos/v2/list'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
}

# 下载保存目录（三种方式各自独立目录，方便对比）
BASE_DIR = r'C:\Users\Administrator\Pictures\images'
PAGE_COUNT = 3        # 抓取页数（每页 30 张图）
PER_PAGE = 10         # 每页实际下载数量（控制总量，避免耗时过长）


# ============================================================
# 通用工具函数：下载单张图片
# ============================================================
def download_image(url, save_dir):
    """下载单张图片到指定目录"""
    filename = url.split('/')[-1].split('?')[0]  # 去掉 URL 参数
    if not filename.endswith('.jpg'):
        filename += '.jpg'
    filepath = os.path.join(save_dir, filename)
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        if resp.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(resp.content)
    except Exception as e:
        print(f'下载失败 {url}: {e}')


def ensure_dir(path):
    """确保目录存在"""
    if not os.path.exists(path):
        os.makedirs(path)


def fetch_image_urls(page, count):
    """从 API 获取一页图片 URL 列表"""
    resp = requests.get(
        f'{API_URL}?page={page}&limit={count}',
        headers=HEADERS
    )
    if resp.status_code == 200:
        return [item['download_url'] for item in resp.json()]
    return []


# ============================================================
# 方式一：单线程 —— 逐个下载，完全串行
# ============================================================
def single_threaded():
    save_dir = os.path.join(BASE_DIR, 'single')
    ensure_dir(save_dir)
    start = time.time()

    for page in range(1, PAGE_COUNT + 1):
        urls = fetch_image_urls(page, PER_PAGE)
        for url in urls:
            download_image(url, save_dir)

    elapsed = time.time() - start
    print(f'[单线程] 耗时: {elapsed:.2f} 秒')


# ============================================================
# 方式二：多线程 —— 线程池并发下载
# ============================================================
def multi_threaded():
    save_dir = os.path.join(BASE_DIR, 'multi')
    ensure_dir(save_dir)
    start = time.time()

    # 第一步：单线程获取所有 URL（API 请求量小，不必并发）
    all_urls = []
    for page in range(1, PAGE_COUNT + 1):
        all_urls.extend(fetch_image_urls(page, PER_PAGE))

    # 第二步：线程池并发下载图片（I/O 密集型，多线程收益大）
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {
            executor.submit(download_image, url, save_dir): url
            for url in all_urls
        }
        for future in as_completed(futures):
            future.result()  # 等待完成，有异常会在此抛出

    elapsed = time.time() - start
    print(f'[多线程] 耗时: {elapsed:.2f} 秒')


# ============================================================
# 方式三：异步协程 —— aiohttp 并发下载
# ============================================================
async def async_download_image(session, url, save_dir):
    """异步下载单张图片"""
    filename = url.split('/')[-1].split('?')[0]
    if not filename.endswith('.jpg'):
        filename += '.jpg'
    filepath = os.path.join(save_dir, filename)
    try:
        async with session.get(url) as resp:
            if resp.status == 200:
                content = await resp.read()
                with open(filepath, 'wb') as f:
                    f.write(content)
    except Exception as e:
        print(f'下载失败 {url}: {e}')


async def async_main():
    save_dir = os.path.join(BASE_DIR, 'async')
    ensure_dir(save_dir)
    start = time.time()

    # 第一步：同步获取所有 URL（aiohttp 也可以，但量小没必要）
    all_urls = []
    for page in range(1, PAGE_COUNT + 1):
        all_urls.extend(fetch_image_urls(page, PER_PAGE))

    # 第二步：aiohttp 并发下载所有图片
    async with ClientSession(
        headers=HEADERS,
        connector=TCPConnector(ssl=False, limit=10)  # 限制并发连接数
    ) as session:
        tasks = [
            asyncio.create_task(async_download_image(session, url, save_dir))
            for url in all_urls
        ]
        await asyncio.wait(tasks)

    elapsed = time.time() - start
    print(f'[异步IO] 耗时: {elapsed:.2f} 秒')


# ============================================================
# 主入口：依次运行三种方式，对比性能
# ============================================================
if __name__ == '__main__':
    print('=' * 50)
    print('图片爬虫性能对比：单线程 vs 多线程 vs 异步IO')
    print(f'下载页数: {PAGE_COUNT}, 每页: {PER_PAGE} 张, 总计: {PAGE_COUNT * PER_PAGE} 张')
    print('=' * 50)

    single_threaded()
    multi_threaded()
    asyncio.run(async_main())

    print('=' * 50)
    print('对比完成！三种方式的图片分别保存在:')
    print(f'  单线程: {BASE_DIR}\\single')
    print(f'  多线程: {BASE_DIR}\\multi')
    print(f'  异步IO: {BASE_DIR}\\async')