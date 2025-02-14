# Ethereum Transfer Script

This script allows you to transfer Ethereum (ETH) on the ERC-20 network from one wallet to another using **Web3.py**.

## Prerequisites

1. Install Python (if not already installed):
   - Download and install Python from [python.org](https://www.python.org/)

2. Install the required Python package:
   ```sh
   pip install web3
   ```

3. Get access to an Ethereum node provider like **Infura** or **Alchemy**:
   - Sign up at [Infura](https://infura.io/) and create a new project.
   - Get your **Infura Project ID**.

4. Gather your wallet details:
   - Sender Address (Your wallet address)
   - Private Key (Do **not** share or expose this publicly)
   - Receiver Address (The recipient's wallet address)

## Usage

1. Open the script file and replace the placeholders with your actual details:
   ```python
   infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
   sender_address = "0xYourSenderAddress"
   private_key = "YourPrivateKey"
   receiver_address = "0xReceiverAddress"
   amount = 0.01  # ETH to send
   ```

2. Run the script:
   ```sh
   python transfer_eth.py
   ```

3. If successful, the script will output the transaction hash:
   ```sh
   Transaction sent! Hash: 0x123456789...
   ```

## Notes

- **Ensure you have enough ETH** in your wallet for both the transfer and gas fees.
- This script sends **ETH**, not ERC-20 tokens. If you need an ERC-20 token transfer script, modifications are required.
- Always keep your **private key secure** and never expose it publicly.
- You can test this script using Ethereum **testnets** (Goerli, Sepolia) before running it on Mainnet.

## License
This project is licensed under the MIT License.

## Disclaimer
Use this script at your own risk. The author is not responsible for any lost funds due to incorrect usage or security breaches.
