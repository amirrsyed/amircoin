# AmirCoin

AmirCoin is a simple cryptocurrency implementation in Python, designed for educational and experimental purposes. It includes basic blockchain functionality, cryptographic security, wallet management, and a simple API for interaction.

## About AmirCoin

• **Name**: AmirCoin
• **Ticker Symbol**: AMC
• **Total Supply**: 1,000,000 AMC
• **Consensus Algorithm**: Proof of Work (PoW)
• **Hashing Algorithm**: SHA-256
• **Block Time**: 10 seconds
• **Difficulty Adjustment**: Every block

## Features

• **Blockchain**: Implements a basic blockchain with blocks linked by hashes.
• **Mining**: PoW algorithm for mining new blocks and securing the network.
• **Wallet**: Provides key generation, transaction signing, and verification.
• **Networking**: Simple networking for node communication.
• **API**: Flask-based API for interacting with the node.

## Getting Started

To start using AmirCoin, follow these steps:

1. Clone the AmirCoin repository to your local machine.
2. Install the required dependencies (`rsa`, `flask`).
3. Run the `api.py` file to start the node API.
4. Use HTTP requests to interact with the API and manage transactions.

## Example Usage

Create a transaction:
`curl -X POST http://localhost:5001/transaction -H "Content-Type: application/json" -d '{"receiver": "recipient_address", "amount": 10}`
Mine a block:
`curl http://localhost:5001/mine`
Check the blockchain:
`curl http://localhost:5001/chain`

## Security Considerations
• AmirCoin uses basic SHA-256 hashing for block creation and digital signatures for transaction verification.
• Private keys should be securely stored and managed to prevent unauthorized access.
• V2.0, not yet released, will have a double spending solution.  

## Disclaimer
AmirCoin is for private transactions.  Value is arbitrated on a peer-to-peer basis, and no central authority tracks AmirCoin price history.  
