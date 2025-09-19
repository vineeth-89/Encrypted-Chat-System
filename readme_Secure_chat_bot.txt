Task 1: Client-Server Calculator with BODMAS Evaluation
Summary:
- Implemented a client-server model where clients send mathematical expressions to the server.
- The server evaluates expressions using the BODMAS rule and sends results back.
- Expressions are space-separated and support up to 20 operands with +, -, *, /, and % operators.
- The client terminates by sending "END".
- The result is displayed in the format: RESULT: <value>.

Execution Instructions:
1. Run the server first:

   python server.py

2. Run the client:

   python client.py

3. Enter a mathematical expression (space-separated, up to 20 operands) or type `END` to terminate the server.
4. The client will display the result in the format: `RESULT: <value>`

Example:

[INPUT] 1 + 5 * 2 - 1 + 10
[OUTPUT] RESULT: 20

Contribution:
Student1 - Chalasani Vineeth (CS24MTECH11023)
- Implemented the server code of the calculator.
- Implemented the Algorithm.
- Captured packets of communication using Wireshark.

Student2 - Surykant Kasare (CS24MTECH11001)
- Implemented the client code of the calculator.
- Debugged the code for various errors and corrected them.
- Captured packets of communication using Wireshark.

---

Task 2: Peer-to-Peer Chat Application with User Discovery
Summary:
- Implemented a server to manage connected users and their details (IP, port).
- Clients retrieve user lists from the server and initiate direct peer-to-peer (P2P) communication.
- Messages are exchanged between users without server involvement.
- The session continues until one user sends "EOM" to terminate it.
- Messages are displayed as:

  [Send]: <message>
  [Received]: <message>

Execution Instructions:
1. Start the server:

   python chat_server.py

2. Start two clients (User-1 and User-2) in separate terminals:

   python chat_client.py

3. Each user registers with the server and retrieves a list of online users.
4. User-1 selects User-2 from the list and initiates a P2P chat session.
5. Users can exchange messages until `EOM` is sent to terminate the chat.

Example:
-- User 1 (Vineeth)
Enter server IP: 192.168.25.202
Enter Server Port Number: 11001
Enter your username: vineeth
Enter your listening port: 1213

1. List users
2. Act as Listener
3. Connect to User
4. Exit
Enter choice: 2
Waiting for connections on port 1213...
Connection request received from ('192.168.25.202', 42820)
Do you want to accept the connection? (yes/no): yes
Connection established.
[Send]: Hello
[Send]: 
[Received]: Hi,vineeth
[Send]: 
-- User 2 (suryakant)
Enter server IP: 192.168.25.202
Enter Server Port Number: 11001
Enter your username: surykant
Enter your listening port: 11021

1. List users
2. Act as Listener
3. Connect to User
4. Exit
Enter choice: 3
Enter peer IP: 192.168.25.245
Enter peer port: 1213
Connected. Type 'EOM' to exit.
[Send]: 
[Received]: Hello
[Send]: Hi,vineeth
[Send]: EOM
Connection closed.

Contribution:
Student1 - Chalasani Vineeth (CS24MTECH11023)
- Implemented the server code of the P2P Communication.
- Debugged the code for various errors and corrected them.
- Captured packets of communication using Wireshark.

Student2 - Surykant Kasare (CS24MTECH11001)
- Implemented the client code of the P2P Communication.
- Implemented the Algorithm.
- Captured packets of communication using Wireshark.

---

Task 3: Diffie-Hellman Key Exchange for Shared Secret Generation
Summary:
- Implemented Diffie-Hellman key exchange for secure communication.
- Clients read p and g from environment variables.
- Each user generates a private key (a or b) and computes public values.
- Shared secret (KSC) is derived for encryption.
- The shared key is displayed to ensure consistency.
- The AES key is derived by using the shared key as seed.

Execution Instructions:
1. Set environment variables for p and g:

   export P=<large_prime_number>
   export Q=<primitive_root>

2. Run the client programs:

   python dh_client.py

3. Users generate private secrets, exchange computed values, and derive a shared key.
4. The shared key is displayed for verification.

Example Output:
-- User 1 (Vineeth)
Enter server IP: 192.168.25.202
Enter Server Port Number: 11001
Enter your username: suryakant
Enter your listening port: 2411

1. List users
2. Act as Listener
3. Connect to User
4. Exit
Enter choice: 1
Fetching list of connected users...
surykant - 192.168.105.187:131
suryakant - 192.168.25.202:2411

1. List users
2. Act as Listener
3. Connect to User
4. Exit
Enter choice: 2
Waiting for connections on port 2411...
Connection request received from ('192.168.25.202', 51024)
Do you want to accept the connection? (yes/no): yes
Connection established.
[Vineeth] Private Key (a): 1
[Vineeth] Public Key (A): 5
[Vineeth] [SECURITY] Shared Secret Key Computed: 13
[Vineeth] AES Key: 422eadfb2f01db573ec83fad817b6d618fc0410a1b2528e0e8d4a29522759f07
[SECURITY] Shared Secret Key Computed: 13
[Send]: 
 -- User 2 (Suryakant)
Enter server IP: 0.0.0.0
Enter Server Port Number: 11001
Enter your username: Suryakant
Enter your listening port: 1352

1. List users
2. Act as Listener
3. Connect to User
4. Exit
Enter choice: 3
Enter peer IP: 127.0.0.1
Enter peer port: 1342
Connected. Type 'EOM' to exit.
[Suryakant] Private Key (a): 14
[Suryakant] Public Key (A): 13
[Suryakant] [SECURITY] Shared Secret Key Computed: 13
[Suryakant] AES Key: 422eadfb2f01db573ec83fad817b6d618fc0410a1b2528e0e8d4a29522759f07
[SECURITY] Shared Secret Key Computed: 13
[Send]: 
Contribution:
Student1 - Chalasani Vineeth (CS24MTECH11023)
- Implemented the client code for the Diffie-Hellman key exchange.
- Implemented the Algorithm of Diffie-Hellman.
- Captured packets of communication using Wireshark.

Student2 - Surykant Kasare (CS24MTECH11001)
- Implemented the server code of the P2P Communication with Diffie-Hellman key exchange.
- Debugged the code for various errors and corrected them.
- Captured packets of communication using Wireshark.

---

Task 4: AES-Encrypted Secure Chat Using Shared Key
Summary:
- Implemented AES encryption for P2P chat using the shared key from Task 3.
- Outgoing messages are encrypted, and incoming messages are decrypted.
- Encrypted and decrypted messages are displayed as:

  [Cipher]: <ciphertext>
  [Plain]: <plaintext>

Execution Instructions:
1. Ensure Task 3 is completed and both users have the same encryption key.
2. Run the secure chat clients:

   python secure_chat.py

3. Messages are encrypted before sending and decrypted upon receipt.

Example Output:
-- User 1 (Vineeth)
Enter server IP: 0.0.0.0
Enter Server Port Number: 11001
Enter your username: Vineeth
Enter your listening port: 11235

1. List users
2. Act as Listener
3. Connect to User
4. Exit
Enter choice: 2
Waiting for connections on port 11235...
Connection request received from ('192.168.25.202', 52366)
Do you want to accept the connection? (yes/no): yes
Connection established.
[Vineeth] Private Key (a): 3
[Vineeth] Public Key (A): 10
[Vineeth] [SECURITY] Shared Secret Key Computed: 19
[Send]: 
[Received][Cipher]: lcGbWtz1IPCHmLwi1QfZ656fAV7C1JEDdJrlgc92ngetlvVZYg==
[Plain]: Hello
[Send]: bro 
[Cipher]: bsDnGFoWYNj/gyEeTsIlZJMjyiVD1+RfduLHANNP3jNF57g=
[Send]:  
-- User 2 (suryakant)
Enter server IP: 192.168.25.202
Enter Server Port Number: 11001
Enter your username: Suryakant
Enter your listening port: 11342

1. List users
2. Act as Listener
3. Connect to User
4. Exit
Enter choice: 3
Enter peer IP: 192.168.25.202
Enter peer port: 11235
Connected. Type 'EOM' to exit.
[Suryakant] Private Key (a): 5
[Suryakant] Public Key (A): 20
[Suryakant] [SECURITY] Shared Secret Key Computed: 19
[Send]: Hello
[Cipher]: lcGbWtz1IPCHmLwi1QfZ656fAV7C1JEDdJrlgc92ngetlvVZYg==
[Send]: 
[Received][Cipher]: bsDnGFoWYNj/gyEeTsIlZJMjyiVD1+RfduLHANNP3jNF57g=
[Plain]: bro
[Send]: EOM
[Cipher]: CO5Ivr3cIeDsPvUAziGBYXBqNi1j57hWFENJgupY44pqswk=
Connection closed.
 Please Enter any key to get menu

1. List users
2. Act as Listener
3. Connect to User
4. Exit
Enter choice: 
[Received][Cipher]: 
[ERROR] Error receiving message: Nonce cannot be empty
Connection terminated.

Contribution:
Student1 - Chalasani Vineeth (CS24MTECH11023)
- Implemented the server code of the P2P Communication with AES encryption.
- Debugged the code for various errors and corrected them.
- Captured packets of communication using Wireshark.

Student2 - Surykant Kasare (CS24MTECH11001)
- Implemented the client code for the AES encryption.
- Captured packets of communication using Wireshark.

---

Acknowledgments:
- Python's `socket`, `cryptography`, and `pycryptodome` libraries were used.
- Inspiration taken from online cryptography and networking tutorials.

Notes:
- Ensure required dependencies are installed using:

  pip install pycryptodome

---

ANTI-PLAGIARISM STATEMENT

We certify that this assignment/report is our own work, based on our personal study and/or research and that we have acknowledged all material and sources used in its preparation, whether books, articles, packages, datasets, reports, lecture notes, or any other document, electronic or personal communication. We also certify that this assignment/report has not previously been submitted for assessment/project in any other course lab, except where specific permission has been granted from all course instructors involved, or at any other time in this course, and that we have not copied in part or whole or otherwise plagiarized the work of other students and/or persons.

We pledge to uphold the principles of honesty and responsibility at CSE@IITH. In addition, we understand our responsibility to report honor violations by other students if we become aware of it.

Names:

    Chalasani Vineeth (CS24MTECH11023)
    Surykant Kasare (CS24MTECH11001)

Date: 4/2/2025

Signature:
CV (Chalasani Vineeth)
SK (Surykant Kasare)
Task 1: Client-Server Calculator
Summary:
- Implemented a client-server model where clients send mathematical expressions to the server.
- The server evaluates expressions using the BODMAS rule and sends results back.
- Expressions are space-separated and support up to 20 operands with +, -, *, /, and % operators.
- The client terminates by sending "END".
- The result is displayed in the format: RESULT: <value>.

Execution Instructions:
1. Run the server first:

   python server.py

2. Run the client:

   python client.py

3. Enter a mathematical expression (space-separated, up to 20 operands) or type `END` to terminate the server.
4. The client will display the result in the format: `RESULT: <value>`

Example:

[INPUT] 1 + 5 * 2 - 1 + 10
[OUTPUT] RESULT: 20

Contribution:
Student1 - Chalasani Vineeth (CS24MTECH11023)
- Implemented the server code of the calculator.
- Implemented the Algorithm.
- Captured packets of communication using Wireshark.

Student2 - Surykant Kasare (CS24MTECH11001)
- Implemented the client code of the calculator.
- Debugged the code for various errors and corrected them.
- Captured packets of communication using Wireshark.

---

Task 2: Peer-to-Peer Chat System
Summary:
- Implemented a server to manage connected users and their details (IP, port).
- Clients retrieve user lists from the server and initiate direct peer-to-peer (P2P) communication.
- Messages are exchanged between users without server involvement.
- The session continues until one user sends "EOM" to terminate it.
- Messages are displayed as:

  [Send]: <message>
  [Received]: <message>

Execution Instructions:
1. Start the server:

   python chat_server.py

2. Start two clients (User-1 and User-2) in separate terminals:

   python chat_client.py

3. Each user registers with the server and retrieves a list of online users.
4. User-1 selects User-2 from the list and initiates a P2P chat session.
5. Users can exchange messages until `EOM` is sent to terminate the chat.

Example:

  [Send]: Hello User-2
  [Received]: Hi User-1

Contribution:
Student1 - Chalasani Vineeth (CS24MTECH11023)
- Implemented the server code of the P2P Communication.
- Debugged the code for various errors and corrected them.
- Captured packets of communication using Wireshark.

Student2 - Surykant Kasare (CS24MTECH11001)
- Implemented the client code of the P2P Communication.
- Implemented the Algorithm.
- Captured packets of communication using Wireshark.

---

Task 3: Diffie-Hellman Key Exchange
Summary:
- Implemented Diffie-Hellman key exchange for secure communication.
- Clients read p and g from environment variables.
- Each user generates a private key (a or b) and computes public values.
- Shared secret (KSC) is derived for encryption.
- The shared key is displayed to ensure consistency.
- The AES key is derived by using the shared key as seed.

Execution Instructions:
1. Set environment variables for p and g:

   export P=<large_prime_number>
   export Q=<primitive_root>

2. Run the client programs:

   python dh_client.py

3. Users generate private secrets, exchange computed values, and derive a shared key.
4. The shared key is displayed for verification.

Example Output:

  [Send]: 124566
  [Received]: 987654
  [Key]: AES Encryption Key: abc123...

Contribution:
Student1 - Chalasani Vineeth (CS24MTECH11023)
- Implemented the client code for the Diffie-Hellman key exchange.
- Implemented the Algorithm of Diffie-Hellman.
- Captured packets of communication using Wireshark.

Student2 - Surykant Kasare (CS24MTECH11001)
- Implemented the server code of the P2P Communication with Diffie-Hellman key exchange.
- Debugged the code for various errors and corrected them.
- Captured packets of communication using Wireshark.

---

Task 4: Secure Encrypted Chat using AES
Summary:
- Implemented AES encryption for P2P chat using the shared key from Task 3.
- Outgoing messages are encrypted, and incoming messages are decrypted.
- Encrypted and decrypted messages are displayed as:

  [Cipher]: <ciphertext>
  [Plain]: <plaintext>

Execution Instructions:
1. Ensure Task 3 is completed and both users have the same encryption key.
2. Run the secure chat clients:

   python secure_chat.py

3. Messages are encrypted before sending and decrypted upon receipt.

Example Output:

  [Cipher]: U2FsdGVkX19...
  [Plain]: Hello, how are you?

Contribution:
Student1 - Chalasani Vineeth (CS24MTECH11023)
- Implemented the server code of the P2P Communication with AES encryption.
- Debugged the code for various errors and corrected them.
- Captured packets of communication using Wireshark.

Student2 - Surykant Kasare (CS24MTECH11001)
- Implemented the client code for the AES encryption.
- Captured packets of communication using Wireshark.

---

Acknowledgments:
- Python's `socket`, `cryptography`, and `pycryptodome` libraries were used.
- Inspiration taken from online cryptography and networking tutorials.

Notes:
- Ensure required dependencies are installed using:

  pip install pycryptodome

---

ANTI-PLAGIARISM STATEMENT

We certify that this assignment/report is our own work, based on our personal study and/or research and that we have acknowledged all material and sources used in its preparation, whether books, articles, packages, datasets, reports, lecture notes, or any other document, electronic or personal communication. We also certify that this assignment/report has not previously been submitted for assessment/project in any other course lab, except where specific permission has been granted from all course instructors involved, or at any other time in this course, and that we have not copied in part or whole or otherwise plagiarized the work of other students and/or persons.We pledge to uphold the principles of honesty and responsibility at CSE@IITH. In addition, we understand our responsibility to report honor violations by other students if we become aware of it.

Names:

    Chalasani Vineeth (CS24MTECH11023)
    Surykant Kasare (CS24MTECH11001)

Date: 4/2/2025

Signature:
CV (Chalasani Vineeth)
SK (Surykant Kasare)
