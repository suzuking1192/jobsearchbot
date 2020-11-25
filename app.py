from flask import Flask, request
import json

from bot import Bot

PAGE_ACCESS_TOKEN='EAAFagrk2FVkBAMAQYExYF63MBmrnpffoyIDczNP7adK3FfqlZBOzyJaoLky0ZAFyW4KiiVTecEn1hIyB5LfbZCuKcXlbK2SbMZCZB1U7Y1AqY6ZCTFPN4qVFUrHqXt79HjsZCj0YVgLmXJiwcdVQaNoTzWUs24m0RPr6wIfWAWZAfa14ZCN072i2U'
Greetings=['hi','hello','howdy','how are you?']


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == 'random':
            return str(challenge)
        return '400'

    else:
        print (request.data)
        data = json.loads(request.data)
        messaging_events = data['entry'][0]['messaging']
        bot=Bot(PAGE_ACCESS_TOKEN)
        for message in messaging_events:
            user_id = message['sender']['id']
            text_input = message['message'].get('text')
            response_test="I am still learning"
            if text_input in Greetings:
                response_test='Hello, Welcome to my first bot!'
            print('Message from user ID {} - {}'.format(user_id, text_input))
            bot.send_text_message(user_id,response_test)


        return '200'

if __name__ == '__main__':
    app.run(debug=True)
