import requests
from lxml import html

from colorama import init, Fore, Back, Style
init(convert=True)

import smtplib

# Introduce your forum data here
YourUser = ""
YourPW = ""

# Introduce your e-mail data here
fromaddr  = ''
toaddrs = ''
SMTP = ''

#Scrape links
login_url = "https://greysec.net/member.php?action=login"
web2scrape = "https://greysec.net/index.php"
PMs2scrape = "https://greysec.net/private.php"

DATA = {
    "url": login_url,
    "action": "do_login",
    "submit": "Login",
    "quick_login": "1",
    "quick_username": YourUser,
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

        
def PMemail(tree):
    with requests.Session() as session:
        post = session.post(login_url, data=DATA)
        raw = session.get(PMs2scrape)
        pmwebsite = html.fromstring(raw.content)

        pm = pmwebsite.xpath('//*[@id="container"]/div[4]/form/table/tr/td[2]/table/tr/td[3]/strong/a/text()')
        
        print(Style.RESET_ALL +'    ' + str(pm) + '\n')

    #SEND EMAIL
    

def PM(tree):
    print(Style.BRIGHT + "  PM SYSTEM")
    PMMsg = str(tree.xpath('//*[@id="pm_notice"]/div[2]/strong/text()'))

    

    if PMMsg:
        print(Style.BRIGHT + '    ' + PMMsg)
        #show pms and send mail
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
        #send mail but save thread title
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
    print(Fore.GREEN + Style.BRIGHT +  """
   _____                              _   _       _   _  __ _           _   _                 
  / ____|                            | \ | |     | | (_)/ _(_)         | | (_)                
 | |  __ _ __ ___ _   _ ___  ___  ___|  \| | ___ | |_ _| |_ _  ___ __ _| |_ _  ___  _ __  ___ 
 | | |_ | '__/ _ \ | | / __|/ _ \/ __| . ` |/ _ \| __| |  _| |/ __/ _` | __| |/ _ \| '_ \/ __|
 | |__| | | |  __/ |_| \__ \  __/ (__| |\  | (_) | |_| | | | | (_| (_| | |_| | (_) | | | \__ \
 
  \_____|_|  \___|\__, |___/\___|\___|_| \_|\___/ \__|_|_| |_|\___\__,_|\__|_|\___/|_| |_|___/
                   __/ |                                                                      
                  |___/     V1.1 Written by MemoriasIT

                  
"""+ Style.RESET_ALL)
    login()

    ##################  WORKING FEATURES  ##################
    #   * Get threads and check if new *BUG: users with s
    #   * Search for spam looking for keywords in threads
    #
    ##################  WORKING FEATURES  ##################


    ##################       TO-DO      ##################
    #
    # * SPAM FIND = SEND EMAIL/ALERT
    # * PM FIND = SEND EMAIL/ALERT
    # * ANSWER PMS
    # * MARK ALL PMS AS READ
    # * LOGIN SYSTEM
    # * CRON/TASK SCHEDULER
    #
    ##################       TO-DO      ##################
    
main()
