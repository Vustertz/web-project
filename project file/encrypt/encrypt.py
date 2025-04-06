from flask import Flask, request, render_template
import base64
import urllib.parse

app = Flask(__name__)

# Encode và Decode Base64
def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def base64_decode(encoded_text):
    return base64.b64decode(encoded_text).decode()

# Encode và Decode URL
def url_encode(text):
    return urllib.parse.quote(text)

def url_decode(encoded_text):
    return urllib.parse.unquote(encoded_text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    text = request.form['text']
    encoding_type = request.form['encoding_type']

    if encoding_type == 'base64':
        encoded_text = base64_encode(text)
        return render_template('index.html', original=text, encoded=encoded_text, encoding_type='Base64')

    elif encoding_type == 'url':
        encoded_text = url_encode(text)
        return render_template('index.html', original=text, encoded=encoded_text, encoding_type='URL')

    return "Encoding type không hợp lệ!"

@app.route('/decode', methods=['POST'])
def decode():
    text = request.form['text']
    encoding_type = request.form['encoding_type']

    if encoding_type == 'base64':
        decoded_text = base64_decode(text)
        return render_template('index.html', original=text, decoded=decoded_text, encoding_type='Base64')

    elif encoding_type == 'url':
        decoded_text = url_decode(text)
        return render_template('index.html', original=text, decoded=decoded_text, encoding_type='URL')

    return "Decoding type không hợp lệ!"

if __name__ == '__main__':
    app.run(debug=True)
