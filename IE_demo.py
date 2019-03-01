# import os
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# dir=os.path.dirname(__file__)
# ie_driver_path=dir+"\IEDriverServer.exe"
# driver=webdriver.Ie(ie_driver_path)
# driver.get("http://www.yahoo.com")
# assert "百度" in driver.title
#
# elem=driver.find_element_by_name("p")
# elem.send_keys("seleniumhq"+Keys.ENTER)
from selenium import webdriver
import re

driver = webdriver.Chrome("./chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("http://home.baidu.com/contact.html")
# 得到页面源代码
doc = driver.page_source

emails = re.findall(r'[\w]+@[\w\.-]+', doc)  # 利用正则，找出 xxx@xxx.xxx 的字段，保存到emails列表
# 循环打印匹配的邮箱
for email in emails:
    print(email)
driver.quit()
