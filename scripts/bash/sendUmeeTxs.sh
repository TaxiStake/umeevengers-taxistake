#!/bin/bash

# STEP 1 : CHANGE LOG NAMES BEFORE EXECUTION
log_tx_hash="umee-to-eth.hashes"

# STEP 2 : VERIFY ALL ADDRESSES AND KEYRINGS
eth_address="0x0000000000000000000000000000000000000000" #Dest ETH address
amount="300uumee"
bridge_fee="10000uumee"
chain_id="umee-alpha-mainnet-2"
sending_alias="hot_wallet" #Alias of address/keypair to send from
keyring="test" # Keyring containing address/keypair to send from

# STEP 3: SET MAX AMOUNT OF TXS NEEDED
eth_tx_count=5

# OTHER
e=1

# Print title
printf "\033[32;1m\n\n[🚕] TaxiStake's UMEE-To-Eth Transaction Script\n[+] Github - taxistake\n\033[0m\n" 

# Main loop
(

  # UMEE to ETH Transactions
  while [ $e -le $eth_tx_count ]
  do
	  #DEBUG: echo e: $e
	  #WARNING: Will not confirm before signing and broadcasting if using local test wallet
	  tx_status=$(umeed tx peggy send-to-eth $eth_address $amount $bridge_fee --from $sending_alias --keyring-backend $keyring --chain-id $chain_id -y)
	  #DEBUG: echo $tx_status
	  tx_hash=$(echo $tx_status | jq -r .txhash)  
	  echo "UMEE TX $e - $tx_hash"
	  echo $tx_hash >> $log_tx_hash
	  sleep 12
	  ((e=e+1))
  done

)
