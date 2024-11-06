//SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

contract Bank{

    uint256 balance = 0;
    address internal accOwner;

    constructor(){
        accOwner = msg.sender;
    }

    function Deposit() public payable {
        require(accOwner == msg.sender, "You arent the owner");
        require(msg.value > 0, "Deposit more than 0");
        balance += msg.value;
    }

    function Withdraw() public payable {
        require(accOwner == msg.sender, "You arent the owner");
        require(msg.value > 0, "Withdraw more than 0");
        balance -= msg.value;
    }

    function Balance() public view returns(uint256){
        require(accOwner == msg.sender, "You arent the owner");
        return balance;
    }



}

