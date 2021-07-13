from flask import Flask, request
from flask_cors import CORS, cross_origin
import jwt
import json
import datetime

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'


#Start of endpoints

@app.route("/login", methods=["POST"])
@cross_origin()
def login_user():
  data = request.get_json()
  print('Recieved: ' + str(data))
  d = { 'email': 'test@gmail.com', 'password': 'woohoo' }
  token = encode_auth_token(d)
  print('made token: ')
  print(token)
  user = { 'user': { 'email': 'test@gmail.com'} , 'token': token }
  return json.dumps(user)

@app.route("/registration", methods=["POST"])
@cross_origin()
def register_user():
  data = request.get_json()
  print('Recieved: ' + str(data))
  d = { 'email': 'test@gmail.com', 'password': 'woohoo' }
  token = encode_auth_token(d)
  print('made token: ')
  print(token)
  user = { 'user': { 'email': 'test@gmail.com'}, 'token': token }
  return json.dumps(user)

@app.route("/verify/", methods=["GET"])
@cross_origin()
def verify_token():
  token = request.headers.get('Authorization').replace("Token ", "")
  if (token != "undefined"):
    user = decode_auth_token(token)
    return json.dumps({'user': user, 'token': token})


def encode_auth_token(user_info):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user_info
        }
        return jwt.encode(
            payload,
            'CescMUOaFicus7Xfd1dtUGEbHm5zcdn4',
            algorithm='HS256'
        )
    except Exception as e:
        return e

def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """

    print('Trying to decode token: ' + auth_token)
    try:
        payload = jwt.decode(auth_token, 'CescMUOaFicus7Xfd1dtUGEbHm5zcdn4', algorithms=["HS256"])
        print(payload)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

if __name__ == '__main__':
   app.run(debug = True)