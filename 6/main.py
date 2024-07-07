from get_content_cached import get_content
from bs4 import BeautifulSoup
import re
import json


def parse_bbc_sport():
    base_url = 'https://www.bbc.com'
    content = get_content(method='GET', url=f'{base_url}/sport', save_as_json=False)
    soup = BeautifulSoup(content, 'lxml')

    articles = soup.find_all('div', {'data-testid': 'promo', 'type': 'article'}, limit=5)
    print('Len:', len(articles))

    data = []

    for article in articles:
        a = article.find('a', {'class': re.compile('.+-PromoLink')})
        articleUrl = f'{base_url}{a.get("href").strip()}'
        print('articleUrl', articleUrl)

        articleContent = get_content(method='GET', url=articleUrl, save_as_json=False)
        articleSoup = BeautifulSoup(articleContent, 'lxml')
        topicBlock = articleSoup.find('div', {'data-component': 'topic-list'})

        topics = []
        for t in topicBlock.find_all('a'):
            topics.append(t.text)
        print('topics', topics)

        data.append({
            'Link': articleUrl,
            'Topics': topics,
        })

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    parse_bbc_sport()