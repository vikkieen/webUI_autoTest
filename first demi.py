from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
dir=os.path.dirname(__file__)
chrome_driver_path=dir+"\chromedriver.exe"
dirver=webdriver.Chrome(chrome_driver_path)
# dirver.get("https://www.yahoo.com")
# assert "yahoo" in dirver.title
#
# elem=dirver.find_element_by_name("p")
# elem.send_keys("seleniumhq"+Keys.RETURN)
# dirver.quit()

#2
# try:
#     dirver.implicitly_wait(5)
#     dirver.get("https://www.baidu.com")
#     elem=dirver.find_element_by_id("kw")
#     elem.send_keys("java")
#     elem.submit()
#     dirver.switch_to.window(dirver.current_window_handle)
#     print("百度首页已打开",dirver.title)
#     nums=dirver.find_element_by_class_name("nums")
#     print(nums.text)
#     wait_seconds=10
#     dirver.execute_script("window.alert(\"{}, {}秒后关闭\")".format(nums.text.replace("\n", "$"), wait_seconds))
#     time.sleep(wait_seconds)
# except Exception as a:
#     print("wrong")
# finally:
#     dirver.close()

# dirver.get("https://www.baidu.com")
# n=dirver.find_elements_by_tag_name("a")
# for i in n:
#     print(i.text)
# dirver.quit()
try:
    dirver.get("https://www.baidu.com")
    dirver.maximize_window()
    dirver.implicitly_wait(2)
    dirver.find_element_by_link_text("关于百度").click()
    print("页面已打开:"+dirver.title)
    dirver.find_element_by_link_text("联系我们").click()
    print("页面已打开:"+dirver.title)
    for handle in dirver.window_handles:
        dirver.switch_to.window(handle)
    print("页面已打开:" + dirver.title)

    email_list=dirver.find_elements_by_class_name("mail-content-text")
    print(len(email_list))
    for j in email_list:
        str=j.text
        if "@" in str:
            print(str)
finally:
    dirver.quit()

# email=dirver.find_elements_by_partial_link_text("@")
# print(len(email))
# for j in email:
#     print(j.text)
# dirver.quit()