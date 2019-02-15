import urllib.request
import urllib.error
#创建get方法
def get(url):
 code=urllib.request.urlopen(url).code
 return code

def mail(txt):
 _user = "你的账号"
 _pwd = "你的密码"
 _to = "收件账号"
 msg = MIMEText(txt, 'plain', 'utf-8')
 #标题
 msg["Subject"] = "代理失效！"
 msg["From"] = _user
 msg["To"] = _to
 
 try:
   #这里我用的qq邮箱
   s = smtplib.SMTP_SSL("smtp.qq.com", 465)
   s.login(_user, _pwd)
   s.sendmail(_user, _to, msg.as_string())
   s.quit()
   print("Success!")
 
 except smtplib.SMTPException as e:
   print("Falied,%s" % e)


if __name__ == '__main__':
 url = "http://shua.jb51.net"
 proxies = ["124.88.67.22:80","124.88.67.82:80","124.88.67.81:80","124.88.67.31:80","124.88.67.19:80","58.23.16.240:80"]
 user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36"
 headers = {'User-Agent':user_agent}
 req = urllib.request.Request(url, headers=headers)
 i = 1
 while 1:
   try:
     code = get(url,proxies)
     print('第'+str(i)+'次代理访问:'+str(code))
     i = i+1
   except urllib.error.HTTPError as e:
     print(e.code)
      #添加mail方法
     mail(e.code)
   except urllib.error.URLError as err:
     print(err.reason)
      #添加mail方法
     mail(err.reason)

