import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver=webdriver.Chrome("./chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.lagou.com/")
driver.find_element_by_id("cboxClose").click()
time.sleep(3)
driver.find_element_by_id("search_input").send_keys("java",Keys.ENTER)
page_list=driver.current_window_handle
driver.switch_to.window(page_list)
while True:
    job_list=driver.find_elements_by_css_selector(".s_position_list  .item_con_list li")
    num=1
    print(len(job_list))
    for job in job_list:
        print(num)
        job.find_element_by_css_selector("h3").click()
        driver.switch_to.window(driver.window_handles[1])
        company=driver.find_element_by_css_selector(".job-name .company").text
        gangwei=driver.find_element_by_css_selector(".position-head .name").text
        money=driver.find_element_by_css_selector(".job_request span:nth-child(1)").text
        local=driver.find_element_by_css_selector(".job_request span:nth-child(2)").text
        exper=driver.find_element_by_css_selector(".job_request span:nth-child(3)").text
        study=driver.find_element_by_css_selector(".job_request span:nth-child(4)").text
        print("公司：%s 岗位：%s  薪资：%s  地点：%s  经验：%s  学历：%s"%(company,gangwei,money,local,exper,study))
        driver.close()
        driver.switch_to.window(page_list)
        num+=1
    next_page = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.item_con_pager .pager_container > *:last-child')))
    # next_page = driver.find_element_by_css_selector('.item_con_pager .pager_container span:last-child')
    next_page_class = next_page.get_attribute('class')
    if 'pager_next_disabled' in next_page_class:
        break
    else:
        next_page.click()
        time.sleep(3)
time.sleep(10)
driver.quit()