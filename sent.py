import sms, APIKeys
from twilio.rest import Client

MESSAGE_FILE = 'message.txt'
account_sid = APIKeys.account_sid
auth_token = APIKeys.auth_token
from_num = APIKeys.from_num 

def Sent():
	with open(MESSAGE_FILE, 'r') as content_file:
		message = content_file.read()

	numbers = sms.getNumbers()
	client = Client(account_sid, auth_token)

	for number in numbers:
		print("Sending to " + number)
		message = client.messages.create(to=number, from_=from_num, body=message)
