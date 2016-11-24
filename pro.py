import requests
from bs4 import BeautifulSoup
import time
proxy_list = []
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Cookie':'_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWQ1YWRlNmRmMDVhNjgxYWNlZjVjMDgzMmI0ZTUxM2M2BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMWxPWkZ0Z1owbzB5Z2YvNXlZOUhTVG9xM1lyVDdDWGQzL0V5eko0WnJ5cFU9BjsARg%3D%3D--629e923ac9184c72ef9690b1dcf0433953d8e830; CNZZDATA1256960793=66246918-1478613112-%7C1479537726'
}

for i in range(1,50):
    time.sleep(10)
    urls = 'http://www.xicidaili.com/nn/{}'.format(str(i))
    content = requests.get(urls,headers = headers)
    soup = BeautifulSoup(content.text,'lxml')
    trs = soup.find_all('tr')
    for tr in trs[1:]:
        tds = tr.findAll('td')
        ip = tds[1].text.strip()
        port = tds[2].text.strip()
        protocal = tds[5].text.strip()
        if protocal == 'HTTP' or protocal == 'HTTPS':
            # print('{}://{}:{}'.format(protocal,ip,port))
            f = open('pl.txt','a')
            f.write('{}://{}:{}'.format(protocal,ip,port))
            f.write('\n')
            f.close()
            proxy_list.append('{}://{}:{}'.format(protocal,ip,port))
for i in proxy_list:
    print(i)
