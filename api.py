from flask import Flask, request, jsonify
from node import Node

app = Flask(__name__)
node = Node()

@app.route('/transaction', methods=['POST'])
def create_transaction():
    data = request.get_json()
    receiver = data['receiver']
    amount = data['amount']
    node.create_transaction(receiver, amount)
    return jsonify({'message': 'Transaction created'}), 201

@app.route('/mine', methods=['GET'])
def mine_block():
    node.mine_pending_transactions()
    return jsonify({'message': 'Block mined'}), 200

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = [block.__dict__ for block in node.blockchain.chain]
    return jsonify(chain_data), 200

@app.route('/validate', methods=['GET'])
def validate_chain():
    is_valid = node.is_chain_valid()
    return jsonify({'is_valid': is_valid}), 200

if __name__ == '__main__':
    app.run(port=5001)
