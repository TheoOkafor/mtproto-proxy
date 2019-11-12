from flask import request
from flask_restful import Resource, Api
from server.index import app
from pyrogram import Client

api = Api(app)

class SendCode(Resource):
  def post(self):
    data = request.get_json()
    return Client.send_code(data['phone_number'])

