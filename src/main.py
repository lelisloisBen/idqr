from flask import Flask, request, jsonify, send_file,send_from_directory
from flask_cors import CORS
from utils import APIException
import os
import pyqrcode
import png
from pyqrcode import QRCode

app = Flask(__name__)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/simple_id')
def test():
    # s = "https://media.wtsp.com/assets/WTSP/images/44cc5ccd-21ee-472f-b1db-37503c9a7a9d/44cc5ccd-21ee-472f-b1db-37503c9a7a9d_1920x1080.jpg" #String which represents the QR code
    s = "https://qrcodeidbackend.herokuapp.com/info"
    url = pyqrcode.create(s) # Generate QR code
    url.png('../qrcodes/myqr.png', scale = 6) #Heroku path
    # url.png('qrcodes/myqr.png', scale = 6)
    filename = '../qrcodes/myqr.png'
    return send_file(filename, mimetype='image/png')

@app.route('/info')
def info():
    return "<div><ul>\
            <li><b>First Name: </b>Robert</li>\
            <li><b>Last Name: </b>Bob</li><li>\
            <li><b>Birth date: </b>12/02/1965</li>\
            <li><b>Age: </b>68 years old</li><li>\
            <li><b>Address: </b>1230 Collins Avenue, Miami Beach 33139 Florida</li>\
            <li><b>SSN: </b>123-45-6789</li><li>\
            </ul></div>"

@app.route('/')
def hello_world():
    return "<div style='text-align: center'><h1>Backend running...</h1><img src='https://www.incimages.com/uploaded_files/image/1920x1080/getty_178851317_308926.jpg' width='80%' /></div>"


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)