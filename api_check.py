# -*- coding: utf-8 -*-
import requests
import re
url = 'https://tlight.biz/media/zadane/tz1.php'
payload = {'id': '5978527b91fab'}
headers = {'content-type': 'application/json', 'X-Auth': 'tokentoken'}
r = requests.get(url=url, headers=headers, params=payload)

if r.status_code == 200:
    status = re.search(r'<status>(.*)</status>', r.text).group(1)
    print('status: ', status)
else:
    print(r.status_code, r.text)