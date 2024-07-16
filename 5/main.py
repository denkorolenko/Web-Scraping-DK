import re
import json
import sqlite3
from get_content_cached import get_content


def write_json(urlJobTitle):
    data = []
    filename = 'jobs.json'

    for i, (url, jobTitle) in enumerate(urlJobTitle):
        data.append({
            'id': i + 1,
            'title': jobTitle,
            'url': url
        })

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    print('json created')


def write_sqlite(urlJobTitle):
    filename = 'jobs.db'

    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    sql = """
        create table if not exists jobs (
            id integer primary key,
            title text,
            url text
        )
    """
    cursor.execute(sql)

    for url, jobTitle in urlJobTitle:
        cursor.execute("""
            insert into jobs (title, url)
            values (?, ?)
        """, (jobTitle, url))

    conn.commit()
    conn.close()

    print('sqlite updated')


def parse_lejobadequat():
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
            'paged': 1,
        },
    }

    content = get_content(method='POST', url='https://www.lejobadequat.com/emplois', headers=headers, json_data=json_data)
    content = content['template']

    pattern = r'<a href=\"([^\"]+)\".+class=\"jobCard_link\"[^.]+<h3 class=\"jobCard_title\">(.+)</h3>'
    urlJobTitle = re.findall(pattern, content)

    print('urlJobTitle', urlJobTitle)

    write_json(urlJobTitle)
    write_sqlite(urlJobTitle)


if __name__ == '__main__':
    parse_lejobadequat()