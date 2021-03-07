import urllib
import http.cookiejar
import json
import os
import requests

def main():
    ## 登录
    account = {
        'email': os.environ['feiji_email'],
        "passwd": os.environ['feiji_pass']
    }
    url = "http://sgicc.airport-gov-cn.com:59999/auth/login"
    postdata ={
        'email': account['email'],
        'passwd': account['passwd'],
        'code':""
    }
    session = requests.session()
    session.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'})

    req = session.post(url,data=postdata)
    #自动记住cookie
    response=req.text.encode()
    logincheck=json.loads(response)
    if logincheck['ret']!=1 :
        print('登录失败')
    print('账号'+account['email']+'登录成功')
    ## 签到
    url = "http://sgicc.airport-gov-cn.com:59999/user/checkin"
    postdata = {}

    session.headers.update({"Content-Type":"application/json"})

    req = session.post(url,data=postdata)
    response=req.text
    try:
        ret = json.loads(response)
    except ValueError:
        print('签到失败')
        print('账号'+account['email']+'签到“很有精神”失败 msg:'+ret['msg'])
    if ret['ret']!=1:
        print('签到失败')
        print('账号'+account['email']+'签到“很有精神”失败 msg:'+ret['msg'])
    #登出
    url = "http://sgicc.airport-gov-cn.com:59999/user/logout"
    req = session.get(url)
    print("结束“很有精神”签到")