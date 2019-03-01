from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
dir=os.path.dirname(__file__)
chrome_driver_path=dir+"/chromedriver.exe"
driver=webdriver.Chrome(chrome_driver_path)
try:
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.lagou.com/")
    print("网页已经打开",driver.title)
    print(driver.window_handles)
    driver.find_element_by_id("cboxClose").click()
    time.sleep(3)
    print(driver.window_handles)
    # driver.switch_to.window(driver.window_handles[0])
    driver.find_element_by_id("search_input").send_keys("java"+Keys.RETURN)
    print("java已搜索")
    print(driver.window_handles)
    # driver.find_element_by_css_selector(".search_input ui-autocomplete-input").send_keys("java",Keys.RETURN)
    job_list = driver.current_window_handle
    driver.switch_to.window(job_list)
    num=1
    while True:
        print(num)
        jobs=driver.find_elements_by_css_selector(".item_con_list li")
        print(len(jobs))
        for i in jobs:
            i.find_element_by_css_selector(".p_top a span").click()
            print(len(driver.window_handles))
            driver.switch_to.window(driver.window_handles[1])
            pos=driver.find_element_by_css_selector(".name").text
            c_name=driver.find_element_by_css_selector(".company").text
            mony=driver.find_element_by_css_selector(".salary").text
            time=driver.find_element_by_css_selector(".job_request p span:nth-child(3)").text
            print("职位名称：%s 公司名称：%s 薪资水平：%s 工作年限要求：%s "%(pos,c_name,mony,time))
            driver.close()
            driver.switch_to.window(job_list)
        next_page=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.item_con_pager .pager_container > *:last-child ')))
        # next_page=driver.find_element_by_css_selector(".item_con_pager .pager_container span:last-child")
        next_page_class=next_page.get_attribute('class')
        if 'pager_next_disabled' in next_page_class:
            print("页面全部完成")
            break
        else:
            print("当前第%d页，有%d个职位信息继续下一页" % (num, len(jobs)))
            next_page.click()
            time.sleep(3)
            num+=1
except AttributeError as a:
    print("'str' object has no attribute 'sleep")
finally:
    time.sleep(10)
    print("爬虫结束")
    driver.quit()

