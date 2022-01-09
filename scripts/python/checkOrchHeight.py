#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# TaxiStake - Check Orchestrator Height
# Github: taxistake
# Based on original script by BlockNgine Validator
#
# 1.0 - Initial release (internal)
#
version = '1.0'

# Import modules
import requests
import json
#from utilities import Utilities

baseURL = "http://localhost:1317/peggy/v1/oracle/event"
peggoNodes = {
    'myNode': f"{baseURL}/umee1hn9ewq285ytuqpcqdhfcfy0ppw64qh5nnhfh8d",
    'externalNode1': f"{baseURL}/umee1mhwp96xs48ly7urmn0mlyxs9fzg660tp0zl964",
    'externalNode2': f"{baseURL}/umee1hkkf84lanaqzdq684rpf2ud7vj8ax7nmvgza3n"
}
ethereumEventNonceArray = []

#def _sendMail(message: str)-> None:
#    Utilities().send_email(
#        receiver_email="me@domain.com", 
#        sender_email="cron@domain.com",
#        subject="Peggo Alert Warning", 
#        text=message
#    )

try:
    for node in peggoNodes:
        json_response = requests.get(url=peggoNodes[node])
        response = json.loads(json_response.text)  # convert from json to python
        ethereumEventNonceArray.append(response['last_claim_event']['ethereum_event_nonce'])
except Exception as error:
    print('[+] Error! ', error)
    #_sendMail(message=f"Unknown error: {error}")

if ethereumEventNonceArray[0] !=  ethereumEventNonceArray[1] \
    or ethereumEventNonceArray[0] !=  ethereumEventNonceArray[2] \
    or ethereumEventNonceArray[1] !=  ethereumEventNonceArray[2]:
    print('[+] Peggo event nonces do not match. Please check service. ', ethereumEventNonceArray)
    ##_sendMail(message=f"Peggo event nonces to not match please check: {ethereumEventNonceArray}")
else:
    print(ethereumEventNonceArray)
