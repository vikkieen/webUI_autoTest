from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
class DiscuzVote(BasePage):
    #发表投票帖子所需参数
    bankuai=(By.CSS_SELECTOR,".bm_c tr:nth-child(2) h2 a")
    fatie=(By.CSS_SELECTOR, "#newspecial img")
    button=(By.CSS_SELECTOR,"#ct #editorbox .tb li:nth-child(2) a")#发起投票按钮
    title=(By.CSS_SELECTOR,"#postbox .pbt .z .px")#投票标题
    select1=(By.CSS_SELECTOR,".mbm p:nth-child(1) input")#投票选项一
    select2=(By.CSS_SELECTOR,".mbm p:nth-child(2) input")#投票选项二
    select3= (By.CSS_SELECTOR,".mbm p:nth-child(3) input")#投票选项三
    new=(By.CSS_SELECTOR,".mbm p:nth-child(6) a")#增加一项
    tou=(By.CSS_SELECTOR,".pnpost .pnc span")#发起投票


    #进行投票所需参数
    toup=(By.CSS_SELECTOR,".pcht .pslt .pr")#进行投票对于某个选项
    tijiao=(By.CSS_SELECTOR,"#pollsubmit span")#提交投票


    #取出投票各个选项的名称以及投票比例

    receive1=(By.CSS_SELECTOR,".pcht tr:nth-child(1) .pvt label")#选项名称一
    receive2 = (By.CSS_SELECTOR, ".pcht tr:nth-child(3) .pvt label")  # 选项名称二
    receive3 = (By.CSS_SELECTOR, ".pcht tr:nth-child(5) .pvt label")  # 选项名称三
    scale1=(By.CSS_SELECTOR,".pcht tr:nth-child(2) td:nth-child(2)")#投票比例一
    scale2 = (By.CSS_SELECTOR, ".pcht tr:nth-child(4) td:nth-child(2)")  # 投票比例一
    scale3 = (By.CSS_SELECTOR, ".pcht tr:nth-child(6) td:nth-child(2)")  # 投票比例一

    #取出投票的主题名称
    get_title=(By.CSS_SELECTOR,"#thread_subject")

    #发表投票
    def fabiao(self,title,select1,select2,select3):
        self.click(*self.bankuai)
        self.click(*self.fatie)
        self.click(*self.button)
        self.sendkeys(title,*self.title)
        self.sendkeys(select1,*self.select1)
        self.sendkeys(select2,*self.select2)
        self.sendkeys(select3,*self.select3)
        self.click(*self.tou)

    #进行投票
    def toupiao(self):
        self.click(*self.toup)
        self.click(*self.tijiao)

    #取出投票各个选项的名称以及投票比例
    def getName(self):
        t1=self.get_element_text(*self.receive1)
        t2=self.get_element_text(*self.receive2)
        t3=self.get_element_text(*self.receive3)
        s1=self.get_element_text(*self.scale1)
        s2=self.get_element_text(*self.scale2)
        s3=self.get_element_text(*self.scale3)
        print("选项名称：%s     投票比例：%s"%(t1,s1))
        print("选项名称：%s     投票比例：%s"%(t2, s2))
        print("选项名称：%s     投票比例：%s"%(t3, s3))

    #取出投票的主题名称
    def getTitle(self):
        title=self.get_element_text(*self.get_title)
        print("投票的主题名称为:%s"%title)