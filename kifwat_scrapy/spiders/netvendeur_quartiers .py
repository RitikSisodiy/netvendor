import json
import re
from itertools import zip_longest, takewhile, dropwhile
from unittest import result
from kifwat_scrapy.main import uploaddata , clear_migrations
# from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import signals
import pdb
class URL:
    def __init__(self,url) -> None:
        self.url = url
    def text(self):
        return self.url
class Link:
    def extract_links(self,res):
        links = [
            URL("https://www.netvendeur.com/prix/region-auvergne-rhone-alpes-3/"),
            URL("https://www.netvendeur.com/prix/region-bourgogne-franche-comte-5/"),
            URL("https://www.netvendeur.com/prix/region-bretagne-6/"),
            URL("https://www.netvendeur.com/prix/region-centre-val-de-loire-7/"),
            URL("https://www.netvendeur.com/prix/region-corse-9/"),
            URL("https://www.netvendeur.com/prix/region-grand-est-1/"),
            URL("https://www.netvendeur.com/prix/region-hauts-de-france-17/"),
            URL("https://www.netvendeur.com/prix/region-ile-de-france-12/"),
            URL("https://www.netvendeur.com/prix/region-normandie-4/"),
            URL("https://www.netvendeur.com/prix/region-nouvelle-aquitaine-2/"),
            URL("https://www.netvendeur.com/prix/region-occitanie-13/"),
            URL("https://www.netvendeur.com/prix/region-outre-mer-23/"),
            URL("https://www.netvendeur.com/prix/region-pays-de-la-loire-19/"),
            URL("https://www.netvendeur.com/prix/region-provence-alpes-cote-d-azur-18/"),
        ]
        return links
class NetvendeurQuartiersSpider(CrawlSpider):
    name = 'netvendeur_quartiers'
    start_urls = [
        'https://www.netvendeur.com/prix-immobilier/'
    ]
    res= {
        "regionid":None,
        "departmentid":None,
        "cityid":None,
        "quaterid":None,
    }
    rules = (
        Rule(
            Link(),
            callback='parse_region',
            cb_kwargs=dict(parenturl = start_urls[0])
        ),
    )
    result=[]
    custom_settings = {
        'CONCURRENT_REQUESTS': 1,
        # 'FEEDS': {
        #     'netvendeur.csv': {
        #         'format': 'csv',
        #         'fields': [
        #             'Name', 'Prix bas maison', 'Prix moyen maison', 'Prix haut maison',
        #             'Prix bas apparetement', 'Prix moyen apparetement', 'Prix haut apparetement',

        #             'depuis 2 ans maisons', 'depuis 2 ans appartements', 'depuis 1 an maisons',
        #             'depuis 1 an appartements', 'depuis 6 mois maisons', 'depuis 6 mois appartements',
        #             'depuis 3 mois maisons', 'depuis 3 mois appartements',

        #             'Maisons', 'Appartements',
        #             '- de 35m2', '35m2 - 80m2', '80m2 - 110m2', '+ de 150m2',
        #             '1 pièce', '2 pièces', '3 pièces', '+ 4 pièces',
        #             'volume', 'evolution', 'price_chart',

        #             "Répartition selon l'âge", "Répartition selon l'activité (Hommes)",
        #             "Répartition selon l'activité (Femmes)",

        #             'Habitants', 'Population', 'Superficie', 'Marie', 'Logements', 'price_table',

        #             'region', 'dept', 'city', 'quarter', 'proximité'
        #         ]
        #     },
        # },
        'DUPEFILTER_CLASS': 'kifwat_scrapy.middlewares.CustomFilter',
        'USER_AGENT': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        print("its running")
        spider = super(NetvendeurQuartiersSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.after_spider_closed, signal=signals.spider_closed)
        return spider

    def after_spider_closed(self, spider):
        print("deleteing the migration record from table")
        clear_migrations()
    def parse_item(self, response, **__):
        typeofdata = __['typeofdata']
        parenturl = __['parenturl']
        breadcrumbs = response.css('[itemprop="itemListElement"] [itemprop="name"]::text').extract()[2:]
        breadcrumbs_dict = dict(zip_longest(['region', 'dept', 'city', 'quarter', 'proximité'], breadcrumbs))
        bas_maison, moyen_maison, haut_maison = response.xpath(
            'normalize-space(//p[@class="re-prices"])').extract_first().split('<')

        prices = response.xpath(
            'normalize-space(//div[contains(@class, "re-appart")]//p[@class="re-prices"])'
        ).extract_first().split('<')

        try:
            appt_bas_maison, appt_moyen_maison, appt_haut_maison = prices
        except ValueError:
            appt_bas_maison = appt_moyen_maison = appt_haut_maison = ''

        table_evo = [[td_or_th.css('::text').extract_first() for td_or_th in tr.xpath('./*')]
                     for tr in response.css('.table-evo tr')]

        if response.meta.get('quarter'):
            breadcrumbs_dict['proximité'] = breadcrumbs_dict['quarter']
            breadcrumbs_dict['quarter'] = response.meta['quarter']

        price_chart = response.css('script:contains("ct-chart-price")').re_first('data:\s*({[\w\W]*?}),\s*options') or '{}'
        price_chart = json.loads(re.sub('(\w+):', r'"\1":', price_chart).replace("'", '"'))

        price_chart = {f'{data_set["label"]} {label}': value  for data_set in price_chart['datasets'] for label, value in zip(price_chart['labels'], data_set['data'])}

        curl = response.request.url
        result =  {
            # 'Name': response.css('#TitreTypeBien:contains("-")::text').extract_first().split('- ')[-1],
            'Name': breadcrumbs[-1],
            'Prix bas maison': re.findall('^([^€]*)', bas_maison)[0].replace(' ', ''),
            'Prix moyen maison': re.findall('^([^€]*)', moyen_maison)[0].replace(' ', ''),
            'Prix haut maison': re.findall('^([^€]*)', haut_maison)[0].replace(' ', ''),

            'Prix bas apparetement': (re.findall('^([^€]*)', appt_bas_maison) or [''])[0].replace(' ', ''),
            'Prix moyen apparetement': (re.findall('^([^€]*)', appt_moyen_maison) or [''])[0].replace(' ', ''),
            'Prix haut apparetement': (re.findall('^([^€]*)', appt_haut_maison) or [''])[0].replace(' ', ''),

            **{
                f'{h} {h2}'.lower(): table_evo[r_i + 1][c_i + 1]
                for c_i, h in enumerate(table_evo[0][1:])
                for r_i, h2 in enumerate(list(map(lambda row: row[0], table_evo[1:])))
            },

            'price_chart': json.dumps(price_chart, ensure_ascii=False),

            **(breadcrumbs_dict),

            **self._partition_by_type(response),
            **self._partition_by_area(response),
            **self._partition_by_number_of_pieces(response),
            'volume': self._get_volume_table(response),
            'evolution': self._get_evolution_table(response),

            "Répartition selon l'âge": self._get_partition_by_age(response),
            "Répartition selon l'activité (Hommes)": self._get_activity_by_men(response),
            "Répartition selon l'activité (Femmes)": self._get_activity_by_women(response),

            **self._price_and_estimate_tables(response),
            'source':curl,
        }
        zipcode = (curl[curl.rfind('-')+1:]).replace("/",'')
        result['zip_code'] = zipcode if zipcode.isnumeric() else None
        # print(zipcode)
        uploaddata(result,typeofdata,parenturl)
        # self.result.append([result,typeofdata,parenturl])
        # if len(self.result)==100:
        #     self.res = uploaddata(self.result)
        #     self.result=[]
        # print(self.res)
        return result

    def parse_region(self, response, **kwargs):
        for link in LinkExtractor(
                restrict_xpaths=['//h2[contains(., "départements")]/../div[contains(@class, "list_dep")]'],
                allow=['/prix/']
        ).extract_links(response):
            yield response.follow(
                link.url,
                callback=self.parse_dept,
                cb_kwargs=dict(parenturl = response.request.url)
            )
    def expand_city(self, response, **kwargs):
        for link in LinkExtractor(
                    restrict_css=['table'],
                    allow=['/prix/']
            ).extract_links(response):
                print(link,link.url)
                yield response.follow(
                    link.url,
                    callback=self.parse_city,
                    cb_kwargs=dict(parenturl = kwargs["parenturl"])
                )
    def parse_dept(self, response, **kwargs):
        if response.css("#prix-departement .black_title .black_title a"):
            for link in LinkExtractor(
                    restrict_css=['#prix-departement .black_title .black_title a'],
                    allow=['/prix/']
            ).extract_links(response):
                yield response.follow(
                    link.url,
                    callback=self.expand_city,
                    cb_kwargs=dict(parenturl = response.request.url)
                )
        else:
            for link in LinkExtractor(
                    restrict_xpaths=['//h3[contains(., "villes")]/../div[contains(@class, "list_dep")]','//*[@id="prix-arrondissement"]'],
                    allow=['/prix/']
            ).extract_links(response):
                yield response.follow(
                    link.url,
                    callback=self.parse_city,
                    cb_kwargs=dict(parenturl = response.request.url)
                )
    def expand_quater(self, response, **kwargs):
        for link in LinkExtractor(
                    restrict_css=['table'],
                    allow=['/prix']
            ).extract_links(response):
                yield response.follow(
                    link.url,
                    callback=self.parse_item,
                    cb_kwargs=dict(typeofdata='city_streets',parenturl = kwargs["parenturl"])
                )
    def parse_city(self, response, **kwargs):
        yield self.parse_item(response,typeofdata='city',**kwargs)
        for link in LinkExtractor(
                restrict_css=['div#prix-autre-quartier'],
                allow=['/prix/']
        ).extract_links(response):
            yield response.follow(
                link.url,
                callback=self.parse_item,
                cb_kwargs=dict(parenturl = response.request.url,typeofdata='quater')
            )

    def parse_quarter(self, response, **kwargs):
        yield self.parse_item(response,typeofdata='quater',**kwargs)
        
        breadcrumbs = response.css('[itemprop="itemListElement"] [itemprop="name"]::text').extract()[2:]
        breadcrumbs = dict(zip_longest(['region', 'dept', 'city', 'quarter', 'proximité'], breadcrumbs))

        for link in LinkExtractor(
                restrict_css=['div#prix-rue'],
                allow=['/prix']
        ).extract_links(response):
            # request proximity areas inside the city
            yield response.follow(
                link.url,
                meta={'quarter': breadcrumbs['quarter']},
                callback=self.parse_item,
                cb_kwargs=dict(typeofdata='streets',parenturl = response.request.url)
            )

    def _partition_by_type(self, response):
        head = response.xpath(
            '//div[@id="repartition"]//*[contains(., "Répartition selon le type de biens")]//div[@class="title-graph"]/text()'
        ).extract()

        values = response.xpath(
            '//div[@id="repartition"]//*[contains(., "Répartition selon le type de biens")]//span[@class="text-val"]/text()'
        ).extract()

        return dict(zip(head, values))

    def _partition_by_area(self, response):
        return self._get_maison_and_appartments(response, 'Répartition selon la superficie')

    def _partition_by_number_of_pieces(self, response):
        return self._get_maison_and_appartments(response, 'Répartition selon le nombre de pièce')

    def _get_maison_and_appartments(self, response, _key):
        heads = response.xpath(
            f'//div[@id="repartition"]//*[contains(., "{_key}")]//div[@class="title-graph"]/text()'
        ).extract()

        values = [
            {
                'maison': report.xpath('.//span[@class="grap-maison"]/@style').re_first('[\d.]+') or '0',
                'appartment': report.xpath('.//span[@class="grap-val"]/@style').re_first('[\d.]+') or '0'
            } for report in response.xpath(
                f'//div[@id="repartition"]//*[contains(., "{_key}")]//div[@class="repart-jauge"]')
        ]

        return {head: json.dumps(value, ensure_ascii=False).replace('"', "'") for head, value in zip(heads, values)}

    def _get_volume_table(self, response):
        table = response.css('#volume-de-bien table')

        if not table.css('tr'):
            return '{}'

        head = [h for h in table.css('tr')[0].xpath('./td/text()').extract() if h.strip()]

        result = []
        for row in table.css('tr')[1:]:
            row_values = [h for h in row.xpath('./td/text()').extract() if h.strip()]

            row_result = {}
            for h, v in zip(head, row_values[1:]):
                row_result[f'{h}, {row_values[0]}'] = v

            result += [row_result]

        return json.dumps(result, ensure_ascii=False).replace('"', "'")

    def _get_evolution_table(self, response):
        result = {}
        for v in response.css('.verticale_volume'):
            head = v.xpath('./following-sibling::div/text()').extract_first()

            result[f'maison, {head}'] = v.css('.maisonv div::attr(style)').re_first('[\d.]+')
            result[f'appartment, {head}'] = v.css('.appartementv div::attr(style)').re_first('[\d.]+')

        return json.dumps(result, ensure_ascii=False).replace('"', "'")

    def _get_partition_by_age(self, response):
        return self._get_chart_data(response, 'repartion-pop-age')

    def _get_activity_by_men(self, response):
        return self._get_chart_data(response, 'repartion-activite-homme')

    def _get_activity_by_women(self, response):
        return self._get_chart_data(response, 'repartion-activite-femme')

    def _get_chart_data(self, response, _key):
        slashed_key = _key.replace("-", "\-")

        raw_json = json.loads(
            re.sub(
                '(\w+):([\w\W]+?)',
                r'"\1":\2',
                response.css(f'script:contains({_key})').re_first(
                    f'{slashed_key}[\w\W]*?data[\w\W]*?({{[\w\W]+?}}),\s*options'
                ) or '{}'
            ).replace("'", '"')
        )

        if raw_json:
            return json.dumps(dict(zip(raw_json['labels'], raw_json['datasets'][0]['data'])),
                              ensure_ascii=False).replace('"', "'")

        return json.dumps({}, ensure_ascii=False)

    def _price_and_estimate_tables(self, response):
        info_table = [t for t in response.css('table:contains(Habitants) td::text').extract() if t.strip()]

        if not info_table:
            return {}

        key_values = list(takewhile(lambda i: 'Logements' != i, info_table))
        result = dict(zip(key_values[::2], key_values[1::2]))

        key_values = list(dropwhile(lambda i: 'Logements' != i, info_table))

        result[key_values[0]] = ','.join(key_values[1:])

        result['price_table'] = price_table = []

        table = response.xpath('//div[@id="en-savoir-plus"]//table[2]')

        if not table.css('tr'):
            result['price_table'] = '{}'
            return result

        head = [h for h in table.css('tr')[0].xpath('./td/text()').extract() if h.strip()]

        for row in table.css('tr')[1:]:
            row_values = [h for h in row.xpath('./td/text()').extract() if h.strip()]

            if not row_values:
                continue

            row_result = {}
            for h, v in zip(head, row_values[1:]):
                row_result[f'{h}, {row_values[0]}'] = v

            price_table += [row_result]

        result['price_table'] = json.dumps(price_table, ensure_ascii=False).replace('"', "'")

        return result
