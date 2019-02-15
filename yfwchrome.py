#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import requests
from pyquery import PyQuery as pq
from lxml import etree
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

import urllib
import time
import datetime
import re
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from StringIO import StringIO
import MySQLdb
from selenium import webdriver
from fake_useragent import UserAgent
# from smtp465 import mail
reload(sys)
sys.setdefaultencoding('utf-8')

#http://www.cnblogs.com/luxiaojun/p/6144748.html
#https://segmentfault.com/q/1010000011139042

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4',
    'Connection': 'keep-alive'
}

ua = UserAgent()
ua.random
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.add_argument('window-size=1920x3000') #指定浏览器分辨率
chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
chrome_options.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败


cap = dict(DesiredCapabilities.CHROME)  #设置userAgent
cap["Chrome.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ")
#driver = webdriver.Chrome(desired_capabilities=cap)
driver=webdriver.Chrome(chrome_options=chrome_options,desired_capabilities=cap)
driver.set_page_load_timeout(10)
driver.set_window_size('480','800')

#url='https://reg.yaofangwang.com/login.aspx'
url='https://reg.yaofangwang.com/login.html'
driver.get(url)
data = driver.title
print data
driver.find_element_by_id('txt_AccountName').send_keys('shangjie')
driver.find_element_by_id('txt_Password').send_keys('gwj@123456')
driver.find_element_by_id('btn_Submit').click()
# driver.find_element_by_id('ctl00_ContentPlaceHolder1_t_login').click()
# driver.find_element_by_id('ctl00_ContentPlaceHolder1_t_login').submit()
# driver.execute_script("javascript:__doPostBack('btn2 b2','')")
#driver.find_element_by_id('ctl00_ContentPlaceHolder1_t_login').click()
time.sleep(5) #甘倍轻 588513 # 乐盼 615972  瑞莱生4袋 582108
#resurl='https://www.yaofangwang.com/medicine-588513-p'+str(pagenum)+'.html?sort=price&sorttype=asc'

def GetGoodList(goodsn):
    #pass
    for pagenum in xrange(1,3):
        resurl='https://www.yaofangwang.com/medicine-'+str(goodsn)+'-p'+str(pagenum)+'.html?sort=price&sorttype=asc'
	print resurl
        driver.get(resurl) #?sort=price&sorttype=asc
        #driver.save_screenshot('login.png')
        driver.page_source
        tree=etree.HTML(driver.page_source)
        ShopNum=tree.xpath('//*[@id="priceA"]/ul/li[1]/a/text()')[0]
        pattern = re.compile(r'\d+') 
        res=pattern.findall(ShopNum)
        print res[0]

        username=tree.xpath('////*[@id="TopNav"]/li[7]/a[1]/text()')
        print username
        for i in xrange(1,int(8)+1):
            if tree.xpath('//*[@id="slist"]/ul/li['+str(i)+']/div[4]/p/a/text()'):
                GoodUrl=tree.xpath('//*[@id="slist"]/ul/li['+str(i)+']/div[2]/h3/a/@href')[0]
                ress=pattern.findall(GoodUrl)
                #print ress[0]
                GoodId=ress[0]
                GoodName=tree.xpath('//*[@id="slist"]/ul/li['+str(i)+']/div[2]/h3/a/text()')[0]
                GoodPrice=tree.xpath('//*[@id="slist"]/ul/li['+str(i)+']/div[3]/p[1]/text()')[0]
                ShopName=tree.xpath('//*[@id="slist"]/ul/li['+str(i)+']/div[4]/p/a/text()')[0]
                GoodStock=tree.xpath('//*[@id="slist"]/ul/li['+str(i)+']/div[2]/p[3]/label/text()')[0]
                print GoodId,GoodUrl,GoodName,GoodPrice[1:],ShopName,"库存：",GoodStock
                #print type(GoodName),type(GoodPrice),type(ShopName)
                mail_content="商品名:"+str(GoodName)+'\n'+"药房网价格："+str(GoodPrice[1:]  )+'\n'+"店铺名："+str(ShopName  )+'\n'+"库存："+str(GoodStock)+'\n'+"网址："+str(GoodUrl)
                mail_subject=str(GoodName)+str(GoodPrice[1:]  )+str(ShopName  )
                # print mail_subject
                # print "++++"
                # print mail_content
                #print float(GoodPrice[1:])
                # if goodsn==588513 and float(GoodPrice[1:])<float(90.0):
                #     mail(mail_content,mail_subject)
                #     print "+++++send mail"
                # if goodsn==615972 and float(GoodPrice[1:])<float(67.0):
                #     mail(mail_content,mail_subject)
                #     print "+++++send mail"

                # if goodsn==629338 and float(GoodPrice[1:])<float(180.0):
                #     mail(mail_content,mail_subject)
                #     print "+++++send mail"
                # if goodsn==626847 and float(GoodPrice[1:])<float(99.0):
                #     mail(mail_content,mail_subject)
                #     print "+++++send mail"
                # if goodsn==626771 and float(GoodPrice[1:])<float(131.0):
                #     mail(mail_content,mail_subject)
                #     print "+++++send mail"
                # if goodsn==647417 and float(GoodPrice[1:])<float(90.0):
                #     mail(mail_content,mail_subject)
                #     print "+++++send mail"
                # if goodsn==605763 and float(GoodPrice[1:])<float(120.0):
                #     mail(mail_content,mail_subject)
                #     print "+++++send mail"            
                # else:
                #     print "+++++++++++++++++++++++++++++++++++++++++++++++="


if 2330000 > int(time.strftime("%H%M%S")) > 83000:
    GetGoodList(588513) # 甘倍轻 588513 
    time.sleep(60) 
    GetGoodList(615972) # 乐盼 615972
    time.sleep(60) 
    GetGoodList(629338) # 甘倍轻14片629338
    time.sleep(60) 
    GetGoodList(626847) # 乐盼  21 626847
    time.sleep(60)
    GetGoodList(626771) # 乐盼  28 626771
    time.sleep(60)
    GetGoodList(605763) # 敏枢  3  605763
    time.sleep(60)
    GetGoodList(647417) # 聚普瑞锌 4 647417
    time.sleep(60)
    GetGoodList(646804) # 聚普瑞锌 6 646804
    time.sleep(60)


driver.close()
driver.quit()
    # obj.get('http://www.baidu.com')
    # obj.find_element_by_id('kw')                    #通过ID定位
    # obj.find_element_by_class_name('s_ipt')         #通过class属性定位
    # obj.find_element_by_name('wd')                  #通过标签name属性定位
    # obj.find_element_by_tag_name('input')           #通过标签属性定位
    # obj.find_element_by_css_selector('#kw')         #通过css方式定位
    # obj.find_element_by_xpath("//input[@id='kw']")  #通过xpath方式定位
    # obj.find_element_by_link_text("贴吧")           #通过xpath方式定位


