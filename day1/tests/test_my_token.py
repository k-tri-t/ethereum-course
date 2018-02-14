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

def test_my_token(token_contract, chain):

    account0 = chain.web3.eth.accounts[0]
    account1 = chain.web3.eth.accounts[1]

    assert token_contract.call().getBalanceOf(account0) == 1000000
    assert token_contract.call().getBalanceOf(account1) == 0

    txid = token_contract.transact().transfer(account1, 10)
    chain.wait.for_receipt(txid)

    assert token_contract.call().getBalanceOf(account0) == 999990
    assert token_contract.call().getBalanceOf(account1) == 10

# end of test_my_token.py
