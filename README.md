# AmirCoin

AmirCoin is a simple, API-operated cryptocurrency written in Python. It utilizes a blockchain, cryptography, wallet management, and a simple API for interaction.  It is not based on pre-existing blockchains, such as Ethereum, so it's transactions are not tracked by brokerage firms.  No known compute ensures 100% uptime.  

## About AmirCoin

• **Name**: AmirCoin\
• **Symbol**: AMC\
• **Total Supply**: 1,000,000 AMC\
• **Consensus Algorithm**: Proof of Work\
• **Hashing Algorithm**: SHA-256\
• **Block Time**: 10s\
• **Difficulty Adjustment**: Every block

## Features

• **Blockchain**: Implements a basic blockchain with blocks linked by hashes.\
• **Mining**: PoW algorithm for mining new blocks and securing the network.\
• **Wallet**: Provides key generation, transaction signing, and verification.\
• **Networking**: Simple networking for node communication.\
• **API**: Flask-based API for interacting with the node.

## Getting Started

Follow these one-time directions:

1. Clone the AmirCoin repository to your local machine.\    Open command-line interface, enter `git clone https://github.com/amirrsyed/amircoin.git`.
2. Install the required dependencies (`rsa`, `flask`).
3. Run the `api.py` file to start the node API.
4. Use HTTP requests to interact with the API and manage transactions.

## Example API calls/functionality

Create a transaction:
`curl -X POST http://localhost:5001/transaction -H "Content-Type: application/json" -d '{"receiver": "recipient_address", "amount": 10}`\
Mine a block:
`curl http://localhost:5001/mine`\
Check the blockchain:
`curl http://localhost:5001/chain`

## Security
• AmirCoin uses basic SHA-256 hashing for block creation and digital signatures for transaction verification.\
• Private keys should be securely stored and managed to prevent unauthorized access.\
• V2.0, not yet released, will have a double spending solution.

## Disclaimer
AmirCoin is for private transactions.  Value is arbitrated on a peer-to-peer basis, and no central authority tracks AmirCoin price history.  
