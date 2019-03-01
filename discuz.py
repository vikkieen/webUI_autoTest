from selenium import webdriver
import os
import time
from selenium.webdriver.common.action_chains import ActionChains
dir=os.path.dirname(__file__)
chrome_driver_path=dir+"/chromedriver.exe"
driver=webdriver.Chrome(chrome_driver_path)

driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://127.0.0.1/forum.php")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("root")
driver.find_element_by_css_selector(".fastlg_l button").click()
time.sleep(15)
driver.find_element_by_css_selector(".bm_c h2 a").click()
time.sleep(15)
driver.find_element_by_css_selector("#newspecial img").click()
py=driver.current_window_handle
driver.find_element_by_css_selector("#postbox .z #subject").send_keys("标题")
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
driver.find_element_by_tag_name("body").send_keys("内容是")
driver.switch_to.window(py)
driver.find_element_by_css_selector("#postsubmit span").click()
driver.find_element_by_css_selector(".fastre").click()
driver.switch_to
# menu=driver.find_element_by_css_selector("#newspecial")
# hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")
# ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()