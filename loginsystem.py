import keyring
import getpass


##################       CONFIG      ##################
#If you want to be asked every run and not save any credentials set this to True
askEveryRun = True

#Introduce email manually
#If you don't want to store the email set this to true and will ask you for your email
askforemail = True 
email = ''

#If you don't want to use keyring set this to False you will be asked for your password
#Requires Mac OS X Keychain/Freedesktop Secret Service (requires secretstorage)/KWallet (requires dbus)/Windows Credential Locker
useKeyring = False
#Only ask for email as the keyring has been already set
alreadySaved = False

#SMTP
fromaddr  = ''
toaddrs = ''
SMTP = ''
UseSMTP = True

#How often do you want to get data
RefreshRate = 3000

#Global version
version = 'V2.2'
##################       CONFIG      ##################


def askforcredentials():
	print("""
		  _      ____   _____ _____ _   _ 
		 | |    / __ \ / ____|_   _| \ | |
		 | |   | |  | | |  __  | | |  \| |
		 | |   | |  | | | |_ | | | | . ` |
		 | |___| |__| | |__| |_| |_| |\  |
		 |______\____/ \_____|_____|_| \_|
		  - %s Written by MemoriasIT -
		  		Save the keyring
		                  
		""" % (version)) 

	if askforemail:
		email = input("Introduce email: ")
	
	if useKeyring and not alreadySaved:	
		YourPW = getpass.getpass("Introduce password: ")
		keyring.set_password("MyBBScraper", email, YourPW)


def main():
	if askEveryRun:
		askforcredentials()

main()