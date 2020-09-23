import urllib.request
import urllib.parse
import json
import time

# 在这里填你的csrt效验码
csrf='4f7a433483e3f8f4da89d179dbcd459b'
# 在这里填上你的b站cookie
cookie="CURRENT_FNVAL=16; _uuid=94E0367D-94F9-F508-2325-2813805E83A676827infoc; buvid3=DDF16585-2C75-4C65-912D-A4F050A0D69453929infoc; LIVE_BUVID=AUTO3715823914788382; rpdid=|(kmR)R||)~Y0J'ul)kJmuR~m; im_notify_type_5794786=0; sid=aams03rg; DedeUserID=5794786; DedeUserID__ckMd5=f80d63961608c14b; SESSDATA=82588e26%2C1609827046%2Cc30ae*71; bili_jct=4f7a433483e3f8f4da89d179dbcd459b; CURRENT_QUALITY=74; bp_video_offset_5794786=415965499558772306; bp_t_offset_5794786=416195031200730287; PVID=1; _dfcaptcha=8d2a82570a4ce33db497a5c0c9a80c51; bfe_id=fdfaf33a01b88dd4692ca80f00c2de7f"

def SeadAdd(Avcode,cookie,csrf):
    url = 'https://api.bilibili.com/x/web-interface/coin/add'
    formdata={'aid':Avcode,'multiply':'1','select_like':'1','cross_domain':'true','csrf':csrf}
    header={
    "Host": "api.bilibili.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Connection": "keep-alive",
    "Origin": "https://www.bilibili.com",
    "Referer": "https://www.bilibili.com/video/"+ str(Avcode),
    "Cookie": cookie,
    "Pragma": "no-cache",
    "Cache-Control":"no-cache"
    }
    request=urllib.request.Request(url=url,headers=header)
    formdata=urllib.parse.urlencode(formdata).encode()
    response=urllib.request.urlopen(request,formdata)

    massage=json.loads(response.read().decode())

    return massage['code']

def Get_todayExp():
    api='https://api.bilibili.com/x/web-interface/coin/today/exp'
    header={
     "Host": "api.bilibili.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Cookie":cookie,
    "Upgrade-Insecure-Requests": "1",
    "Cache-Control":"max-age=0"
    }
    response = urllib.request.Request(url=api,headers=header)
    response = urllib.request.urlopen(response)
    response = json.loads(response.read().decode('utf-8'))
    return response

def Get_bangumi():
    bangumiApi="https://api.bilibili.com/x/web-interface/newlist?rid=33"
    response=urllib.request.urlopen(bangumiApi)
    response=json.loads(response.read().decode('utf-8'))
    data=response['data']
    avlist=[]
    for i in data['archives']:
        avlist.append(i['aid'])
    return avlist

def main():
    # f=open("log.txt",'w+')
    # localtime = time.asctime(time.localtime(time.time()))
    time_=(50-Get_todayExp()['data'])/10
    Avlist=Get_bangumi()
    i=0
    while time_!=0:
        if SeadAdd(Avlist[i], cookie, csrf) != 0:
            print('已经投过币了！')
            # f.write(str(localtime)+' 已经投过币了！\n')
            i+=1
        else:
            print(str(Avlist[i])+'投币成功')
            # f.write(str(localtime) + ' 投币成功'+str(Avlist[i])+"\n")
            i+=1
            time_-=1
    print("你今天的投币经验机会已经使用完毕")
    # f.write(str(localtime) + ":你今天的投币经验机会已经使用完毕\n")
