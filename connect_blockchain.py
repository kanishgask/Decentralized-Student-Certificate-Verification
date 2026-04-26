from web3 import Web3

ganache_url="http://127.0.0.1:7545"

web3=Web3(
Web3.HTTPProvider(ganache_url)
)

contract_address="PASTE_DEPLOYED_CONTRACT"

abi=[
{
"inputs":[
{"internalType":"string","name":"_id","type":"string"},
{"internalType":"string","name":"_studentName","type":"string"},
{"internalType":"string","name":"_course","type":"string"},
{"internalType":"string","name":"_university","type":"string"},
{"internalType":"string","name":"_hash","type":"string"}
],
"name":"addCertificate",
"outputs":[],
"stateMutability":"nonpayable",
"type":"function"
},
{
"inputs":[
{"internalType":"string","name":"_id","type":"string"}
],
"name":"verifyCertificate",
"outputs":[
{"type":"string"},
{"type":"string"},
{"type":"string"},
{"type":"string"},
{"type":"bool"}
],
"stateMutability":"view",
"type":"function"
}
]

contract=web3.eth.contract(
address=contract_address,
abi=abi
)

account=web3.eth.accounts[0]

def add_certificate(
id,
name,
course,
university,
hashv
):

 tx=contract.functions.addCertificate(
 id,
 name,
 course,
 university,
 hashv
 ).transact(
 {'from':account}
 )

 web3.eth.wait_for_transaction_receipt(tx)


def verify_certificate(id):

 return contract.functions.verifyCertificate(
 id
 ).call()
