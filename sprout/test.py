import json
from algosdk.v2client import algod
from algosdk import account, mnemonic
from algosdk.future.transaction import AssetConfigTxn, AssetTransferTxn, AssetFreezeTxn


mnemonic1 = "quality earth near gun survey sentence swing pair also original insect stomach august exit student random rubber next cluster resemble impulse wheat under above meadow"
mnemonic2 = "episode six subway wall symbol giggle shock muffin cherry domain trophy truck object despair bring few hunt loud sense enable engine access worth absent glimpse"

# For ease of reference, add account public and private keys to
# an accounts dict.
accounts = {}
counter = 1
for m in [mnemonic1, mnemonic2]:
    accounts[counter] = {}
    accounts[counter]['pk'] = mnemonic.to_public_key(m)
    accounts[counter]['sk'] = mnemonic.to_private_key(m)
    counter += 1

# Specify your node address and token. This must be updated.

algod_address = "http://localhost:8080"
algod_token = "36690027c08289d0c63ab134d78393f8f3a2d0f0ee74a7c4703389d7157dc5e2"

# Initialize an algod client
algod_client = algod.AlgodClient(algod_token=algod_token, algod_address=algod_address)
