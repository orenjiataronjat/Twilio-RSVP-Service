Github wouldn't allow me to upload blank csv files so each one has the letter a in it, remove those

In APIKeys.py please put in your credentials
In the Participants folder the csv files should contain phone numbers separated by cells in the rows
Add your phone number to numberList.csv in order to access the get count, write, send and add commands

Responses to the phone number you add in the credentials will be stored in the Response folder. 

The default responses are Yeet (yes) and Neet (no). They are not caps sensitive and all other responses will be saved into other.csv

Multiple CSV files can be read in from the Participants folder

test.py contains extra code I was using for trying to test different features.

To run the program open two terminal windows and type in to the first terminal
python -m sms

And into the second terminal
./ngrok http 5000

Just text the number in your credentials and the app should work