#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# TaxiStake - UMEE Estimate Bridge Fee
# Github: taxistake
#
# 1.0 - Initial release (internal)
#
version = '1.0'

# Library imports
import os
import sys
import json
import requests

# Variables
eth_price_endpoint = 'https://peggo-fakex-qhcqt.ondigitalocean.app/api/v3/simple/price?ids=ethereum&vs_currencies=usd'
umee_price_endpoint = 'https://peggo-fakex-qhcqt.ondigitalocean.app/api/v3/simple/token_price/ethereum?contract_addresses=0xe54fbaecc50731afe54924c40dfd1274f718fe02&vs_currencies=usd'

# Color stuffz
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_title_screen():
    # Print program title banner
    print('')
    print(bcolors.BOLD + '[🚕] TaxiStake UMEE Bridge Fee Estimation Script - ' + bcolors.OKGREEN + version + bcolors.ENDC)
    print(bcolors.BOLD + '[+] ------------------------------' + bcolors.ENDC)
    #print(bcolors.BOLD + '[+] Program Version: ' + bcolors.FAIL + version + bcolors.ENDC)

def getEthPrice():
    r = requests.get(eth_price_endpoint).json()
    return(r['ethereum']['usd'])

def getUmeePrice():
    r = requests.get(umee_price_endpoint).json()
    return(r['0xe54fbaecc50731afe54924c40dfd1274f718fe02']['usd'])

def main():
    #(((0.00225*ETH_PRICE)/100)/UMEE_PRICE)=BRIDGE_FEE (in UMEE). ATM 0.008UMEE or 8000uumee

    eth_price = getEthPrice()
    print('[+] ETH Price:', bcolors.OKGREEN + str(eth_price) + bcolors.ENDC, 'USD')

    umee_price = getUmeePrice()
    print('[+] UMEE Price:', bcolors.WARNING + str(umee_price) + bcolors.ENDC, 'USD')

    bridge_fee = (((0.00225*eth_price/100)/umee_price))
    print('[+] Recommended Bridge Fee:', bcolors.OKBLUE + str(bridge_fee) + bcolors.ENDC, 'UMEE or ' + bcolors.OKBLUE + str(bridge_fee*1000000) + bcolors.ENDC, 'uumee')

if __name__ == '__main__':
     print_title_screen()
     main()
     sys.exit(bcolors.BOLD + '[+] The program has completed' + bcolors.ENDC)
