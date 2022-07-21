#bycripton


import argparse
import requests, json
import sys
from sys import argv
import os



parser = argparse.ArgumentParser()

parser.add_argument ("-i", help= "target/host IP address", type=str, dest='target', required=True )

args = parser.parse_args()

BLACK = '\033[30m'
red = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

print (red+"""

 ██████╗██████╗ ██╗██████╗ ████████╗ ██████╗ ███╗   ██╗
██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝██╔═══██╗████╗  ██║
██║     ██████╔╝██║██████╔╝   ██║   ██║   ██║██╔██╗ ██║
██║     ██╔══██╗██║██╔═══╝    ██║   ██║   ██║██║╚██╗██║
╚██████╗██║  ██║██║██║        ██║   ╚██████╔╝██║ ╚████║
 ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═══╝
                                                       
"""+red)
print (red+"<----------SCRIPT BY CRIPTON---------->\n")


ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = GREEN +"[+]"
        b = CYAN+"[+]"
        print (a, "Víctima:", data['query'])
        print(red+"<--------------->"+red)
        print (b, "ISP:", data['isp'])
        print(red+"<--------------->"+red)
        print (a, "Organización:", data['org'])
        print(red+"<--------------->"+red)
        print (b, "Ciudad:", data['city'])
        print(red+"<--------------->"+red)
        print (a, "Region:", data['region'])
        print(red+"<--------------->"+red)
        print (b, "Longitud:", data['lon'])
        print(red+"<--------------->"+red)
        print (a, "Latitud:", data['lat'])
        print(red+"<--------------->"+red)
        print (b, "zona horaria:", data['timezone'])
        print(red+"<--------------->"+red)
        print (a, "Zip code:", data['zip'])
        print (" "+YELLOW)

except KeyboardInterrupt:
        print ('terminado'+GREEN)
        sys.exit(0)
except requests.exceptions.ConSnectionError as e:
        print (red+"[~]"+" revise su coonexion a internet!"+clear)
sys.exit(1)
