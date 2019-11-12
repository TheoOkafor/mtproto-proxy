from quart import Quart, request, jsonify
from quart_openapi import Pint, Resource

from telethon import TelegramClient
import logging
logging.basicConfig(
  format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
  level=logging.WARNING
)

app = Pint(__name__, title='mtproto-proxy')

api_id = 1150044
api_hash = "07a4a593788b5d222f4f3139dca2e0b9"

async def main(client, phone_number):
  print('here we go')
  response = await client.send_code_request(phone_number, True)

  print(response.stringify())

@app.route('/auth.sendCode')
class SendCode(Resource):
  async def post(self):
    data = await request.get_json()
    phone_number = data['phone_number']
    print(phone_number)
    client = TelegramClient('anon', api_id, api_hash)
    await client.connect()
    sent = await client.send_code_request(phone_number)
    response = {
      'type': 'SentCodeTypeSms',
      'phone_code_hash': sent.phone_code_hash
    }
    print(sent)
    # print('about to go')
    # async with client:
    #   client.loop.run_until_complete(main(client, phone_number))
    return jsonify(response)

app.run()
