reated on 2015-12-19
模拟登录南邮邮箱
@author: wuzhidong
'''
import urllib2
import urllib


#模拟登录南邮邮箱
def loginNUPTMailBox(uid, password):
    #登录页的URL
    url = 'http://mail.njupt.edu.cn/coremail/index.jsp'
    
    #浏览器标识符
    agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    
    #构造的HTTP请求的头部
    headers = {}
    headers['User-Agent'] = agent
    
    #构造的请求的内容
    values = {}
    values['action:login'] = ''
    values['uid'] = uid
    values['password'] = password
    
    #请求内容编码
    data = urllib.urlencode(values)
    
    #构造请求
    request = urllib2.Request(url, data, headers)
    
    #将请求作为参数传入urlopen方法，得到返回的内容
    response = urllib2.urlopen(request)
    
    #打开文件（如果没有就新建），设置只写
    file = open('NUPTMailBox.html', 'r+w')
    
    #把response的内容写进文件
    file.write(response.read())
    
    #关闭文件
    file.close()
    
    #打开文件，设置只读
    file = open('NUPTMailBox.html', 'r')
    
    #把文件里的内容打印出来
    print file.read()
    
    #关闭文件
    file.close()
