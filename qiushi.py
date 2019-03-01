from selenium import webdriver
import re
driver = webdriver.Chrome("./chromedriver.exe")
try:
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.qiushibaike.com/text/")
    total=0
    n=1
    while True:
        print("第%d页**************************************************************************"%n)
        title=driver.find_elements_by_css_selector("h2")
        content=driver.find_elements_by_css_selector(".content")
        num=driver.find_elements_by_css_selector(".stats .stats-vote")
        total=total+n*len(title)
        for i in range(0,len(title)):
            print("标题：",title[i].text)
            print("内容：", content[i].text)
            print("好笑数:",num[i].text)
            print("-"*50)
        print("第%d页有%d个笑话"%(n,len(title)))
        # doc = driver.page_source
        # result=re.match("下一页",doc)
        # bool=driver.find_element_by_css_selector(".pagination .current").text=="13"
        # print(bool)

        if driver.find_element_by_css_selector(".pagination .current").text!="13":
            driver.find_element_by_css_selector(".pagination .next").click()
            n+=1
        else:break
    print("一共有%d页有%d个笑话"%(n,total))
finally:
    driver.quit()

