import requests
import re


def practice():
    resp = requests.get('https://www.bootcss.com')
    resp.encoding = 'utf-8'

    pattern = re.compile(r'<a\s+[^>]*?href\s*=\s*["\']?([^"\'>\s]+)["\']?[^>]*>(.*?)</a>', re.S)
    """
    <a\s+[^>]*?href\s*=\s*["\']?([^"\'>\s]+)["\']?[^>]*>(.*?)</a>
    匹配所有a标签，提取href属性和标签内容
    1. 匹配所有a标签
    2. 提取href属性和标签内容
    3. 提取标签内容时，忽略空格和换行符
    """

    if resp.status_code == 200:
        all_matches = pattern.findall(resp.text)
        for href, text in all_matches:
            print(f'href: {href}, text: {text.strip()}')

import random
import time

def douban_top250():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
        'Host': 'movie.douban.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://movie.douban.com/top250',
        'Cookie': 'll="118282"; bid=eQrlQnx7WLs; _pk_id.100001.4cf6=4b3e18b446de4c7f.1760598077.; __yadk_uid=WJcS3wRjX3Po3xTZkyRuRBF214g5gcZs; _vwo_uuid_v2=D9679AD98559D350C34B794C4E0A70DFE|d343cef6f72a5bd1b65e3aa294f01f25; viewed="10594787"; ap_v=0,6.0; __utmc=30149280; __utmz=30149280.1784269120.7.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmc=223695111; __utmz=223695111.1784269120.6.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1784272388%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=1; __utma=30149280.2117789649.1760598077.1784269120.1784272388.8; __utmb=30149280.0.10.1784272388; __utma=223695111.1205926998.1760598077.1784269120.1784272389.7; __utmb=223695111.0.10.1784272389'
    }



    for page in range(1, 11):
        resp = requests.get(f'https://www.douban.com/top250?start={(page - 1) * 25}&filter=',
                            headers=headers)
        resp.encoding = 'utf-8'
        if resp.status_code != 200:
            print(f'第{page+1}页请求失败: {resp.status_code}')
            continue

        pattern1 = re.compile(r'<span class="title">(?!&nbsp;/&nbsp;)(.*?)</span>')
        titles = pattern1.findall(resp.text)
        pattern2 = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
        ratings = pattern2.findall(resp.text)

        print(f'第{page}页数据: {len(titles)}条')
        for title, rating in zip(titles, ratings):
            print(f'title: {title}, rating: {rating}')
        time.sleep(random.random()*2+1)


if __name__ == '__main__':
    # practice()
    douban_top250()


    pass