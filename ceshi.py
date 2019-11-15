import requests


head = requests.api.head('https://www.csdn.net/')



print(head.headers)
print(head.content.decode('UTF-8'))


