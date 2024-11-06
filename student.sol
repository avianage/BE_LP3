//SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

contract StudentData{

    struct Student{
        string name;
        uint rollno;
        
    }

    Student[] public studentarr;

    function add_student(string memory name, uint rollno) public {
        for (uint i = 0; i < studentarr.length; i++){
            if (studentarr[i].rollno == rollno){
                revert("Student with number exist");
            }
        }
        studentarr.push(Student(name, rollno));
    }

    function get_student() public view returns(uint){
        return studentarr.length;
    }

    function display_student() public view returns(Student[] memory){
        return studentarr;
    }

    function getStudentbyIndex(uint idx) public view returns(Student memory){
        require(idx < studentarr.length, "index out of bound");

        return studentarr[idx]; 
    }

    //fallback

    fallback() external payable { 
        revert("This contract doesnt accept ether");
    }
    
    receive() external payable { 
        revert("This contract doesnt accept ether");
    }
}