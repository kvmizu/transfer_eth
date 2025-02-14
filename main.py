from web3 import Web3

# Connect to Ethereum node (Infura example)
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Wallet details
sender_address = "0xYourSenderAddress"
private_key = "YourPrivateKey"
receiver_address = "0xReceiverAddress"

# Amount to send in ETH
amount = 0.01  # Example: Sending 0.01 ETH

# Convert ETH to Wei (1 ETH = 10^18 Wei)
amount_in_wei = web3.to_wei(amount, 'ether')

# Get the current gas price
gas_price = web3.eth.gas_price

# Get the nonce (transaction count) for the sender's address
nonce = web3.eth.get_transaction_count(sender_address)

# Create the transaction
tx = {
    'nonce': nonce,
    'to': receiver_address,
    'value': amount_in_wei,
    'gas': 21000,  # Standard gas limit for ETH transfer
    'gasPrice': gas_price,
    'chainId': 1  # Mainnet Chain ID (use 5 for Goerli testnet, 11155111 for Sepolia)
}

# Sign the transaction
signed_tx = web3.eth.account.sign_transaction(tx, private_key)

# Send the transaction
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

# Print transaction hash
print(f'Transaction sent! Hash: {web3.to_hex(tx_hash)}')
