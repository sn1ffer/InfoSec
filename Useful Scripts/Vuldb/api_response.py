"""Auth API to change"""

import os
import yaml
import requests
import json

api_settings = yaml.load(open(os.path.abspath('api_config.yaml')), Loader=yaml.FullLoader)

postData = {'recent': int(api_settings['count'])}
postData['details'] = int(api_settings['details'])
url = api_settings['url']
personal_api_key = api_settings['personalApiKey']


userAgent = 'VulDB API Advanced Python Demo Agent'
headers = {'User-Agent': userAgent, 'X-VulDB-ApiKey': personal_api_key}

response = requests.post(url, headers=headers, data=postData)

if response.status_code == 200:
    responseJson = json.loads(response.content)
    result = responseJson['result']
