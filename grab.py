import requests
import sys
from urllib.parse import urlparse
import time
import re
from fake_useragent import UserAgent
import os
from colorama import Fore, init
from rich import print as cetak
from pystyle import Colors,Colorate,Write
from rich.panel import Panel as nel
import requests,urllib3
from multiprocessing.dummy import Pool, Lock, Semaphore
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from multiprocessing import Pool
init(autoreset=True)
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from module.run import server
def clear():
    if sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('freebsd'):
        os.system('clear')
    else:
        os.system('cls')
headersx = {'User-Agent': UserAgent().random}

red = Fore.RED 
green = Fore.GREEN 
yellow = Fore.YELLOW
white = Fore.WHITE
blue = Fore.BLUE
def gui():
    Write.Print("─══════════════════════════ቐቐ══════════════════════════─\n", Colors.blue_to_purple, interval=0.01)
    text = f""" 
 /$$   /$$ /$$                      /$$$$$$ 
| $$$ | $$|__/                     /$$__  $$
| $$$$| $$ /$$  /$$$$$$$  /$$$$$$ | $$  \__/
| $$ $$ $$| $$ /$$_____/ /$$__  $$| $$$$    
| $$  $$$$| $$|  $$$$$$ | $$  \ $$| $$_/    
| $$\  $$$| $$ \____  $$| $$  | $$| $$      
| $$ \  $$| $$ /$$$$$$$/|  $$$$$$/| $$      
|__/  \__/|__/|_______/  \______/ |__/     
                                     
    GitHub: Nisofganz2
    """

    for N, line in enumerate(text.split("\n")):
        print(Colorate.Horizontal(Colors.red_to_green, line, 1))
        time.sleep(0.05)
    Write.Print("\n─══════════════════════════ቐቐ══════════════════════════─\n\n", Colors.blue_to_purple, interval=0.01)
    
def inputPage():
    try:
        srv = ''
        print('*Server\n1.Arcive\n2.Special\n3.Onhold')
        ab = int(input("Choose Server : "))
        if ab == 1:
            srv = 'archive'
        elif ab == 2:
            srv = 'special'
        elif ab == 3:
            srv = 'onhold'
        else:print('Option Not Available.')
        page = int(input("Input Page : "))
        toPage = int(input("Input To Page : "))
        
        return page, toPage, srv
    except:pass
    
def defacerNet(page,toPage, srv):
    try:
        for page in range(page, toPage + 1):
            try:
                ua = {'User-Agent': UserAgent().random}
                url = f'https://defacer.net/{srv}/{page}' 
                req2 = requests.get(url, headers=ua, timeout=30).text
                domains = re.findall(r"<a href='(.*?)'>", req2)
                domains = [domain for domain in domains if not 'defacer.net' in domain]
                if domains != 0:
                    for domainst in domains:
                        domains = ''.join(domainst)
                        domains = domains.split("/")[2]
                        open('allMirrorGrab.txt', 'a+').write(domains + '\n')
                    print(f'{blue}Defacer-Net {white}| {yellow}Page : {green}{page} {white}| {yellow}Grabbed : {green}{len(domains)} {white}Domains')
                else:
                    print("limit page!")
                    break
            except:pass
    except:pass
    
def defacermirror(page,toPage, srv):
    try:
        for page in range(page, toPage + 1):
            try:
                ua = {'User-Agent': UserAgent().random}
                url = f"https://defacermirror.com/{srv}.php?page={page}"
                req2 = requests.get(url, headers=ua, timeout=15, verify=False).text
                cob = re.findall(r"<a href=\"(.*?)\" target=\"_blank\"", req2)
                if len(cob) != 0:
                    for ing in cob:
                        cba = ing.split('/')[2]
                        open('allMirrorGrab.txt', 'a+').write(cba + "\n")
                    print(f'{blue}Defacer-Mirror {white}| {yellow}Page : {green}{page} {white}| {yellow}Grabbed : {green}{len(cob)} {white}Domains')
                else:
                    break
            except:pass
    except:pass
    
def haxorid(page,toPage, srv):
    try:
        for page in range(page, toPage + 1):
            try:
                ua = {'User-Agent': UserAgent().random}
                url = f"http://haxor.id/{srv}?page={page}"
                req2 = requests.get(url, headers=ua, timeout=30, verify=False).content.decode("utf-8")
                cob = re.findall("href=\"(.*?)\" target=\"_blank\">", req2)
                if len(cob) != 0:
                    for ing in cob:
                        cv = ''.join(ing)
                        cba = cv.split("/")[2]
                        open('allMirrorGrab.txt', 'a+').write(cba + "\n")
                    print(f'{blue}Haxor-ID {white}| {yellow}Page : {green}{page} {white}| {yellow}Grabbed : {green}{len(cob)} {white}Domains')
                else:
                    break
            except:pass
    except:pass

def mirrorh(page,toPage, srv):
    try:
        for page in range(page, toPage + 1):
            try:
                ua = {'User-Agent': UserAgent().random}
                url = f'https://mirror-h.org/{srv}/page/{page}'
                req1 = requests.get(url, headers=ua, timeout=30)
                req2 = requests.get(url, headers=ua, timeout=30).text
                domainsw = re.findall(r'300px;"><a href="https://mirror-h.org/zone/(.*?)/">(.*?)</a></td>', req2)
                domainsx = [item[1] for item in domainsw]
                if domainsx:
                    for xxx in domainsx:
                        parsed_url = urlparse(xxx)
                        domains = parsed_url.netloc
                        open('allMirrorGrab.txt', 'a+').write(domains + '\n')
                    print(f'{blue}Mirror-H {white}| {yellow}Page : {green}{page} {white}| {yellow}Grabbed : {green}{len(domainsx)} {white}Domains')
                else:mirrorh(page,toPage, srv)
            except:pass
    except:pass
                
                
                

def runAll():
    page, toPage, srv = inputPage()
    defacerNet(page,toPage, srv)
    mirrorh(page,toPage, srv)
    defacermirror(page,toPage, srv)
    haxorid(page,toPage, srv)
    
    
if __name__ == "__main__":
    runAll()