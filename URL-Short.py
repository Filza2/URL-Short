from requests import post,get
import os,re
def header():
    os.system("cls" if os.name=='nt' else "clear");print("""
██╗   ██╗██████╗ ██╗      ███████╗██╗  ██╗ ██████╗ ██████╗ ████████╗
██║   ██║██╔══██╗██║      ██╔════╝██║  ██║██╔═══██╗██╔══██╗╚══██╔══╝
██║   ██║██████╔╝██║█████╗███████╗███████║██║   ██║██████╔╝   ██║   
██║   ██║██╔══██╗██║╚════╝╚════██║██╔══██║██║   ██║██╔══██╗   ██║   
╚██████╔╝██║  ██║███████╗ ███████║██║  ██║╚██████╔╝██║  ██║   ██║   
 ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
 
                      By @TweakPY - @vv1ck
""")
    
def short_url_1():
    header()
    url=input("- Enter The URL : ");header()
    r=post('https://hideuri.com/api/v1/shorten',headers={'Host': 'hideuri.com','Cookie': '_cfvdata=as874as89sa9as84s89f4asfa8f','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': 'https://hideuri.com/','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest','Content-Length': '47','Origin': 'https://hideuri.com','Te': 'trailers'},data=f'url={url}')
    if 'result_url' in r.json():print(f'- Done successfully, Your URL : {r.json()["result_url"]}')
    elif 'error' in r.json():exit('- Error ! ')
    else:exit('- Error ! ')
    
def short_url_2():
    header()
    url=input("- Enter The URL : ");header()
    r=get(f'https://v.ht/api.php?url={url}',headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'})
    if 'https://v.ht/' in r.text:print(f'- Done successfully, Your URL : {r.text}')
    else:exit('- Error ! ')
    
def short_url_3():
    header()
    url=input("- Enter The URL : ");header()
    r=post(f'http://chilp.it/api.php?url={url}',headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'})
    if 'http://chilp.it/' in r.text:print(f'- Done successfully, Your URL : {r.text}')
    else:exit('- Error ! ')
    
def short_url_4():
    header()
    url=input("- Enter The URL : ");header()
    r=post('https://is.gd/create.php',headers={'Host': 'is.gd','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded'},data=f'url={url}&shorturl=&opt=0')
    try:short_url=re.findall('''<a id="qrlabel" onclick="load_qrcode('(.*?)'); return false" href="https://chart.apis.google.com/chart?cht=qr&amp;chs=100x100&amp;choe=UTF-8&amp;chld=H|0&amp;chl=(.*?)">Give me this URL as a QR code</a>''',r.text)[0][2]
    except:exit('- Error ! ')
    print(f'- Done successfully, Your URL : {short_url}')

def short_url_5():
    header()
    url=input("- Enter The URL : ");header()
    r=post('https://da.gd/',headers={'Host': 'da.gd','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded'},data=f'url={url}&shorturl=')
    try:short_url=re.findall('<a href="(.*?)" style="color: #888; font-family: monospace;">(.*?)</a>',r.text)[0][1]
    except:exit('- Error ! ')
    print(f'- Done successfully, Your URL : {short_url}')


def Core():
    _short=int(input('''
1 - Short URL via [ Hideuri.com ]
2 - Short URL via [ v.ht ]
3 - Short URL via [ chilp.it ]
4 - Short URL via [ is.gd ]
5 - Short URL via [ da.gd ]

Enter ID : '''))
    if _short==1:short_url_1()
    elif _short==2:short_url_2()
    elif _short==3:short_url_3()
    elif _short==4:short_url_4()
    elif _short==5:short_url_5()
    else:exit("- It seems that this is not Right ? ")

header();Core()
print('\n')