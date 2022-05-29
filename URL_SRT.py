from requests import post
print("""
██╗   ██╗██████╗ ██╗      ███████╗██████╗ ████████╗    
██║   ██║██╔══██╗██║      ██╔════╝██╔══██╗╚══██╔══╝    
██║   ██║██████╔╝██║█████╗███████╗██████╔╝   ██║       
██║   ██║██╔══██╗██║╚════╝╚════██║██╔══██╗   ██║       
╚██████╔╝██║  ██║███████╗ ███████║██║  ██║   ██║       
 ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝       
            By @TweakPY  -  @vv1ck                                                  
""")
c=int(input("1-short Link with bitly\n2-short Link with hideuri\n:"))
if c==1:
	to_short=input("[?] The url : ")	
	res=post('https://api-ssl.bitly.com/v3/shorten',data={'access_token':'8a7a79e75bf4d990986f7a63e7c6cc71e5612f7c','uri':to_short})
	if 'url' in res.text:print('[+] Your short url : '+res.json()['data']['url'])
	else:print("[!] Error shorting the url")
elif c==2:
    url_short=input("[?] The url : ")	
    res=post('https://hideuri.com/api/v1/shorten',headers={'Host': 'hideuri.com','Cookie': '_cfvdata=as874as89sa9as84s89f4asfa8f','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': 'https://hideuri.com/','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest','Content-Length': '47','Origin': 'https://hideuri.com','Te': 'trailers'},data=f'url={url_short}')
    if 'result_url' in res.json():print('[+] Your short url : '+res.json()['result_url'])
    elif 'error' in res.json():print('[!] The Error is => : '+res.json()['error'])
    else:print('[!] Error ..')
else:exit("Alright ..")

