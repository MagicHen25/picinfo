import args
import func

from bs4 import BeautifulSoup
import requests
import time
import pymongo
import random


proxy_ips = func.get_proxy_ip(args.proxy_file)   #从代理文件获取代理IP

picinfo = requests.get(args.url,headers = args.headers_picinfo,proxies = random.choice(proxy_ips))
time.sleep(3)#防止过快抓取
soup = BeautifulSoup(picinfo.text,'lxml')
TotPags = int(soup.find("a",class_="last").get("href").split('/')[-1])

PagLiks = ['http://www.177picxx.info/page/{}'.format(str(i)) for i in range(29,TotPags + 1)]#所有目录页链接

print('Get all links fom www.177picxxinfo.com done!')

for PagLik in PagLiks:
    time.sleep(3)
    FilCons = func.get_cont_from(PagLik,proxy_ips)
    for FilCon in FilCons:
        FilCon['img'] = func.down_pic_from(FilCon['img'],proxy_ips)
        func.write_html_from(FilCon)
