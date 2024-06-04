from flask import Flask, request, jsonify, render_template


text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding' 


app = Flask(__name__)

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encode():
    data = request.json
    message = data.get('message')
    key = data.get('key')
    encrypted_message = encrypt(message, key)
    return jsonify({'result': encrypted_message})

@app.route('/decrypt', methods=['POST'])
def decode():
    data = request.json
    message = data.get('message')
    key = data.get('key')
    decrypted_message = decrypt(message, key)
    return jsonify({'result': decrypted_message})

if __name__ == '__main__':
    app.run(debug=True)