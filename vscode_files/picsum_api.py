# Generate random images throuh picsum website's free API.
# No authentication is required

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
print(data[0])
url = data[random.randrange(1, 100)]['url']
time.sleep(2)
firefox_browser.firefox(url)
print(url)