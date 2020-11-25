from flask import Flask, request
import json

from bot import Bot, Samplebot,Wherebot

PAGE_ACCESS_TOKEN='EAAFagrk2FVkBAMAQYExYF63MBmrnpffoyIDczNP7adK3FfqlZBOzyJaoLky0ZAFyW4KiiVTecEn1hIyB5LfbZCuKcXlbK2SbMZCZB1U7Y1AqY6ZCTFPN4qVFUrHqXt79HjsZCj0YVgLmXJiwcdVQaNoTzWUs24m0RPr6wIfWAWZAfa14ZCN072i2U'

STOPBOT=['About the company','Others']


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
        bot=Samplebot(PAGE_ACCESS_TOKEN)
        finishbot=Bot(PAGE_ACCESS_TOKEN)
        wherebot=Wherebot(PAGE_ACCESS_TOKEN)
        for message in messaging_events:
            user_id = message['sender']['id']
            text_input = message['message'].get('text')
            print('Message from user ID {} - {}'.format(user_id, text_input))
            if text_input in STOPBOT:
                response_text="I see. Our human operator will reply to you soon. Thank you for your patience. Please write details about yout inquiry so that we can handle efficiently."
                finishbot.send_text_message(user_id,response_text)

            elif text_input =="Look for jobs":
                wherebot.send_text_message(user_id)
            elif text_input == "Yes":
                    response_text="I see. Our human operator will reply to you soon. Thank you for your patience. Please write details about yout inquiry so that we can handle efficiently."
                    finishbot.send_text_message(user_id,response_text)
            elif text_input == "No":
                    response_text="I am very sorry to say that we are currently supporting only those who live in Japan."
                    finishbot.send_text_message(user_id,response_text)






            else:
                bot.send_text_message(user_id)




        return '200'

if __name__ == '__main__':
    app.run(debug=True)
