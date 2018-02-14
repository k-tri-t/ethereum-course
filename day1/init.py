import json

f = open('project.json', 'r')
jPop = json.load(f)
f.close()

jBcHChain = {
    "chain": {
        "class": "populus.chain.ExternalChain"
    },
    "contracts": {
        "backends": {
            "JSONFile": {
                "class": "populus.contracts.backends.filesystem.JSONFileBackend",
                "priority": 10,
                "settings": {
                    "file_path": "./registrar.json"
                }
            },
            "Memory": {
                "class": "populus.contracts.backends.memory.MemoryBackend",
                "priority": 50
            },
            "ProjectContracts": {
                "class": "populus.contracts.backends.project.ProjectContractsBackend",
                "priority": 20
            },
            "TestContracts": {
                "class": "populus.contracts.backends.testing.TestContractsBackend",
                "priority": 40
            }
        }
    },
    "web3": {
        "provider": {
            "class": "web3.providers.ipc.IPCProvider"
        }
    }
}
    
jChains = dict()
jChains['bch'] = jBcHChain
jPop['chains'] = jChains

f = open('project.json', 'w')
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
