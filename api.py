from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import datetime
from qrcode import createQR

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

#Start of endpoints

@app.route('/get_image')
@cross_origin()
def get_image():
  image = createQR()
  return image

if __name__ == '__main__':
   app.run(debug = True)