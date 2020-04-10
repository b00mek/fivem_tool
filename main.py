import os
import time
import requests
import subprocess
import urllib
import webbrowser
import colorama
from colorama import Fore
import shutil
import ctypes, sys
import random
import string

colorama.init()


homepath = os.path.expanduser(os.getenv('USERPROFILE'))

ctypes.windll.kernel32.SetConsoleTitleW(f"fivem_tool | made by: frosted_team")


clear = lambda : os.system("cls")


def wylaczproces(nazwa):
    os.system("taskkill /f /im " + nazwa)


def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def login():

    haslo = randomString(10)

    print(f'Your password: {haslo}')
    password = str(input("> "))


    if password == haslo:
        print(f"{Fore.GREEN}Logged in!")
    else:
        print(f"{Fore.RED}Wrong password!{Fore.RESET}")
        login()

login()





def usuwanie_fivem():

    wylaczproces('FiveM.exe')
    wylaczproces('Steam.exe')

    print('Deleting Temp Folder')
    shutil.rmtree(homepath + '/AppData/Local/Temp', ignore_errors=True)
    time.sleep(3)

    print('Deleting DigitalEntitlements folder')
    shutil.rmtree(homepath + '/AppData/Local/Temp/DigitalEntitlements', ignore_errors=True)

    print('Deleting CitizenFX files')
    shutil.rmtree(homepath + '/AppData/Roaming/CitizenFX', ignore_errors=True)
    shutil.rmtree(homepath + '/Saved Games/CitizenFX', ignore_errors=True)

def spoofer():

    url = 'https://frostedflakes.pl/fivem/spoofer/crackedSpoofer.exe'
    url2 = 'https://frostedflakes.pl/fivem/spoofer/MetroFramework.Design.dll'
    url3 = 'https://frostedflakes.pl/fivem/spoofer/MetroFramework.dll'
    url4 = 'https://frostedflakes.pl/fivem/spoofer/MetroFramework.Fonts.dll'

    try:
        os.startfile(homepath + '\AppData\Roaming\FiveM_\crackedSpoofer.exe')
        print('Launching Spoofer')
    except FileNotFoundError:
        if not os.path.exists(homepath+'\Appdata\Roaming\FiveM_'):
            os.makedirs(homepath+'\Appdata\Roaming\FiveM_')
        urllib.request.urlretrieve(url, homepath+'\Appdata\Roaming\FiveM_\crackedSpoofer.exe')
        urllib.request.urlretrieve(url2, homepath+'\Appdata\Roaming\FiveM_\MetroFramework.Design.dll')
        urllib.request.urlretrieve(url3, homepath+'\Appdata\Roaming\FiveM_\MetroFramework.dll')
        urllib.request.urlretrieve(url4, homepath+'\Appdata\Roaming\FiveM_\MetroFramework.Fonts.dll')





        os.startfile(homepath+'\Appdata\Roaming\FiveM_\crackedSpoofer.exe')




print(f'''{Fore.CYAN}
   __ _                         _              _ 
  / _(_)                       | |            | |
 | |_ ___   _____ _ __ ___     | |_ ___   ___ | |
 |  _| \ \ / / _ \ '_ ` _ \    | __/ _ \ / _ \| |
 | | | |\ V /  __/ | | | | |   | || (_) | (_) | |
 |_| |_| \_/ \___|_| |_| |_|    \__\___/ \___/|_|
 
           {Fore.CYAN}### {Fore.RED}made by: frosted_team{Fore.CYAN} ###

''')


print(f'Select your option')

option = input('''

[ 1 ] FiveM CitizenFX deleter ( fivem local storage deleter ) 
[ 2 ] DISCORD_RPC disabler
[ 3 ] FiveM Local Storage Deleter + Spoofer

''')

if option == ('1'):
    clear()

    option = input('Are you sure [y/n]: ')
    if option == ('y'):

        usuwanie_fivem()

    if option == ('n'):
        exit()


if option == ('2'):

    print('disabling discord_rpc')
    os.rename(homepath + '/AppData/Roaming/Discord/0.0.306/modules/discord_rpc', homepath + '/AppData/Roaming/Discord/0.0.306/modules/discord_rpc.disabled')
    print('discord_rpc disabled')


if option == ('3'):
    print('Deleting FiveM local storage')
    usuwanie_fivem()
    time.sleep(5)
    print('Launching Spoofer')
    time.sleep(5)
    spoofer()

input('Press enter to exit')
