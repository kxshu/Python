# coding:utf-8
import sys
import io

#reload(sys)
#sys.setdefaultencoding('utf8')
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

a="我我我"
print(a)
