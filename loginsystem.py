#passwords
import keyring
import getpass

#save data
import json
import os
current_file_path = __file__
current_file_dir = os.path.dirname(__file__)
configfile = os.path.join(current_file_dir, "settings.json")


def validAnswer(prompt):
	while True:
		try:
			return {"yes":True,"no":False}[input(prompt).lower()]
		except KeyError:
			print("Invalid input please enter yes or no!")


def main():


	with open(configfile, 'r') as f:
		jsonfile = json.load(f)
		
		#FIRST RUN
		if jsonfile["first_run"]:
			
			print('''

		   _____             __ _       
		  / ____|           / _(_)      
		 | |     ___  _ __ | |_ _  __ _ 
		 | |    / _ \| '_ \|  _| |/ _` |
		 | |___| (_) | | | | | | | (_| |
		  \_____\___/|_| |_|_| |_|\__, |
		                           __/ |
		  Developed by MemoriasIT |___/ 

				''')


			prompt = 'Would you like to be asked for credentials every run? '
			askEveryRun = validAnswer(prompt)

			#Requires Mac OS X Keychain/Freedesktop Secret Service (requires secretstorage)/KWallet (requires dbus)/Windows Credential Locker
			prompt = 'Would you like to use the KeyRing feature? (see requirements in readme)'
			useKeyring = validAnswer(prompt)

			if not askEveryRun:
				prompt = 'What is your email? '
				email = input(prompt)
				if useKeyring:	
					YourPW = getpass.getpass("Introduce password: ")
					keyring.set_password("MyBBScraper", email, YourPW)
			else:
				email = ''
				

			prompt = 'Would you like to use the SMTP notification feature?'
			useSMTP = validAnswer(prompt)

			if useSMTP:
				SMTP = input('Introduce SMTP:Port ')
				fromaddr  = input('From: ')
				toaddrs = input('To: ')
			else:
				SMTP = ''
				fromaddr  = ''
				toaddrs = ''
				


			prompt = 'How often would you like to refresh the data? (s)'
			RefreshRate = input(prompt)

			first_run = False

			data = {
		   'first_run' : False,
		   'askEveryRun' : askEveryRun,
		   'email' : email,
		   'RefreshRate' : RefreshRate,
		   'useKeyring' : useKeyring,
		   'useSMTP' : useSMTP,
		   'fromaddr' : fromaddr,
		   'toaddrs' : toaddrs,
		   'version' : 'V2.3'
			}

			# Writing JSON data
			with open(configfile, 'w') as f:
				json.dump(data, f)

		if jsonfile["askEveryRun"] and not jsonfile["first_run"]:

			print("""
		  _      ____   _____ _____ _   _ 
		 | |    / __ \ / ____|_   _| \ | |
		 | |   | |  | | |  __  | | |  \| |
		 | |   | |  | | | |_ | | | | . ` |
		 | |___| |__| | |__| |_| |_| |\  |
		 |______\____/ \_____|_____|_| \_|
		  - %s Written by MemoriasIT -
		  				                  
		""" % (jsonfile["version"])) 

			askEveryRun = jsonfile["askEveryRun"]
			RefreshRate = jsonfile["RefreshRate"]
			useKeyring = jsonfile["useKeyring"]
			useSMTP = jsonfile["useSMTP"]
			fromaddr = jsonfile["fromaddr"]
			toaddrs = jsonfile["toaddrs"]
			email = ''
			





main()