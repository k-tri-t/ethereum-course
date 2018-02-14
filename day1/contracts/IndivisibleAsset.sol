pragma solidity ^0.4.8;

contract IndivisibleAsset { 

    string public _name;
    string public _symbol;
    uint256 public _quantity;
    address public _owner;

    event Transfer(address indexed from, address indexed to);
    
    function IndivisibleAsset(string name, string symbol, uint256 quantity) {

        _name = name;
        _symbol = symbol;
        _quantity = quantity;

        _owner = msg.sender;
    }

    function getOwner() returns (address owner) {
        return (_owner);
    }

    function transfer(address to) {

        if (_owner != msg.sender) {
            throw;
        }
        
        _owner = to;
        
        Transfer(msg.sender, to);
    }
}

/* end of IndivisibleAsset.sol */
