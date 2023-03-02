import serial
MySerial = serial.Serial('/dev/tty.usbmodem1101', baudrate=115200)

BaseID = 'tbln5MUszSys14Ue0'
token = 'patpkXlkSq8Kmzzld.9b0f1f4f2fe44bbe40edc41508302dbb415284d2eb18aa3e6e307a19295410a5'


URL = 'https://api.airtable.com/v0/appJumgmG0eu9J8Vi/Table%201'
headers = {'Authorization': 'Bearer ' + token}

import requests

r = requests.get(URL, headers = headers)
print(r.status_code)
data = r.json()
value = data ['records'][1]['fields']['Value']
print (value) # use value as a motor speed for the car


# r = requests.get (URL)
# r.status_code

airtablevalue = value

while True:
    # Insert Code to read Airtable
    if airtablevalue == 1:
        break

MySerial.write(b'import POT_CONTROL\r\n')
MySerial.write(b'POT_CONTROL.main()\r\n')
