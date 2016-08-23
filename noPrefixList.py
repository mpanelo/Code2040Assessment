#!/usr/bim/python3


import requests, json, ast


url = 'http://challenge.code2040.org/api/prefix'
headers = {'content-type': 'application/json'}
payload = {'token': 'a73ecbe8d51588140dde230662aa86af'}

response = requests.post(url, data=json.dumps(payload), headers=headers)

data = ast.literal_eval(response.text)
# print(data)

noPrefixList = []

for item in data['array']:
    if not item.startswith(data['prefix']):
        noPrefixList.append(item)

# print(noPrefixList)

newUrl = url + '/validate'
payload['array'] = noPrefixList

newResponse = requests.post(newUrl, data=json.dumps(payload), headers=headers)

print(newResponse.status_code)
