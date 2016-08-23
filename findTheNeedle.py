#!/usr/bin/python3

import requests, json, ast


url = 'http://challenge.code2040.org/api/haystack'
headers = {'content-type': 'application/json'}
payload = {'token': 'a73ecbe8d51588140dde230662aa86af'}

response = requests.post(url, data=json.dumps(payload), headers=headers)

data = ast.literal_eval(response.text)

# Method 1

indexOfNeedle = data['haystack'].index(data['needle'])

# Method 2
"""
index = -1
for i in range(len(data['haystack'])):
    if data['haystack'][i] == data['needle']:
        index = i
"""

newUrl = url + '/validate'
payload['needle'] = indexOfNeedle

newResponse = requests.post(newUrl, data=json.dumps(payload), headers=headers)

print(newResponse.status_code)
