import requests, json, colorama, sys, os
from colorama import Fore

def IpTracker():
  os.system('clear')

print(f"""{Fore.GREEN}

██╗░░░░░██╗░░░██╗██╗░░██╗███╗░░██╗██╗░██████╗░██╗░░██╗████████╗
██║░░░░░██║░░░██║╚██╗██╔╝████╗░██║██║██╔════╝░██║░░██║╚══██╔══╝
██║░░░░░██║░░░██║░╚███╔╝░██╔██╗██║██║██║░░██╗░███████║░░░██║░░░
██║░░░░░██║░░░██║░██╔██╗░██║╚████║██║██║░░╚██╗██╔══██║░░░██║░░░
███████╗╚██████╔╝██╔╝╚██╗██║░╚███║██║╚██████╔╝██║░░██║░░░██║░░░
╚══════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░
""")

print(f"{Fore.RED}Luxnight, A Basic IP Tracker\n")


print(f"{Fore.BLUE}© {Fore.RED}Developed By Shake")
print(f"{Fore.LIGHTGREEN_EX}+----------------------------+")
print(f"{Fore.MAGENTA}Rastrea Una Direccion IP\n")
IP = input(f"{Fore.LIGHTMAGENTA_EX}IP>> ")

IP = IP
API = 'http://ip-api.com/json/'

try:
        data = requests.get(API+IP).json()
        sys.stdout.flush()
        print(f"{Fore.GREEN}[+] {Fore.BLUE}IP: {Fore.YELLOW}", data['query'])
        print(f"{Fore.LIGHTGREEN_EX}+----------------------------+")
        print(f"{Fore.GREEN}[+] {Fore.BLUE}ISP: {Fore.YELLOW}", data['isp'])
        print(f"{Fore.LIGHTGREEN_EX}+----------------------------+")
        print(f"{Fore.GREEN}[+] {Fore.BLUE}Organización: {Fore.YELLOW}", data['org'])
        print(f"{Fore.LIGHTGREEN_EX}+----------------------------+")
        print(f"{Fore.GREEN}[+] {Fore.BLUE}Ciudad: {Fore.YELLOW}", data['city'])
        print(f"{Fore.LIGHTGREEN_EX}+----------------------------+")
        print(f"{Fore.GREEN}[+] {Fore.BLUE}Región: {Fore.YELLOW}", data['region'])
        print(f"{Fore.LIGHTGREEN_EX}+----------------------------+")
        print(f"{Fore.GREEN}[+] {Fore.BLUE}Longitud: {Fore.YELLOW}", data['lon'])
        print(f"{Fore.LIGHTGREEN_EX}+----------------------------+")
        print(f"{Fore.GREEN}[+] {Fore.BLUE}Latitud: {Fore.YELLOW}", data['lat'])
        print(f"{Fore.LIGHTGREEN_EX}+----------------------------+")
        print(f"{Fore.GREEN}[+] {Fore.BLUE}Zona Horaria: {Fore.YELLOW}", data['timezone'])
        print(f"{Fore.LIGHTGREEN_EX}+----------------------------+")
        print(f"{Fore.GREEN}[+] {Fore.BLUE}Código Zip: {Fore.YELLOW}", data['zip'])
        print(f"{Fore.LIGHTGREEN_EX}+----------------------------+")
        print(f"{Fore.GREEN}[+] {Fore.CYAN}Contacto: zScorpion16@proton.me")

except KeyboardInterrupt:
        print(f"\n")
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print(f"{Fore.RED}[-] {Fore.MAGENTA}Por Favor Revise Su Conexión A Internet.")
sys.exit(2)
os.system("clear")

IpTracker()
