#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import timeit
import urllib  # Python中的cURL库
import urllib.request
from multiprocessing import Pool  # 多进程
from urllib import parse, request
import _thread
import random
from lxml import etree  # 解析

i = 0
mylock = _thread.allocate_lock()


def GetUserAgent():
    user_agents = ["Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)", "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
                   "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)", "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)", "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)", "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1"]
    user_agent = random.choice(user_agents)
    return user_agent


user_agent = GetUserAgent()

url = 'https://www.zcool.com.cn/work/ZMzI3MTE1ODA=.html'    # 希望刷阅读量的文章的URL
# url = 'https://www.zcool.com.cn/work/ZMzI3NzgxMjg=.html'    # 希望刷阅读量的文章的URL
# url = 'https://www.jianshu.com/p/842843fd51d4'    # 希望刷阅读量的文章的URL
refererData = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=site%3A%20www.zcool.com.cn%20%E7%99%BC%E5%AD%A9%E5%85%92&oq=site%253A%2520www.zcool.com.cn%2520ABV%252040%2526lt%253B&rsv_pq=eeed783900003358&rsv_t=1e66qYbPlSgk1jsY3RbI5uphI7miR%2FRbSF7yI4hZAWGwS5wCaS%2BEWirpxGM&rqlang=cn&rsv_enter=0&inputT=4904&rsv_sug3=36&rsv_n=2&bs=site%3A%20www.zcool.com.cn%20ABV%2040%25'  # 伪装成是从baidu.com搜索到的文章
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf-8')    # 将GET方法中待发送的数据设置为空
headers = {
    'User-Agent': user_agent,
    'Referer': refererData
}    # 构造GET方法中的Header

# count = 0    # 初始化计数器
req = urllib.request.Request(url, data, headers, method='GET')    # 组装GET方法的请求


# def test(no, r):
#     global i, j
#     for j in range(no, r):
#         rec = urllib.request.urlopen(req)    # 发送GET请求，获取博客文章页面资源
#         page = rec.read()    # 读取页面内容到内存中的变量，这句代码可以不要
#         mylock.acquire()
#         i += 1
#         mylock.release()
#         print(i)
#         print(page)    # 打印页面信息，这句代码永远不会执行

#         if i % 6:    # 每6次访问为1个循环，其中5次访问等待时间为31秒，另1次为61秒
#             # 为每次页面访问设置等待时间是必须的，过于频繁的访问会让服务器发现刷阅读量的猥琐行为并停止累计阅读次数
#             time.sleep(31)
#         else:
#             time.sleep(61)

#     _thread.exit_thread()


def _run(threadName, count):
    while 1:    # 一旦开刷就停不下来
        rec = urllib.request.urlopen(req)    # 发送GET请求，获取博客文章页面资源
        page = rec.read()    # 读取页面内容到内存中的变量，这句代码可以不要
        count += 1    # 计数器加1

        # print(count)    # 打印当前循环次数
        print("%s: %s" % (threadName, count))

        if count % 6:    # 每6次访问为1个循环，其中5次访问等待时间为31秒，另1次为61秒
            # 为每次页面访问设置等待时间是必须的，过于频繁的访问会让服务器发现刷阅读量的猥琐行为并停止累计阅读次数
            time.sleep(31)
        else:
            time.sleep(61)
    _thread.exit_thread()


def fast():
    try:
        _thread.start_new_thread(_run("T1", 0))
        _thread.start_new_thread(_run("T2", 1))
    except:
        print("Error: unable to start thread")

fast()
