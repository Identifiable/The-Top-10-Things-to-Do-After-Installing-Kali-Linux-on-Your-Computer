#!/usr/bin/python3

import os
os.system('clear')
print('')
print('')
print('')
print('')
print('     @iot_botnet')
print('|---------------------------------------------------|')
print('|   Simple Kali Autoinstaller by @iot_botnet        |')
print('|---------------------------------------------------|')
print('')
print('//[1]Kali linux AutoInstaller (Good features.')
print('')
print('')
print('')
choix1 = input("Sections (1): ")
os.system('clear')
if choix1 == '1':
  os.system('clear')
choix2 = input("Do you really want to proceed ? [Y/N] ")
Y = "Y"
if choix2 == 'N':
  os.system('exit')
if choix2 == 'Y':
  os.system('clear')
print('  .---------.')
print('  |.-------.|')
print('| | > :D  # ||')
print('  | | | |')
print('  | "-------etf')
print('.- ^ --------- ^ -.')
print('| ---~   Installing git .... |')
print('"-------------'')')
os.system('sudo apt-get install git')
os.system('clear')
print('  .---------.')
print('  |.-------.|')
print('| | > :D  # ||')
print('  | | | |')
print('  | "-------etf')
print('.- ^ --------- ^ -.')
print('| ---~   Updating ... |')
print('"-------------'')')
os.system('clear')
os.system('sudo apt-update')
os.system('clear')
print('  .---------.')
print('  |.-------.|')
print('| | > :D  # ||')
print('  | | | |')
print('  | "-------etf')
print('.- ^ --------- ^ -.')
print('| ---~   Installing Tilix .... |')
print('"-------------'')')
os.system('sudo apt-get install tilix')
os.system('clear')
print('  .---------.')
print('  |.-------.|')
print('| | > :D  # ||')
print('  | | | |')
print('  | "-------etf')
print('.- ^ --------- ^ -.')
print('| ---~   Installing T00ls .... |')
print('"-------------'')')
os.system('sudo apt-get install maltego metasploit-framework burpsuite wireshark aircrack-ng hydra nmap beef-xss nikto')
os.system('clear')
print('  .---------.')
print('  |.-------.|')
print('| | > :D  # ||')
print('  | | | |')
print('  | "-------etf')
print('.- ^ --------- ^ -.')
print('| ---~   Installing the last version of Tor  .... |')
print('"-------------'')')
os.system('sudo add-apt-repository ppa:webupd8team/tor-browser')
os.system('sudo apt-get update')
os.system('sudo apt-get install tor-browser')
os.system('clear')
os.system('wget -O- ''https://pgp.mit.edu/pks/lookup?op=get&search=0xA3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89''')
os.system('sudo apt-key add -')
os.system('apt-get update')
os.system('apt-get install tor deb.torproject.org-keyring')
os.system('clear')
print('  .---------.')
print('  |.-------.|')
print('| | > :D  # ||')
print('  | | | |')
print('  | "-------etf')
print('.- ^ --------- ^ -.')
print('| ---~   Installing a Good Code Editor  .... |')
print('"-------------'')')
os.system('apt-get install gvfs gvfs-common gvfs-daemons gvfs-libs gconf-service gconf2 gconf2-common gvfs-bin psmisc')
choix5 = input("DO YOU WANT ME TO MAKE YOU A EXPLOIT FOLDER ON YOUR ROOT DESKTOP FOR RUBBER DUCKY ? [Y/N]")
if choix5 == 'Y':
  os.system('cd $root')
  os.system('mkdir Exploits')
  os.system('cd Exploits')
  os.system('git clone https://github.com/hak5darren/USB-Rubber-Ducky')
  os.system('clear')
  os.system('java -jar encoder.jar -i input_payload.txt -o inject.bin')
print('  .---------.')
print('  |.-------.|')
print('| | > :D  # ||')
print('  | | | |')
print('  | "-------etf')
print('.- ^ --------- ^ -.')
print('| ---~   Change SSH Keys and default password .... |')
print('"-------------'')')
os.system('clear')
os.system('cd /etc/ssh/')
os.system('dpkg-reconfigure openssh-server')
os.system('clear')
if choix5 == 'N':
  os.system('exit')





