from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# webdriver-manager 自动下载并管理 ChromeDriver，无需手动配置
# 首次运行时会自动下载匹配当前 Chrome 版本的驱动
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get('https://www.baidu.com')
print(browser.title)
browser.quit()