from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import datetime
from qrcode import createQR

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

#Start of endpoints

@app.route('/generate', methods=["POST"])
@cross_origin()
def get_image():
  data = request.get_json()
  image = createQR('https://tippy.to/u/' + str(data['owner_id']), 
    data['qr_style'], data['qr_colour'], data['qr_inner_eye_style'],
    data['qr_inner_eye_colour'], data['qr_outer_eye_style'],
    data['qr_outer_eye_colour'], data['bg_colour'])
  return image

if __name__ == '__main__':
   app.run(debug = True)