import scrapy
from scrapy.http import response
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
#from craigslist_sample.items import CraigslistSampleItem
from scrapy.contrib.spiders import CSVFeedSpider
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.selector import HtmlXPathSelector
class MySpider(CrawlSpider):
	name = "craigs"
	download_delay = 2
	allowed_domains = ["thivien.net"]
	start_urls = ["http://www.thivien.net/searchauthor.php?Country=2"]
	rules = (Rule (SgmlLinkExtractor(allow=[r'Country=2&Page=\d+']), follow=True),
	Rule(SgmlLinkExtractor(allow=(r'viewauthor')), callback='parse_item'),)
#restrict_xpaths=('//p[@id="nextpage"]',))
# def parse_item(self, response):
# hxs = HtmlXPathSelector(response)
# titles = hxs.select("//span[@class='pl']")
# items = []
# for titles in titles:
# item = CraigslistSampleItem()
# item ["title"] = titles.select("a/text()").extract()
# item ["link"] = titles.select("a/@href").extract()
# items.append(item)
# return items
	def parse_item(self,response):
		hxs = Selector(response)
		sites = hxs.xpath('//div[contains(@id,"PoemBody")]/text()')
		urls=hxs.xpath('//a[contains(@href,"viewpoem")]//@href')
		for url in urls:
			print url.extract()
			yield scrapy.Request("http://www.thivien.net/"+url.extract(), callback=self.getTho)
	def getTho(sefl,response):
		hxs = Selector(response)
		b=response.xpath("//p[contains(@class,'Poem_Han')]")
		if b:
			sites=response.xpath("//td[contains(@valign, 'top')]/p//text()")
		else:
			sites = hxs.xpath('//div[contains(@id,"PoemBody")]//text()')
			   
		
		author=hxs.xpath('//a[contains(@href,"viewauthor")]/b/text()')[0].extract().encode('utf-8')
		title=hxs.xpath('//a[contains(@name,"POEM")]/text()').extract()[0].encode('utf-8')
	# print author
	# print title
		filename="("+author+") "+title+".txt"
		filename=unicode(filename,"utf-8")
	# print filename
		print("***************************************************************************************")
		with open(filename,'w') as thefile:
			for site in sites:
				print>>thefile,site.extract().encode('utf-8')