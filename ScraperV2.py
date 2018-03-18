#GET WEBSITE
import requests
from lxml import html

#COLORS AND STYLES
from colorama import init, Fore, Back, Style
init(convert=True)

#MAIL SYSTEM
import smtplib

#load data
import json
import os
current_file_path = __file__
current_file_dir = os.path.dirname(__file__)
configfile = os.path.join(current_file_dir, "settings.json")
with open(configfile, 'r') as f:
        jsonfile = json.load(f)


#USING PASSWORDS 
import loginsystem
import getpass
if jsonfile["useKeyring"]:
    import keyring

#refresh data
import time

#check new content
import hashlib


#login if ask everytime
if jsonfile["askEveryRun"] and jsonfile["useKeyring"]:
    email = input('Introduce email: ')
    YourPW = keyring.get_password("MyBBScraper", email)
elif jsonfile["askEveryRun"] and not jsonfile["useKeyring"]:
    email = input('Introduce email: ')
    YourPW = getpass.getpass("Introduce password: ")

YourPW = 'test' 

#Scrape links
login_url = "https://greysec.net/member.php?action=login"
web2scrape = "https://greysec.net/index.php"
PMs2scrape = "https://greysec.net/private.php"

DATA = {
    "url": login_url,
    "action": "do_login",
    "submit": "Login",
    "quick_login": "1",
    "quick_username": jsonfile["email"],
    "quick_password": YourPW,
    }



def PrintWeb(og_data, authorlist, ThreadStatus):
    print(Style.BRIGHT + "  RECENT THREADS\n")
    for x in range(0, 11, 1):
        Thread = og_data[2*x]
        Cat = og_data[2*x+1]
        author = authorlist[x]
        Status = ThreadStatus[x]

        if (Status == 'ps_status ps_minion'):
            print(Style.BRIGHT + '  (!) '+ Thread + Style.RESET_ALL + ' by ' + author)
        else:
            print(Style.RESET_ALL + '    '+ Thread + ' by ' + author)
        print(Style.RESET_ALL + '    ' + Cat +'\n')

def SendMail():
    print('not implemented')
    #NEED TO CHANGE FUNCTION NOT IMPLEMENTED YET
    # gmail_user = 'you@gmail.com'  
    # gmail_password = 'P@ssword!'

    # sent_from = gmail_user  
    # to = ['me@gmail.com', 'bill@gmail.com']  
    # subject = 'OMG Super Important Message'  
    # body = 'Hey, what\'s up?\n\n- You'

    # email_text = """\  
    # From: %s  
    # To: %s  
    # Subject: %s

    # %s
    # """ % (sent_from, ", ".join(to), subject, body)

    # try:  
    #     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    #     server.ehlo()
    #     server.login(gmail_user, gmail_password)
    #     server.sendmail(sent_from, to, email_text)
    #     server.close()

    #     print('Email sent!')
    # except:  
    #     print('Something went wrong...')

        
def PMemail(tree):
    with requests.Session() as session:
        post = session.post(login_url, data=DATA)
        raw = session.get(PMs2scrape)
        pmwebsite = html.fromstring(raw.content)

        pm = pmwebsite.xpath('//*[@id="container"]/div[4]/form/table/tr/td[2]/table/tr/td[3]/strong/a/text()')
        
        print(Style.RESET_ALL +'    ' + str(pm) + '\n')

    #SEND EMAIL NOT IMPLEMENTED
        # SendMail()

    

def PM(tree):
    print(Style.BRIGHT + "  PM SYSTEM")
    # NOTIFICATION SYSTEM NOT IMPLEMENTED
    # md5 = os.path.join(current_file_dir, "md5.json")
    # with open(md5, 'r') as f:
    #     md5file = json.load(f)

    #     oldmd5 = jsonfile["md5"]

        #Get messsages
    PMMsg = tree.xpath('//*[@id="pm_notice"]/div[2]/strong/text()')
    
    pm2hash = ''.join(PMMsg)
    md5 = hashlib.md5(pm2hash.encode("utf")).hexdigest()
    

    if PMMsg:
        print(Style.BRIGHT + '    ' + str(PMMsg))
        
        if md5 != oldmd5:
            with open(md5, 'w') as f:
                json.dump(md5, f)
            PMemail(tree)
    else:
        print(Style.RESET_ALL +'    No PM\'s \n\n')

def getWeb(r):
    
    #Get website
    web =requests.get('https://greysec.net/index.php')
    tree = html.fromstring(r.content)
    #PM
    PM(tree)
                #Threads
    og_data = tree.xpath('//*[@id="prostats_table"]/table/tbody/tr/td[1]/table/tr[2]/td/table//@title')
    authorlist = tree.xpath('//*[@id="prostats_table"]/table/tbody/tr/td[1]/table/tr[2]/td/table/tr/td[4]/a/text() | //*[@id="prostats_table"]/table/tbody/tr/td[1]/table/tr[2]/td/table/tr/td[4]/a/span/strong/text() | //*[@id="prostats_table"]/table/tbody/tr/td[1]/table/tr[2]/td/table/tr/td[4]/a/span/text()')  
    ThreadStatus = tree.xpath('//*[@id="prostats_table"]/table/tbody/tr/td[1]/table/tr[2]/td/table/tr/td[1]/span/@class')

    SearchSpam(og_data)
    PrintWeb(og_data, authorlist, ThreadStatus)
        
    

def SearchSpam(og_data):
    print(Style.BRIGHT + "  ANTI-SPAM")
    #Look for words in title, which can be spam
    if ("CVV" in str(og_data)):
        print(Style.BRIGHT + '    Found possible SPAM...\n')
        #send mail but save threa22d title
            #mail subject: thread title
            #mail body: thread body
    else:
        print(Style.RESET_ALL +'    No SPAM detected \n')

def login():
    with requests.Session() as session:
        post = session.post(login_url, data=DATA)
        r = session.get(web2scrape)
        getWeb(r)

def main():
    while True:
        print(Fore.GREEN + Style.BRIGHT +  """
       _____                              _   _       _   _  __ _           _   _                 
      / ____|                            | \ | |     | | (_)/ _(_)         | | (_)                
     | |  __ _ __ ___ _   _ ___  ___  ___|  \| | ___ | |_ _| |_ _  ___ __ _| |_ _  ___  _ __  ___ 
     | | |_ | '__/ _ \ | | / __|/ _ \/ __| . ` |/ _ \| __| |  _| |/ __/ _` | __| |/ _ \| '_ \/ __|
     | |__| | | |  __/ |_| \__ \  __/ (__| |\  | (_) | |_| | | | | (_| (_| | |_| | (_) | | | \__ \
     
      \_____|_|  \___|\__, |___/\___|\___|_| \_|\___/ \__|_|_| |_|\___\__,_|\__|_|\___/|_| |_|___/
                       __/ |                                                                      
                      |___/     %s Written by MemoriasIT    
    """ % (jsonfile["version"]) + Style.RESET_ALL)
        login()
        time.sleep(int(jsonfile["RefreshRate"]))

main()
