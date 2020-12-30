# This script connects to the "Daily Smarty" API and gets 
# the site's urls and automatically opens them in Firefox for Ubuntu.

import requests
import pprint
import firefox_browser
import time

response = requests.get('https://api.dailysmarty.com/posts')

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

# json returns a dict(). keys and values.
data = response.json()
posts = data['posts']

for i in range(len(posts)):
    url = posts[i]['url_for_post']
    firefox_browser.firefox(url)
    print('Opening: ' + url)
    time.sleep(1.5) # delay to prevent opening links simultaneously

print('done')