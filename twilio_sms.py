from twilio.rest import Client

sid = #write here sid number
token = #write token number here
client = Client(sid,token)

my_msg = "Hi, It's Working correctly...☺"

client.messages.create(
	to= #type here number to whom you're sending ,
	from_= #type your number ,
	body=my_msg
	)
