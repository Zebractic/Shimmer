import os
import requests
import json
import sys
import time

title = """


\33[31m  ██████  ██░ ██  ██▓ ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  
▒██    ▒ ▓██░ ██▒▓██▒▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒██▀▀██░▒██▒▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒
  ▒   ██▒░▓█ ░██ ░██░▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒░▓█▒░██▓░██░▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▓  ░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░ ▒ ░▒░ ░ ▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░   ░  ░░ ░ ▒ ░░      ░   ░      ░      ░     ░░   ░ 
      ░   ░  ░  ░ ░         ░          ░      ░  ░   ░     
                                                           


"""
try:
    while True:
        os.system('title SHIMMER')
        os.system('cls')
        print(title)

        print('[1] IP Lookup')

        print ('[2] Reverse Shell(*Bad USB Required*)')

        x = input(' \n ENTER OPTION NUMBER: ')

        if x == '1':
            os.system('cls')
            print('IP LOOKUP')
            ip = input(' \n ENTER IP: ')
            r = requests.get(f'http://ip-api.com/json/{ip}')
            data = r.json()
            os.system('cls')
            print('RESULTS\n')
            print(f'Country:  {data['country']}')
            print(f'City:  {data['city']}')
            print(f'TimeZone:  {data['timezone']}')
            time.sleep(10)
        else:
            os.system('cls')
            print(' \n Option is either curently in testing or is not available!')
            time.sleep(2)
except KeyboardInterrupt:
    print('Returning...')
    time.sleep(2)

