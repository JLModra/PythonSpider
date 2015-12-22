# -*- coding:UTF-8 -*-
'''
created on 2015-12-19
妯℃嫙鐧诲綍鍗楅偖閭
@author: wuzhidong
'''
import urllib2
import urllib


#妯℃嫙鐧诲綍鍗楅偖閭
def loginNUPTMailBox(uid, password):
    #鐧诲綍椤电殑URL
    url = 'http://mail.njupt.edu.cn/coremail/index.jsp'
    
    #娴忚鍣ㄦ爣璇嗙
    agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    
    #鏋勯�犵殑HTTP璇锋眰鐨勫ご閮�
    headers = {}
    headers['User-Agent'] = agent
    
    #鏋勯�犵殑璇锋眰鐨勫唴瀹�
    values = {}
    values['action:login'] = ''
    values['uid'] = uid
    values['password'] = password
    
    #璇锋眰鍐呭缂栫爜
    data = urllib.urlencode(values)
    
    #鏋勯�犺姹�
    request = urllib2.Request(url, data, headers)
    
    #灏嗚姹備綔涓哄弬鏁颁紶鍏rlopen鏂规硶锛屽緱鍒拌繑鍥炵殑鍐呭
    response = urllib2.urlopen(request)
    
    #鎵撳紑鏂囦欢锛堝鏋滄病鏈夊氨鏂板缓锛夛紝璁剧疆鍙啓
    file = open('NUPTMailBox.html', 'r+w')
    
    #鎶妑esponse鐨勫唴瀹瑰啓杩涙枃浠�
    file.write(response.read())
    
    #鍏抽棴鏂囦欢
    file.close()
    
    #鎵撳紑鏂囦欢锛岃缃彧璇�
    file = open('NUPTMailBox.html', 'r')
    
    #鎶婃枃浠堕噷鐨勫唴瀹规墦鍗板嚭鏉�
    print file.read()
    
    #鍏抽棴鏂囦欢
    file.close()
