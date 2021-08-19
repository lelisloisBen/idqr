from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException
import os

app = Flask(__name__)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def hello_world():
    return "<div style='text-align: center; background-color: black'><h1>Backend running...</h1><br/><h3>Welcome back samir</h3><img src='https://www.incimages.com/uploaded_files/image/1920x1080/getty_178851317_308926.jpg' width='80%' /></div>"


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)