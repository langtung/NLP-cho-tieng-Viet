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
from scrapy.http import Request,FormRequest
class MySpider(CrawlSpider):
	name = "vnthuquan"
	download_delay = 2
	allowed_domains = ["vnthuquan.net"]
	start_urls = ["http://vnthuquan.net/truyen/"]
	
	def getTho(self,response):
		hxs = Selector(response)
		a=response.xpath('///td//a[contains(@href,"java")]/text()')
		with open('testLink.txt','wb') as thefile:
			for a1 in a:
				print>> thefile,a.extract()
	
	def parse(self, response): # select 50 products on each page
		return[FormRequest.from_response(response,
		formdata={'DataGrid1$ctl24$ctl00': ''},
		dont_click=True,
		callback=self.getTho)]
		


	
		
	# def getTho(sefl,response):
		# hxs = Selector(response)
		# b=response.xpath("//p[contains(@class,'Poem_Han')]")
		# if b:
			# sites=response.xpath("//td[contains(@valign, 'top')]/p//text()")
		# else:
			# sites = hxs.xpath('//div[contains(@id,"PoemBody")]//text()')
			   
		
		# author=hxs.xpath('//a[contains(@href,"viewauthor")]/b/text()')[0].extract().encode('utf-8')
		# title=hxs.xpath('//a[contains(@name,"POEM")]/text()').extract()[0].encode('utf-8')
	# print author
	# print title
		filename="("+author+") "+title+".txt"
		filename=unicode(filename,"utf-8")
	# print filename
		# print("***************************************************************************************")
		# with open(filename,'w') as thefile:
			# for site in sites:
				# print>>thefile,site.extract().encode('utf-8')
