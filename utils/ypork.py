import urllib
import http.cookiejar
import json
import os

def main():
    ## 登录
   account={
        'email':os.environ['FEIJI_EMAIL'],
        "passwd":os.environ['FEIJI_PASS']
    }

    url = "https://forever.ypork.com/auth/login"
    postdata =urllib.parse.urlencode({
        'email': account['email'],
        'passwd': account['passwd']
    }).encode('utf-8')
    header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
    }
    req = urllib.request.Request(url,postdata,header)
    #自动记住cookie
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    r = opener.open(req)
    response=r.read().decode('utf-8')
    logincheck=json.loads(response)
    if logincheck['ret']!=1 :
        print('登录失败')
    print('账号'+account['email']+'登录成功')
    ## 签到
    url = "https://forever.ypork.com/user/checkin"
    postdata =urllib.parse.urlencode({}).encode('utf-8')
    header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
        "Content-Type":"application/json",

    }
    req = urllib.request.Request(url,postdata,header)
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    r = opener.open(req)
    response=r.read().decode('utf-8')
    try:
        ret = json.loads(response)
    except ValueError:
        print('签到失败')
        print('账号'+account['email']+'签到cdpc失败 msg:'+ret['msg'])
    if ret['ret']!=1:
        print('签到失败')
        print('账号'+account['email']+'签到cdpc失败 msg:'+ret['msg'])
    print(ret)
    #登出
    url = "https://forever.ypork.com/user/logout"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
    }
    req = urllib.request.Request(url, None, header)
    print("结束ypork签到")

