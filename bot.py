import requests
import json

FACEBOOK_GRAPH_URL='https://graph.facebook.com/v9.0/me/'

class Bot(object):
    def __init__(self, access_token, api_url=FACEBOOK_GRAPH_URL):
        self.access_token= access_token
        self.api_url=api_url

    def send_text_message(self,psid,message,messaging_type='RESPONSE'):
        headers={
            'Content-Type':'application/json'
        }

        data={
            'messaging_type':messaging_type,
            'recipient':{'id':psid},
            'message':{'text':message}
        }

        params = {'access_token':self.access_token}
        self.api_url=self.api_url + 'messages'
        response= requests.post(self.api_url,headers=headers,params=params,data=json.dumps(data))

        print(response.content)


bot = Bot('EAAFagrk2FVkBAMAQYExYF63MBmrnpffoyIDczNP7adK3FfqlZBOzyJaoLky0ZAFyW4KiiVTecEn1hIyB5LfbZCuKcXlbK2SbMZCZB1U7Y1AqY6ZCTFPN4qVFUrHqXt79HjsZCj0YVgLmXJiwcdVQaNoTzWUs24m0RPr6wIfWAWZAfa14ZCN072i2U')
bot.send_text_message(3720587844673826,'Testing..')

class Samplebot(object):
    def __init__(self, access_token, api_url=FACEBOOK_GRAPH_URL):
        self.access_token=access_token
        self.api_url=api_url

    def send_text_message(self,psid,messaging_type='RESPONSE'):
        headers={
        'Content-Type':'application/json'
        }

        data={
            'messaging_type':messaging_type,
            'recipient':{'id':psid},
            "message":{
            "text":"Hi, what can I do for you?",
            "quick_replies":[
            {
            "content_type":"text",
            "title":"Look for jobs",
            "payload":"<POSTBACK_PAYLOAD>"
            },{
            "content_type":"text",
            "title":"About the company",
            "payload":"<POSTBACK_PAYLOAD>"
            },{
            "content_type":"text",
            "title":"Others",
            "payload":"<POSTBACK_PAYLOAD>"
            }
            ]
            }
        }
        params = {'access_token':self.access_token}
        self.api_url=self.api_url + 'messages'
        response= requests.post(self.api_url,headers=headers,params=params,data=json.dumps(data))

        print(response.content)

# bot to ask where users live

class Wherebot(object):
    def __init__(self, access_token, api_url=FACEBOOK_GRAPH_URL):
        self.access_token=access_token
        self.api_url=api_url

    def send_text_message(self,psid,messaging_type='RESPONSE'):
        headers={
        'Content-Type':'application/json'
        }

        data={
            'messaging_type':messaging_type,
            'recipient':{'id':psid},
            "message":{
            "text":"Do you live in Japan now?",
            "quick_replies":[
            {
            "content_type":"text",
            "title":"Yes",
            "payload":"<POSTBACK_PAYLOAD>"
            },{
            "content_type":"text",
            "title":"No",
            "payload":"<POSTBACK_PAYLOAD>"
            }
            ]
            }
        }
        params = {'access_token':self.access_token}
        self.api_url=self.api_url + 'messages'
        response= requests.post(self.api_url,headers=headers,params=params,data=json.dumps(data))

        print(response.content)
