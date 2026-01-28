"""
序列化与反序列化
    字典与json互转

pip

"""

import json
"""
    json模块 四个比较重要函数
        dump    将python对象格式序列化到文件中
        dumps   将python对象处理成json格式字符串
        load    将文件中的json数据反序列化成对象
        loads   将字符串的内容反序列化成对象
"""

def dict_json():
    """字典与json互转"""

    dict = {
        'name': 'lisi',
        'age': 19,
        'sex': 'male',
        'hobby': ['football', 'basketball']
    }

    print(f'dict:{dict}\n')
    json_str = json.dumps(dict)# dumps 处理成字符串
    print(f'json_str:{json_str}\n')

    with open('test.json', 'w', encoding='utf-8') as f:
        json.dump(dict, f)

def json_dict():
    """json与字典互转"""

    with open('test.json', 'r', encoding='utf-8') as f:
        json_str = json.load(f)# load 处理成字典
        print(f'json_str to  dict:{json_str}\n')
        print()

import requests
def requests_api():
    """requests 模块"""

    url = 'http://web.juhe.cn/finance/gold/shgold'
    params = {
        'key': '7db36de6b02a39f2f9e62f2b2afcb952',
        'v': ''
    }

    response = requests.get(url, params)

    if response.status_code == 200:
        json_str = response.json()
        print(f"{json_str['result']}")
    else:
        print('请求错误')

def main():
    # dict_json()
    # json_dict()
    requests_api()

if __name__ == '__main__':
    main()