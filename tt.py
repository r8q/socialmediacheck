import random, string, requests, time
from colorama import Fore
import sys, os, pyfiglet
import os
os.system("cls" or "clear")
print(Fore.MAGENTA + pyfiglet.figlet_format("glovelace", font = "cybermedium"  ))
print(Fore.LIGHTCYAN_EX +'===================  🤖  🤖  ========================')
print(Fore.BLUE +'Author 🔥	:	https://t.me/glovelace')
print(Fore.LIGHTYELLOW_EX +'Author 💎	:	https://github.com/selfweezer')
print(Fore.LIGHTBLUE_EX +'Author 💘	:	https://t.me/losersalwaysloser')
print(Fore.LIGHTBLUE_EX +'Author 💞	:	https://t.me/decryptedd')
print(Fore.LIGHTCYAN_EX +'===================  🌀  🌀  ========================')
time.sleep(.5)
hmletters = int(input('kaç harfli olmasını istersin ? : '))
print("")
websit = input('hangi web sitesi için istiyorsun : ex: instagram.com/ ')
print("")
web = list(websit)
webs = web[:-1]
webss = ''.join(webs)
#wbhook = ''
print()
time.sleep(.3)
while True:
    try:
        usernames = ('').join(random.choices(string.ascii_lowercase + string.digits, k=hmletters))
        #webhook = DiscordWebhook(url=wbhook, content=f'`{usernames}` | Might be Available or Banned on => ||`{webss}`|| |')
        r = requests.get(f'https://{websit}{usernames}')
        '''theurl=f'https://{websit}{usernames}'
        for proxy in open('proxies.txt').read().splitlines():
            try:
            r = requests.get(
            url=theurl,
            proxies={
            'https':'https://{}'.format(proxy),
            'http':'http://{}'.format(proxy)
            except:
                print("proxy error !")
            }
        )'''
        if r.status_code == 200:
            print(Fore.CYAN+"[-] "+Fore.RED + "UnAvailable"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {usernames}'+Fore.WHITE+" <=|"+Fore.CYAN+" [-]")
        else:
            print(Fore.CYAN + "[+] " + Fore.GREEN + "Available" + Fore.WHITE + ' |=>' + Fore.LIGHTMAGENTA_EX + f' {usernames}'+Fore.WHITE+" <=|" + Fore.CYAN + " [+]")
            with open("ok.txt",'a',encoding='utf8') as f:
                    f.write(f"{usernames} | Available or Banned On => {webss} |\n")
            #webhook.execute()
    except:
        pass