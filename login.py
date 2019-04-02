# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit


import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
payload = { 'nm': 'user@email.com', 'password': 'blahblahsecretpassw0rd' }
#This URL will be the URL that your login form points to with the "action" tag.
url = 'http://127.0.0.1:5000/loginform'
#This URL is the page you actually want to pull down with requests.
requesturl = 'http://localhost:5000/hello/'

with requests.Session() as session:
    post = session.post(url, data=payload)
    print(post.text)
    #print(r.text)   #or whatever else you want to do with the request data!
