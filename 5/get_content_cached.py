import hashlib
import os
import time
import requests
import random
import json


def get_content(method='POST', url=None, headers=None, json_data=None, save_as_json=True):
    toHash = f'{url}{headers}{json_data}'
    filename = hashlib.md5(toHash.encode('utf-8')).hexdigest()
    dirname = 'cache'
    path = os.path.join(dirname, filename)

    os.makedirs(dirname, exist_ok=True)

    try:
        with open(path, 'r') as f:
            content = f.read()
            print('get from file')
            if save_as_json:
                return json.loads(content)
            else:
                return content
    except:
        response = None
        if method == 'GET':
            response = requests.get(url, headers=headers, json=json_data)
        elif method == 'POST':
            response = requests.post(url, headers=headers, json=json_data)

        secTimeout = random.uniform(0.5, 3)
        print('Sleep for {} seconds'.format(secTimeout))
        time.sleep(secTimeout)

        if not response.ok:
            print('Cannot get content, code: ', response.status_code)
            return

        print('get from server')

        with open(path, 'w') as f:
            if save_as_json:
                f.write(json.dumps(response.json(), indent=4))
                return response.json()
            else:
                f.write(response.text)
                return response.text