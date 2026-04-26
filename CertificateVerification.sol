// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CertificateVerification {

    struct Certificate {
        string studentName;
        string course;
        string university;
        string certificateHash;
        bool exists;
    }

    mapping(string => Certificate) certificates;

    function addCertificate(
        string memory _id,
        string memory _studentName,
        string memory _course,
        string memory _university,
        string memory _hash
    ) public {

        certificates[_id] = Certificate(
            _studentName,
            _course,
            _university,
            _hash,
            true
        );
    }

    function verifyCertificate(
        string memory _id
    ) public view returns(
        string memory,
        string memory,
        string memory,
        string memory,
        bool
    ){

        Certificate memory cert =
            certificates[_id];

        return(
            cert.studentName,
            cert.course,
            cert.university,
            cert.certificateHash,
            cert.exists
        );
    }
}
