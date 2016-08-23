#!/usr/bin/python3

import requests, json


url = 'http://challenge.code2040.org/api/reverse'
headers = {'content-type': 'application/json'}
payload = {'token': 'a73ecbe8d51588140dde230662aa86af'}

response = requests.post(url, data=json.dumps(payload), headers=headers)

someString = response.text

# Method 1
"""
listOfChars = list(someString)
listOfChars.reverse()
reversedString = ''.join(listOfChars)
"""

# Method 2

reversedString = someString[::-1]

# Method 3
"""
reversedString = ''
for i in range(len(someString) - 1, -1, -1):
    reversedString += someString[i]
"""

print('Original string: %s' % response.text)
print('Reversed string: %s' % reversedString)


payload['string'] = reversedString
newUrl = url + '/validate'
newResponse = requests.post(newUrl, data=json.dumps(payload), headers=headers)

print(newResponse.status_code)
