# Advanced Encrypter - Decrypter

![alt text](<templates/Screenshot 2024-06-04 214646.png>)

**Welcome to Advanced Encrypter!**

This Flask application provides a user interface for Vigenere cipher encryption and decryption.

**Features:**

* Encrypts and decrypts messages using the Vigenere cipher.
* User-friendly web interface for easy interaction.
* Supports both encryption and decryption functionalities.

**Getting Started:**

1. **Prerequisites:**
    * Python 3 ([https://www.python.org/downloads/](https://www.python.org/downloads/))
    * pip (usually comes bundled with Python)

2. **Installation:**
    * Clone this repository or download the code files.
    * Install required dependencies:
        ```bash
        pip install Flask
        ```

3. **Running the Application:**
    * Open a terminal in the project directory.
    * Run the following command:
        ```bash
        python app.py
        ```
    * This will start the Flask development server.

4. **Access the Application:**
    * Open your web browser and navigate to http://127.0.0.1:5000/ (replace with your machine's IP if accessing remotely).
    * You should see a web interface for entering messages and keys for encryption/decryption.

**How to Use:**

* Enter your message in the text box.
* Provide a secret key for encryption/decryption.
* Click the "Encrypt" button to encrypt your message.
* Click the "Decrypt" button to decrypt an encrypted message (with the same key).
* The encrypted/decrypted message will be displayed below the respective button.

**Technical Details:**

* The application utilizes Flask, a lightweight web framework for Python.
* Vigenere cipher implementation is included for encryption and decryption functionalities.
* The web interface is built using HTML templates rendered by Flask.

**Further Development:**

* Implement error handling for invalid user input.
* Integrate support for additional encryption algorithms.
* Enhance the user interface for better user experience.

**License:**

This project is distributed under the MIT License (see LICENSE file for details).

**Author:**

* Aakash/C0dewordSky 

**Feel free to contribute to this project by creating pull requests!**
