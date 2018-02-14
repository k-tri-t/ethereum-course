import pytest

@pytest.fixture()
def token_contract(chain):
    TokenFactory = chain.provider.get_contract_factory('MyToken')
    deploy_txid = TokenFactory.deploy(args=[
        0,
        "BcH Coin",
        "BcH",
        0,
    ])
    contract_address = chain.wait.for_contract_address(deploy_txid)
    return TokenFactory(address=contract_address)

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

def test_one_time_escrow(token_contract, asset_contract, chain):

    account0 = chain.web3.eth.accounts[0]
    account1 = chain.web3.eth.accounts[1]

    txid = chain.web3.eth.sendTransaction({
        'from': account0,
        'to': account1,
        'value': chain.web3.toWei(1, "ether")
    })
    chain.wait.for_receipt(txid)

    txid = token_contract.transact().transfer(account1, 300)
    chain.wait.for_receipt(txid)

    EscrowFactory = chain.provider.get_contract_factory('OneTimeEscrow')
    txid = EscrowFactory.deploy(args=[
        token_contract.address,
        account1,
        asset_contract.address,
        account0,
        300,
    ])
    contract_address = chain.wait.for_contract_address(txid)
    EscrowFactory.address = contract_address;

    txid = token_contract.transact({
        'from': account1
    }).transfer(contract_address, 300)
    chain.wait.for_receipt(txid)

    txid = asset_contract.transact().transfer(contract_address)
    chain.wait.for_receipt(txid)

    assert token_contract.call().getBalanceOf(account0) == 999700
    assert token_contract.call().getBalanceOf(account1) == 0
    assert token_contract.call().getBalanceOf(contract_address) == 300
    assert asset_contract.call().getOwner().lower() == contract_address.lower()

    txid = EscrowFactory.transact().settle();
    chain.wait.for_receipt(txid)

    assert token_contract.call().getBalanceOf(account0) == 1000000
    assert token_contract.call().getBalanceOf(account1) == 0
    assert token_contract.call().getBalanceOf(contract_address) == 0
    assert asset_contract.call().getOwner().lower() == account1.lower()

# end of test_one_time_escrow.py
