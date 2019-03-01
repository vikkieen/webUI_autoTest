from selenium import webdriver
driver=webdriver.Chrome("chromedriver.exe")
import time
    #邮箱登录
# driver.get("https://mail.163.com/")
# driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
# email=driver.find_element_by_name("email")
# email.send_keys("")
# psw=driver.find_element_by_name("password")
# psw.send_keys("")
# driver.find_element_by_id("dologin").click()

#alert弹出框
driver.get("http://baidu.com")
driver.execute_script("window.alert('测试弹出框accept')")
time.sleep(2)
driver.switch_to.alert.accept()
driver.execute_script("window.alert('测试弹出框miss')")
time.sleep(2)
driver.switch_to.alert.dismiss()
