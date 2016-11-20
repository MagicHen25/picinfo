import requests
import args
import random
from bs4 import BeautifulSoup
import shutil
import datetime




def get_proxy_ip(proxy_file):
    proxy_for_spider = []
    f = open(proxy_file,'r')
    lines = f.readlines()
    for line in lines:
        proxy_for_spider.append(str(line)[0:-1])
    return proxy_for_spider

def get_cont_from(url,proxy_ips):
    print('Downloading: ' + url)
    # page_content = requests.get(url,headers = args.headers_picinfo,proxies=random.choice(proxy_ips))
    page_content = requests.get(url,headers = args.headers_picinfo)
    soup = BeautifulSoup(page_content.text,'lxml')
    titles = soup.select('div.tit > h2 > a')
    imgs = soup.select('div > a > img')
    conts = []
    for title,img in zip(titles,imgs):
        data = {
            'title':title.text,
            'href':title.get('href'),
            'img':img.get('src')
        }
        conts.append(data)
    return conts

def down_pic_from(url,proxy_ips):
    print(url)
    # r = requests.get(url,stream = True,proxies=random.choice(proxy_ips))
    r = requests.get(url,stream = True)
    pic_name = args.PicPat + datetime.datetime.now().strftime("%m%d%H%M%S-") + url.split('/')[-1]
    if r.status_code == 200:
        with open(pic_name ,'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw,f)
    return pic_name

def write_html_from(data):
    tmp = args.FixStr.replace('COMIC-NAME',data['title'])
    tmp = tmp.replace('COMIC-HREF',data['href'])
    HTML_input = tmp.replace('COMIC-IMG',data['img'][3:]).encode()
    f = open(args.HTMLFile,'ab')
    f.write(HTML_input)
    f.write('\n'.encode())
    f.close()
