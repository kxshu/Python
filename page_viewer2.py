# encoding=utf8
import requests
import re
import time
from bs4 import BeautifulSoup

firstUrl = 'http://blog.csdn.net/snake_son/article/details/52282490'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    ,
    'Cookie': '_message_m=23yegwleahbzf4fy5a05grgr; uuid=e7680a5d-2824-45d9-ac7a-06289c3d3cd8; avh=53945000%2c52282490; dc_tos=os5x0v; dc_session_id=1498493448566'
}

def getHtml(url):
    text = requests.get(url,headers).text
    # print('text  ',text)
    return text

# txt = getHtml(firstUrl)

def parseHtml(text):
    reg_next = r'blog_articles_xiayipian.*?location.href=(.*?);">'
    regNext = re.compile(reg_next)
    nextUrl = re.findall(regNext,text)
    print('当前新页面: ',nextUrl)
    str1 = ''.join(nextUrl).rstrip('\'')
    # htmurl = 'http://blog.csdn.net'+''.join(str1).rstrip('\'')

    # 将字符串前n个字符替换为指定的字符
    # strnset(sStr1,ch,n)
    sStr1 = ''.join(str1)
    ch = ''
    n = 1
    sStr1 = n * ch + sStr1[1:]
    htmurl = 'http://blog.csdn.net'+sStr1
    print('htmurl  '+htmurl)
    return htmurl


for i in range(1,56):
    text = getHtml(firstUrl)
    newUrl = parseHtml(text)
    firstUrl = newUrl
    print('first2 ',firstUrl,'newUrl ',newUrl)