# -*- coding: utf-8 -*-
import requests
import json
import re
data = {
    "name": "Волков Иван Иванович",
    "phone": "+7 999 11111111",
    "offer": "iphone",
    "comments": "красный"
}
url = 'https://tlight.biz/media/zadane/tz1.php'
headers = {'content-type': 'application/json', 'X-Auth': 'tokentoken'}
r = requests.post(url=url, data=json.dumps(data), headers=headers)

if r.status_code == 200:
    id = re.search(r'<id>(.*)</id>',r.text).group(1)
    print('id: ', id)
else:
    print(r.status_code, r.text)