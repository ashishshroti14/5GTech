To run and test the code, follow these steps:



1. **Run the Server**:
   - Open a terminal or command prompt.
   - Navigate to your project directory.
   - Run the server with the following command:
     ```sh
     python tcp_server.py
     ```

2. **Test the Server Using the Stub**:
   - Open another terminal or command prompt.
   - Navigate to your project directory.
   - Run the client stub with the following command:
     ```sh
     python tcp_client_stub.py
     ```
   - You should see output from the server indicating a connection was made and a response sent back.

3. **Run the Unit Tests**:
   - In your terminal, navigate to your project directory.
   - Run the tests with the following command:
     ```sh
     python -m unittest test_protocol_handler.py
     ```

This should output the results of the unit tests, confirming that the protocol handler and device manager work as expected.
