#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
import urllib    # Python中的cURL库  
import urllib.request 
from urllib import request,parse
import time    # 时间函数库，包含休眠函数sleep()  
# url = 'https://www.zcool.com.cn/work/ZMzI3MTE1ODA=.html'    # 希望刷阅读量的文章的URL  
url = 'https://www.zcool.com.cn/work/ZMzMyMTEwNDg=.html'    # 希望刷阅读量的文章的URL  
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'    # 伪装成Chrome浏览器  
refererData = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=site%3A%20www.zcool.com.cn%20%E7%99%BC%E5%AD%A9%E5%85%92&oq=site%253A%2520www.zcool.com.cn%2520ABV%252040%2526lt%253B&rsv_pq=eeed783900003358&rsv_t=1e66qYbPlSgk1jsY3RbI5uphI7miR%2FRbSF7yI4hZAWGwS5wCaS%2BEWirpxGM&rqlang=cn&rsv_enter=0&inputT=4904&rsv_sug3=36&rsv_n=2&bs=site%3A%20www.zcool.com.cn%20ABV%2040%25'    #伪装成是从baidu.com搜索到的文章  
dict ={
   'name':'Germey'
}
data=bytes(parse.urlencode(dict),encoding='utf-8')    # 将GET方法中待发送的数据设置为空  
headers = {'User-Agent' : user_agent, 'Referer' : refererData}    # 构造GET方法中的Header  
count = 0    # 初始化计数器  
req = urllib.request.Request(url, data, headers,method='GET')    # 组装GET方法的请求  
while 1:    # 一旦开刷就停不下来  
    rec = urllib.request.urlopen(req)    # 发送GET请求，获取博客文章页面资源  
    page = rec.read()    # 读取页面内容到内存中的变量，这句代码可以不要  
    count += 1    # 计数器加1  
    print (count)    # 打印当前循环次数  
    if count % 6:    # 每6次访问为1个循环，其中5次访问等待时间为31秒，另1次为61秒  
        time.sleep(31)    # 为每次页面访问设置等待时间是必须的，过于频繁的访问会让服务器发现刷阅读量的猥琐行为并停止累计阅读次数  
    else:  
        time.sleep(61)  
print (page)    # 打印页面信息，这句代码永远不会执行  
