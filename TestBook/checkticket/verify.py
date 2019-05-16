import requests
from PIL import Image
from selenium.webdriver import ActionChains
import time
from io import BytesIO
# 识别验证模块

class Code():
    def __init__(self, browser):
        self.browser = browser
        self.verify_url = 'http://littlebigluo.qicp.net:47720/'     # 验证码识别网址，返回识别结果

        # 确定验证码的位置
    def get_position(self):
        time.sleep(3)
        element = self.browser.find_element_by_class_name('touclick-img-par')
        time.sleep(2)
        location = element.location
        size = element.size
        position= (location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height'])
        return position

        # 截取整个网页页面
    def get_screenshot(self):
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

        # 从截取的网页，裁剪出验证码图片，并保存到本地
    def get_touclick_img(self, name = 'captcha.png'):
        position = self.get_position()
        print('验证码的位置:', position)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop(position)
        captcha.save('captcha.png')

        #验证码解析
    def parse_img(self):
        # files = {'file': open('captcha.png', 'rb')}             # 打开保存到本地的验证码图片
        files = {'pic_xxfile': open('captcha.png', 'rb')}
        response = requests.post(self.verify_url, files=files)
        num = response.text.split('<B>')[1].split('<')[0]
        print('验证码识别成功！图片位置：%s' % num)
        try:
            if int(num):
                return [int(num)]
        except ValueError:
            num = list(map(int,num.split()))
            return num

        # 识别结果num都以列表形式返回，方便后续验证码的点击

        # 实现验证码自动点击
    def move(self):
        num = self.parse_img()
        try:
            element = self.browser.find_element_by_class_name('touclick-img-par')
            for i in num:
                if i <= 4:
                    ActionChains(self.browser).move_to_element_with_offset(element,40+72*(i-1),73).click().perform()
                else :
                    i -= 4
                    ActionChains(self.browser).move_to_element_with_offset(element,40+72*(i-1),145).click().perform()
        except:
            print('元素不可选！')

    def main(self):
        self.get_touclick_img()
        self.move()
