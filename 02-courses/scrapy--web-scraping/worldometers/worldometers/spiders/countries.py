import scrapy
import logging


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = [
        'https://www.worldometers.info/world-population/population-by-country/'
    ]

    def parse(self, response):
        countries = response.xpath('//td/a')
        for country in countries:
            name = country.xpath('.//text()').get()
            link = country.xpath('.//@href').get()

            # 1st way of retrieving each link
            # absolute_url = response.urljoin(link)
            # yield scrapy.Request(url=absolute_url)

            # 2nd way of retrieving each link
            yield response.follow(
                url=link,
                callback=self.parse_country,
                meta={'country_name': name})

    def parse_country(self, response):
        country_name = response.request.meta['country_name']
        rows = response.xpath(
            "(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr"
        )

        for row in rows:
            year = row.xpath('.//td[1]/text()').get()
            population = row.xpath('.//td[2]/strong/text()').get()
            yearly_pct_change = row.xpath('.//td[3]/text()').get()
            yearly_change = row.xpath('.//td[4]/text()').get()
            migrants_net = row.xpath('.//td[5]/text()').get()
            median_age = row.xpath('.//td[6]/text()').get()
            fertility_rate = row.xpath('.//td[7]/text()').get()
            pop_density = row.xpath('.//td[8]/text()').get()
            urban_pop = row.xpath('.//td[9]/text()').get()
            pct_of_world_pop = row.xpath('.//td[10]/text()').get()
            world_pop = row.xpath('.//td[11]/text()').get()
            global_rank = row.xpath('.//td[12]/text()').get()

            yield {
                'country': country_name,
                'year': year,
                'population': population,
                'yearly_pct_change': yearly_pct_change,
                'yearly_change': yearly_change,
                'migrants_net': migrants_net,
                'median_age': median_age,
                'fertility_rate': fertility_rate,
                'pop_density': pop_density,
                'urban_pop': urban_pop,
                'pct_of_world_pop': pct_of_world_pop,
                'world_pop': world_pop,
                'global_rank': global_rank,

            }
