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
import re
ptrn=u"'(.*?)'"
class MySpider(CrawlSpider):
	name = "vnthuquan"
	#download_delay = 1.2
	allowed_domains = ["vnthuquan.net"]
	ptrn=u"/'(.*?)/'"
	start_urls=["http://vnthuquan.net/truyen/truyen.aspx?tid=2qtqv3m3237nvntnvn4n3n31n343tq83a3q3m3237nvn"]
	with open('finalLinks.txt') as f:
		start_urls = [url.strip() for url in f.readlines()]	
	def parse(self,response):
		hxs = Selector(response)
		s=hxs.xpath("//div[@onclick]/@onclick")
		for s1 in s:
			print s1.extract()
		if(len(s)!=0):
			print(len(s))
			for s1 in s:
				s3=s1.extract()
				s2=re.search(ptrn,s3).group(1)
				url="http://vnthuquan.net/truyen/"+s2
				thefile1=open('CollectionLinks.txt','a')
				print>> thefile1,"%s	%s" % (response.url,url)
				#yield scrapy.Request(url,callback=self.getNoiDung)
		else:
			url1=re.sub("truyen/truyen","truyen/chuonghoi",response.url)
			thefile1=open('CollectionLinks.txt','a')
			print>> thefile1,"%s,%s" % (response.url,url1)
			#yield scrapy.Request(url1,callback=self.getNoiDung1)
	def getNoiDung1(self,response):
		hxs = Selector(response)
		a=hxs.xpath("//div[contains(@class,'truyen_text')]//text()")
		a1=hxs.xpath("//p[1]//text()").extract()[0]
		a2=hxs.xpath("//p[2]//text()").extract()[0]
		filename=a1+"-"+a2+".txt"
		try:
			with open(filename,'wb') as thefile:
				for a10 in a:
					print >> thefile,a10.extract().encode('utf-8')
		except:
			thefile1=open('damageLinks.txt','a')
			print>> thefile1,hxs.url()
	def getNoiDung(self,response):
		hxs = Selector(response)
		a=hxs.xpath("//div[contains(@class,'truyen_text')]//text()")
		a1=hxs.xpath("//p[1]//text()").extract()[0]
		a2=hxs.xpath("//p[2]//text()").extract()[0]
		a4=hxs.xpath("//p[4]//text()")[1].extract()
		a4=re.sub(r"\r|\n|\t","",a4).strip()
		try:
			a5=hxs.xpath("//p[5]//text()").extract()[0]
		except:
			a5=""
		filename=a1+"-"+a2 +"-"+a4+"-"+a5+".txt"
		#filename=unicode(filename,"utf-8")
		try:
			with open(filename,'wb') as thefile:
				for a10 in a:
					print >> thefile,a10.extract().encode('utf-8')
		except:
			thefile1=open('damageLinks.txt','a')
			print>> thefile1,response.url
		