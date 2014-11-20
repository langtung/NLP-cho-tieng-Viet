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
	name = "vnexpress"
	allowed_domains = ["vnexpress.net"]
	start_urls = ["http://vnexpress.net/tin-tuc/the-gioi/page/2.html"]
	rules = (Rule (SgmlLinkExtractor(allow=[r'page/\d+']), follow=True),
	Rule(SgmlLinkExtractor(allow=(r'tin-tuc/the-gioi'),restrict_xpaths ='//div[contains(@class,"block_mid_new")]'), callback='getTho'),)
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
	# def parse_item(self,response):
		# hxs = Selector(response)
		# sites = hxs.xpath('//div[contains(@id,"PoemBody")]/text()')
		# urls=hxs.xpath('//a[contains(@class,"txt_link")]//@href')
		# for url in urls:
			# print url.extract()
			# yield scrapy.Request("http://www.thivien.net/"+url.extract(), callback=self.getTho)
	def getTho(sefl,response):
		hxs = Selector(response)
		a=response.xpath("//p[contains(@class,'Normal')]//text()")
		a=[''.join(a1 for a1 in a.extract())]
		#author=hxs.xpath('//a[contains(@href,"viewauthor")]/b/text()')[0].extract().encode('utf-8')
		title=hxs.xpath('//div/h1//text()')[0].extract()
		print title.encode('utf-8')
	# print author
	# print title
		filename=title+".txt"
		#filename=unicode(filename,"utf-8")
	# print filename
		print("***************************************************************************************")
		with open(filename,'wb') as thefile:
			for a1 in a:
				print>>thefile,a1.encode('utf-8')