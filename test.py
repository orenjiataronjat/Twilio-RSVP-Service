import csv, sys, glob, os, APIKeys
from twilio.rest import Client
import pandas as pd

MESSAGE_FILE = 'message.txt'
account_sid = APIKeys.account_sid
auth_token = APIKeys.auth_token
from_num = APIKeys.from_num 

# with open(MESSAGE_FILE, 'r') as content_file:
# 	sms = content_file.read()

# 	allFiles = glob.glob("Participants" + "/*.csv") 
# 	print(allFiles)
# 	peoplereader = []
# 	for file in allFiles:
# 		df = pd.read_csv(file,index_col=None, header=0)
# 		peoplereader.append(df)

# 	flatpeople = [item for sublist in peoplereader for item in sublist]
# 	print(flatpeople)
# 	numbers = set([p[0] for p in flatpeople])
# 	print('10')
# 	client = Client(account_sid, auth_token)
# 	print('11')
# 	print(numbers)
	
# 	for num in numbers:
# 		print('12')
# 		print("Sending to " + num)


def Sent():
	with open(MESSAGE_FILE, 'r') as content_file:
		sms = content_file.read()

	allFiles = glob.glob("Participants" + "/*.csv")
	peoplereader = []
	for file in allFiles:
		with open(file, 'r') as csvfile:
			peoplereader += csv.reader(csvfile)
	numbers = set([p[0] for p in peoplereader]) # remove duplicate numbers

	client = Client(account_sid, auth_token)

	for num in numbers:
		print("Sending to " + num)
		message = client.messages.create(to=num, from_=from_num, body=sms)

Sent()

'''
Removed code from get count in sms.py
            # with open(CSV_Respones['yeet'],'r') as csvfile1:
            #     reader1 = csv.reader(csvfile1)
            #     with open(CSV_Respones['neet'],'r') as csvfile2:
            #         reader2 = csv.reader(csvfile2)
            #         yeetCount = row_count = sum(1 for row in reader1)
            #         neetCount = row_count = sum(1 for row in reader2)
            #         resp.message('Yeets: {}'.format(yeetCount) + '\nNeets: {}'.format(neetCount) + '\nYeetsC: {}'.format(yeets) + '\nNeetsC: {}'.format(neets))
'''