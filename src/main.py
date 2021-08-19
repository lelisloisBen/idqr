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

@app.route('/test')
def test():
    # String which represents the QR code
    s = "www.geeksforgeeks.org"
    
    # Generate QR code
    url = pyqrcode.create(s)
    
    # Create and save the svg file naming "myqr.svg"
    # url.svg("myqr.svg", scale = 8)
    
    # Create and save the png file naming "myqr.png"
    url.png('myqr.png', scale = 6)

    # return str(url)
    #  filename = 'sid.png'
    # return send_file(url, mimetype='image/png')

    return send_from_directory(
    '/Users/samirbenzada/Desktop/idqr/',
    'myqr.png',
    as_attachment=True,
    attachment_filename='myqr.png',
    mimetype='image/png'
 )

@app.route('/')
def hello_world():
    return "<div style='text-align: center'><h1>Backend running...</h1><img src='https://www.incimages.com/uploaded_files/image/1920x1080/getty_178851317_308926.jpg' width='80%' /></div>"


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)