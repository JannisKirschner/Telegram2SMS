from twilio.rest import Client
from telethon import TelegramClient, events, sync

##############################
#First go to www.twilio.com and register a number 
#Then go to  https://my.telegram.org -> Api Dev Tools to get a token
#Enter them into the script
#After running, enter the telegram 2fa token
##############################


account_sid = 'SECRET'
auth_token = 'TOKEN'
smsClient = Client(account_sid, auth_token)
twilio_phone = 'YOUR_TWILIO_PHONE_HERE'


api_id = SECRET
api_hash = 'TOKEN'
my_phone = ' +YOUR_PHONE_HERE'
client = TelegramClient('session_name', api_id, api_hash)
@client.on(events.NewMessage)

async def my_event_handler(event):
    
    excludeGroupChats = True;
    
    msg = event.message
    chat  = await event.get_chat()
    user = await event.get_sender()

    if(excludeGroupChats):
        if not hasattr(chat,'title'):
            sms = "Message: " + msg.message + " \n " + "User: " + user.username + " \n "
            if(event.sticker):
                sms += event.sticker.file_name + " "
            if(event.gif):
                sms += event.gif.file_name + " "
            if(event.voice):
                sms += event.voice.file_name + " "
            if(event.photo):
                sms += event.photo.file_name + " "
            message = smsClient.messages.create(body=sms, from_=twilio_phone, to=my_phone)

            print(message.sid)


   
client.start(my_phone)
print("---Welcome to telegram2sms---")
#print(client.get_me())
client.run_until_disconnected()




