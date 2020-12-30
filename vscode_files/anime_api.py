import requests
import pprint
# import firefox_browser
# import time

print('hello')

response = requests.get('https://www.flickr.com/services/rest/')

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found: ' + str(response.status_code))
