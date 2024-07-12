import scrapy
import re


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    max_count_follow = 1

    def parse(self, response):
        quotes = response.xpath('//div[contains(@class, "quote")]')
        for quote in quotes:
            text_xpath = './span[contains(@class, "text")]/text()'
            text = quote.xpath(text_xpath).get()
            text = re.sub('^“|”$', '', text)

            author_xpath = './/small[contains(@class, "author")]/text()'
            author = quote.xpath(author_xpath).get()

            yield {
                'text': text,
                'author': author,
            }

        next_btn = response.xpath('//li[@class="next"]/a/@href').get()
        if next_btn and self.max_count_follow:
            self.max_count_follow -= 1
            yield response.follow(next_btn, callback=self.parse)
