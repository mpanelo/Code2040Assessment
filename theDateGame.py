#!/usr/bin/python3

import requests, json, ast
import datetime

url = 'http://challenge.code2040.org/api/dating'
headers = {'content-type': 'application/json'}
payload = {'token': 'a73ecbe8d51588140dde230662aa86af'}

response = requests.post(url, data=json.dumps(payload), headers=headers)

timeData = ast.literal_eval(response.text)

extraSeconds = int(timeData['interval'])

# Format YYYY-MM-DD
date = timeData['datestamp'].split('T')[0]
# Format HH-MM-SS
time = timeData['datestamp'].split('T')[1]
# print(date + 'T' + time)

# Convert date from a string to a list
date = date.split('-')
# Covert time from a string to a list
time = time.split(':')
# Remove the 'Z' character from the last element of the time list
time[2] = time[2].rstrip('Z')

# Remove any leading 0's from each element in date and time, and convert all
# elements into integers.
for i in range(3):
    if date[i].startswith('0'):
        date[i] = date[i][1:]

    if time[i].startswith('0'):
        time[i] = time[i][1:]

    date[i] = int(date[i])
    time[i] = int(time[i])

dt = datetime.datetime(date[0], date[1], date[2], time[0], time[1], time[2])
addSeconds = datetime.timedelta(seconds=extraSeconds)
dt = dt + addSeconds

dateISOFormat = dt.isoformat() + 'Z'

newUrl = url + '/validate'
payload['datestamp'] =  dateISOFormat

newResponse = requests.post(newUrl, data=json.dumps(payload), headers=headers)
print(newResponse.status_code)

