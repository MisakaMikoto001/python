# 识别网站技术栈
import ssl
import builtwith


ssl._create_default_https_context = ssl._create_unverified_context
print(f'技术栈：{builtwith.parse('https://www.jianshu.com')}')

import whois
print(f'域名信息：{whois.whois('www.jianshu.com')}')
