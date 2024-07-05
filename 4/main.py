import requests
import re
import time
import random
import json


def parse_lejobadequat_site(numOfPages=1):

    jobTitles = []

    for pageIndex in range(numOfPages):
        currentPage = pageIndex + 1

        print('Current page: ', currentPage)

        headers = {
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/json',
            'origin': 'https://www.lejobadequat.com',
            'referer': 'https://www.lejobadequat.com/emplois',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }

        json_data = {
            'action': 'facetwp_refresh',
            'data': {
                'facets': {
                    'recherche': [],
                    'ou': [],
                    'type_de_contrat': [],
                    'fonction': [],
                    'load_more': [
                        3,
                    ],
                },
                'frozen_facets': {
                    'ou': 'hard',
                },
                'http_params': {
                    'get': [],
                    'uri': 'emplois',
                    'url_vars': [],
                },
                'template': 'wp',
                'extras': {
                    'counts': True,
                    'sort': 'default',
                },
                'soft_refresh': 1,
                'is_bfcache': 1,
                'first_load': 0,
                'paged': currentPage,
            },
        }

        response = requests.post('https://www.lejobadequat.com/emplois', headers=headers, json=json_data)

        print('Status code:', response.status_code)
    
        if not response.ok:
            # we could add here a retry logic instead
            print('Statuc code is not valid, stoping execution')
            return

        content = response.json()['template']
        # print('Content:', content)

        pattern = r"<h3 class=\"jobCard_title\">(.+)</h3>"
        tempJobTitles = re.findall(pattern, content)
        print('Job Titles:', tempJobTitles)

        jobTitles.extend(tempJobTitles)

        secTimeout = random.uniform(0.5, 3)
        print('Sleep for {} seconds'.format(secTimeout))
        time.sleep(secTimeout)

    # save jobs to file
    with open('result.json', 'w') as f:
        f.write(json.dumps(jobTitles, indent=4))


if __name__ == '__main__':
    parse_lejobadequat_site(numOfPages=3)
