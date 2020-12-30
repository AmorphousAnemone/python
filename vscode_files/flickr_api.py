import requests
import pprint
import firefox_browser
import random
import time

print('hello')

response = requests.get('https://picsum.photos/v2/list?limit=100')

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found: ' + str(response.status_code))


data = response.json()
print(len(data))
for i in range(10):
    url = data[random.randrange(0, 100)]['url']
    firefox_browser.firefox(url)
    time.sleep(4)