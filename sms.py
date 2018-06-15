from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import sent, csv, glob

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    MESSAGE_FILE = 'message.txt'
    CSV_Responses = ["Responses/yeet.csv", "Responses/neet.csv", "Responses/other.csv"]
    CSV_Users = 'numberList.csv'    

    resp = MessagingResponse()

    number = request.form['From']
    message_body = request.form['Body']

    numberList = []
    with open(CSV_Users,'r') as csvfile:
        reader = csv.reader(csvfile)
        for number in reader:
            numberList.append(number)

    if number in numberList:
        if message_body.upper() == 'GET COUNT':
            yeets = count(CSV_Responses[0])
            neets = count(CSV_Responses[1])
            other = count(CSV_Responses[2])
            resp.message(
                'Yeets: {}'.format(yeets) + 
                '\nNeets: {}'.format(neets) + 
                '\nOthers: {}'.format(other) + 
                '\nResponse Rate: {}'.format(100* (yeets + neets + other)/(sum(1 for row in getNumbers())))+'%')
        
        elif message_body[0:6].upper() == "WRITE:":
            messageFile = open(MESSAGE_FILE, 'w')
            messageFile.write(message_body[7:])
            messageFile.close

        elif message_body.upper() == "SEND":
            messageFile = open(MESSAGE_FILE)
            resp.message(messageFile.read() + "\nSend these messages? [Type Yes to send] ")
        
        elif message_body.upper() == "YES":
            sent.Sent()

        elif message_body[0:4].upper() == "ADD ":
            with open(CSV_Users,'a') as csvfile:
                writer = csv.writer(csvfile)
            writer.writerow([message_body[4:]])
            #check to make sure this works properly

        else:
            print(number)
            print(message_body)
            resp.message("Invalid command please try one of the following \n\n\nGet count \nWrite: \nSend \nAdd")

    else:
        if message_body[0:4].upper() == 'YEET':
            write(CSV_Responses[0], number, message_body)
        elif message_body[0:4].upper() == 'NEET':
            write(CSV_Responses[1], number, message_body)
        else:
            write(CSV_Responses[2], number, message_body)

    return str(resp)

def getNumbers():
    allFiles = glob.glob("Participants" + "/*.csv")
    numbers = []
    for file in allFiles:
        with open(file, 'r') as csvfile:
            numbers += csv.reader(csvfile)
    return set([p[0] for p in numbers])

def count(file):
    with open(file,'r') as csvfile:
        reader = csv.reader(csvfile)
        return sum(1 for row in reader)

def write(file, number, message_body):
    with open(file,'a',newline='') as csvfileW:
        writer = csv.writer(csvfileW)
        writer.writerow([number] + [message_body])
            
if __name__ == "__main__":
    app.run(debug=True)
