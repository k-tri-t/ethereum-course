import json

f = open('populus.json', 'r')
jPop = json.load(f)
f.close()

jBcHChain = {
    "chain": {
        "class": "populus.chain.ExternalChain"
    },
    "contracts": {
        "backends": {
            "JSONFile": {
                "$ref": "contracts.backends.JSONFile"
            },
            "Memory": {
                "$ref": "contracts.backends.Memory"
            },
            "ProjectContracts": {
                "$ref": "contracts.backends.ProjectContracts"
            },
            "TestContracts": {
                "$ref": "contracts.backends.TestContracts"
            }
        }
    },
    "web3": {
        "$ref": "web3.GethIPC"
    }
}
    
jChains = jPop['chains']
jChains['bch'] = jBcHChain

f = open('populus.json', 'w')
json.dump(jPop, f, indent=2)
f.close()

jGenesis = {
    "config": {
        "chainId": 16,
        "homesteadBlock": 0,
        "eip155Block": 0,
        "eip158Block": 0
    },
    "difficulty": "0x200",
    "gasLimit": "2100000",
    "alloc": {
    }
}

f = open('genesis.json', 'w')
json.dump(jGenesis, f, indent=2)
f.close()

# end of init.py
