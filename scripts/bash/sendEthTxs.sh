#!/bin/bash

# STEP 1 : CHANGE LOG NAMES BEFORE EXECUTION
log_tx_hash="eth-to-umee.hashes"

# STEP 2 : VERIFY ALL ADDRESSES AND KEYRINGS
cosmos_amount="100" #uumee
erc_contract_address="0xe54fbaecc50731afe54924c40dfd1274f718fe02"  # UMEE ERC-20 contract
cosmos_dest_address="umee100000000000000000000000000000000000000"  # Dest address on umee
eth2_pk="0000000000000000000000000000000000000000000000000000000000000" # Clear text ETH priv key. Better: Use envar. Even better: Use vault/HSM
#$ETH_PK_CLEAN = envvar TODO: This can be more secure with a vault
#$ETH_RPC = envvar

# STEP 3: SET MAX AMOUNT OF TXS NEEDED
cosmos_tx_count=5

# OTHER
c=1

# Print title
printf "\033[32;1m\n\n[🚕] TaxiStake's Eth-to-UMEE Transaction Script\n[+] Github - taxistake\n\033[0m\n" 

# Main loop
(

  # ETH to COSMOS Transactions
  while [ $c -le $cosmos_tx_count ]
  do
          #DEBUG: echo c: $c
          tx_status=$(peggo bridge send-to-cosmos $erc_contract_address $cosmos_dest_address $cosmos_amount --eth-pk=$eth2_pk --eth-rpc=$ETH_RPC 2>&1)
          #DEBUG: echo $tx_status
	  tx_hash=$(echo $tx_status | cut -d ":" -f 9 | tr -d " ")  
          echo "ETH TX $c - $tx_hash"
	  echo $tx_hash >> $log_tx_hash
          sleep 20
	  ((c=c+1))
  done

)
