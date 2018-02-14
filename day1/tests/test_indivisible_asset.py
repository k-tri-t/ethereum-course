import pytest

@pytest.fixture()
def asset_contract(chain):
    AssetFactory = chain.provider.get_contract_factory('IndivisibleAsset')
    deploy_txid = AssetFactory.deploy(args=[
        "5322 Endo, Fujisawa",
        "m^2",
        300,
    ])
    contract_address = chain.wait.for_contract_address(deploy_txid)
    return AssetFactory(address=contract_address)

def test_indivisible_assset(asset_contract, chain):

    account0 = chain.web3.eth.accounts[0]
    account1 = chain.web3.eth.accounts[1]

    assert asset_contract.call().getOwner().lower() == account0.lower()

    txid = asset_contract.transact().transfer(account1)
    chain.wait.for_receipt(txid)

    assert asset_contract.call().getOwner().lower() == account1.lower()

# end of test_indivisible_asset.py
