from scrapy import Spider
from scrapy.selector import Selector

from ..items import Index, sintaScore, scopusScore, jurnalData, Title, Nav


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["sinta2.ristekdikti.go.id"]
    start_urls = [
        "http://sinta2.ristekdikti.go.id/affiliations/detail?page=2&id=384&view=documents&q=smart%20city&search=1", ]

    def parse(self, response):
        questions = Selector(response).xpath('//dt[@class="uk-text-primary"]')
        question1 = Selector(response).xpath('//dl[@class="uk-description-list-line"]')
        question2 = Selector(response).xpath('//div[@class="uk-width-large-1-4 sinta-stat2"]')
        question3 = Selector(response).xpath('//div[@class="uk-width-large-1-4 scopus-stat2"]')
        question4 = Selector(response).xpath('//li[@class="rel-links"]')

        item5 = Title()
        item5['title'] = response.selector.xpath(
            '//title[not(@*)]/text()').extract()[0]
        yield item5

        for question in questions:
            item1 = jurnalData()
            item1['title'] = question.xpath(
                'a[@class="paper-link"]/text()').extract()[0]
            item1['url'] = question.xpath(
                'a[@class="paper-link"]/@href').extract()[0]
            yield item1

        for question in question1:
            item5 = Index()
            item5['index_by'] = question.xpath(
                'dd[@class="indexed-by"]/text()').extract()[0]
            yield item5

        for question in question2:
            item2 = sintaScore()
            item2['score'] = question.xpath(
                'div[@class="stat2-lbl"]/text()').extract()[0]
            item2['total'] = question.xpath(
                'div[@class="stat2-val"]/text()').extract()[0]
            yield item2

        for question in question3:
            item3 = scopusScore()
            item3['score'] = question.xpath(
                'div[@class="stat2-lbl"]/text()').extract()[0]
            item3['total'] = question.xpath(
                'div[@class="stat2-val"]/text()').extract()[0]
            yield item3

        for question in question4:
            item4 = Nav()
            item4['title'] = question.xpath(
                'a[@class="hvr-grow"]/text()').extract()[0]
            item4['url'] = question.xpath(
                'a[@class="hvr-grow"]/@href').extract()[0]
            yield item4
            
