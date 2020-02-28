# AccessLevelControl
A controlled, tired system that has plaintext usernames, pseudo-random salt, hashed/salted passwords, and access levels stored in a csv (or txt) file.

- Encrypts the password the user enters using the SHA-512 algorithm
- Has input validation to require the password length to be a minimum of 8 characters and a maximum of 25 characters as well as one digit. If the user enters a password length outside those limits, return an error message and prompt the user to re-enter the password. 
- Has input validation to require the user to have at least one number and at least one letter in the password
- Has error handling.

SHA-512 stands for Secure Hash Algorithm and is a set of cryptographic hash functions designed by the NSA. It is a novel hash function that is computed with 64-bit words. There are 80 rounds of encryption. 

 Attched is a csv file with a test user. The username is 'user1' and the password is 'Password1' and has an access level of 1.
