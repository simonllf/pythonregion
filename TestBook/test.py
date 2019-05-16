from selenium import webdriver
from time import sleep


# browser = webdriver.PhantomJS(r'C:/phantomjs211/bin/phantomjs.exe')
# 设置火狐Headless模式为true
IP = "127.0.0.0"
PORT = 9999
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
# 设置代理服务器
# options.set_preference('network.proxy.type', 1)
# options.set_preference('network.proxy.http', IP)#IP为你的代理服务器地址:如‘127.0.0.0’，字符串类型
# options.set_preference('network.proxy.http_port', PORT)  #PORT为代理服务器端口号:如，9999，整数类型

browser = webdriver.Firefox(options=options)

browser.get("http://www.baidu.com")

# 2.通过浏览器向服务器发送URL请求
browser.get("https://www.baidu.com/")

browser.find_element_by_id("kw").send_keys(u"hello world!")
browser.save_screenshot("baidu1.png")

# print(browser.page_source)

print(browser.title)
browser.quit()

# sleep(3)

# .刷新浏览器
# browser.refresh()

# 4.设置浏览器的大小
# browser.set_window_size(1400, 800)

# 5.设置链接内容
# element = browser.find_element_by_link_text("新闻")
# element.click()

element = browser.find_element_by_link_text("习近平的“下团组”时间")
element.click()

