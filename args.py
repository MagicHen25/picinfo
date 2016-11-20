proxy_file = 'pl.txt'
PicPat = 'F:/picinfo/'
HTMLFile = 'F:/picinfo.html'
FixStr = '''
<div class="post_box">
<div class="c-top">
<div class="tit">
<h2 class="h1"><a href="COMIC-HREF" >COMIC-NAME</a></h2>
</div>
</div>
<div class="c-con">
<a class="disp_a"> <img src="COMIC-IMG"/></a>
</div>
</div>
'''

url = 'http://www.177picxx.info'

headers_picinfo = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Cookie':'isid_incap_967260=ctS/LWhHQsmuCGand1/MM6ZmE1gAAAAAQUIPAAAAAAB2MC63apy6lY1PMu2NaJI5; visid_incap_967274=+M6MaPHlSIyfFBV6YunzeqdmE1gAAAAAQUIPAAAAAAA2hnBR9QsvTdLFwjzApWtY; __cfduid=ddf4cb15f0ceacc77761139958510f1771478322421; _ga=GA1.2.1257268074.1477666464; _gat=1'
}
