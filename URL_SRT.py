import requests
print("""
██╗   ██╗██████╗ ██╗      ███████╗██████╗ ████████╗    
██║   ██║██╔══██╗██║      ██╔════╝██╔══██╗╚══██╔══╝    
██║   ██║██████╔╝██║█████╗███████╗██████╔╝   ██║       
██║   ██║██╔══██╗██║╚════╝╚════██║██╔══██╗   ██║       
╚██████╔╝██║  ██║███████╗ ███████║██║  ██║   ██║       
 ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝       
<\> @TweakPY                                                       
""")
print("---------------------")
more_one=int(input("1) One Link\n2) More Than One\n3) Short Link\n---------------------\n"))
print("~~~~~~~~~~~~~~~~~~~~~")
if more_one==1:
	to_short=input("[?] Type the Url: ")
	url=f"https://chkweb.tk/bit.ly/main.php?url={to_short}"
	req=requests.post(url)
	if "true" in req.text:
		print(f"[+] Done shorting the url.")
		print("===================================")
		print(f"[+] The url befor:\n"+req.json()["data"]["long_url"])
		print("===================================")
		print(f"[+] The url after shorting:\n"+req.json()["data"]["short"])
		print("===================================")
	elif "invalid" in req.text:print("[!] Please Type a valid link..")
	else:print(f"[!] >> Error in Shorting" )
elif more_one==2:
	to_short=input( "[?]-1 Type the Url: ")
	to_short2=input("[?]-2 Type the Url: ")
	to_short3=input("[?]-3 Type the Url: ")
	req=requests.post(f"https://chkweb.tk/bit.ly/main.php?url={to_short}")
	req2=requests.post(f"https://chkweb.tk/bit.ly/main.php?url={to_short2}")
	req3=requests.post(f"https://chkweb.tk/bit.ly/main.php?url={to_short3}")
	if "true" in req.text:
		print("===================================")
		print(f"[+]-1 The url befor:\n"+req.json()["data"]["long_url"])
		print(f"[+]-1 The url after shorting:\n"+req.json()["data"]["short"])
		print("===================================")
	elif "invalid" in req.text:print("[!]-1 Please Type a valid link..")
	else:print(f"[!]-1 >> Error in Shorting" )
	if "true" in req2.text:
		print(f"[+]-2 The url befor:\n"+req2.json()["data"]["long_url"])
		print(f"[+]-2 The url after shorting:\n"+req2.json()["data"]["short"])
		print("===================================")
	elif "invalid" in req2.text:print("[!]-2 Please Type a valid link..")
	else:print(f"[!]-2 >> Error in Shorting" )
	if "true" in req3.text:
		print(f"[+]-3 The url befor:\n"+req3.json()["data"]["long_url"])
		print(f"[+]-3 The url after shorting:\n"+req3.json()["data"]["short"])
		print("===================================")
	elif "invalid" in req3.text:print("[!]-3 Please Type a valid link..")
	else:print(f"[!]-3 >> Error in Shorting" )
elif more_one==4:
	API_KEY='8a7a79e75bf4d990986f7a63e7c6cc71e5612f7c'
	to_short=input("[?] Type The Url : ")	
	data={'access_token':API_KEY, 'uri':to_short}
	url='https://api-ssl.bitly.com/v3/shorten'
	response=requests.post(url,data=data)
	if 'url' in response.text:print(response.json()['data']['url'])
	else:print("[!?] Error with shorting the url")
else:exit("Alright ..")

