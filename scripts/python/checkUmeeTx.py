#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# TaxiStake - Check UMEE TX Script
# Github: taxistake
#
# 1.0 - Initial release (internal)
#
version = '1.0'

# Library imports
import os
import sys
import argparse
import subprocess
import multiprocessing
import time
import pickle
 
import json
 
from tqdm import tqdm
from subprocess import check_output
from multiprocessing import Process

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
    print(bcolors.BOLD + '[🚕] TaxiStake UMEE TX Check Script - ' + bcolors.OKGREEN + version + bcolors.ENDC)
    print(bcolors.BOLD + '[+] ------------------------------' + bcolors.ENDC)
    #print(bcolors.BOLD + '[+] Program Version: ' + bcolors.FAIL + version + bcolors.ENDC)

def checkTx(txs):
    #print('Checking TXs')
    global hash_dict
    code_zero = 0
    code_error = 0
    hash_dict = {"txhash":[],"code":[],"code_reason":[]};
    for tx in tqdm(txs, ncols=80, position=0, leave=False, ascii=False):
        if len(tx) > 0 and tx != '' and tx != '\n':
            output = subprocess.check_output(['umeed', 'query', 'tx', '--output=json', '--type=hash', tx.strip()]) 
            json_out = json.loads(output)
            #print(json_out)

            code = json_out['code']
            tx_hash = json_out['txhash']
        
            if str(code) == '0':
                print('\nTXID: ', tx_hash, 'Code: ' + bcolors.OKGREEN, str(code) + bcolors.ENDC )
                code_zero += 1
            else:
                print('\nTXID: ', tx_hash, 'Code: ' + bcolors.WARNING, str(code) + bcolors.ENDC )
                code_error += 1
            time.sleep(0.1)
    #return(hash_dict)
    print('\nSuccessful TXs: ' + bcolors.OKGREEN, str(code_zero) + bcolors.ENDC, "Error TXs:" + bcolors.FAIL, str(code_error) + bcolors.ENDC)
    return()

def main(argv=sys.argv[1:]): 
    # Globals
    global i
    global txs

    parser = argparse.ArgumentParser(description='Checks UMEE Transaction status for codes and errors')
    parser.add_argument('-f', '--file', default=False,
        type=argparse.FileType('r'),
        help='the file name containing UMEE TXs')
    args = parser.parse_args(args=argv) 

    if args.file:
        hashfile = args.file
        open(hashfile.name, 'r')
        Lines = hashfile.readlines()
        print(bcolors.BOLD + '[+] Checking TXs in file: ' + bcolors.OKGREEN + str(hashfile.name) + bcolors.ENDC)
        checkTx(Lines)
    else:
        parser.print_help(sys.stderr)

if __name__ == '__main__':
     print_title_screen()
     main()
     sys.exit(bcolors.BOLD + '[+] The program has completed' + bcolors.ENDC)
