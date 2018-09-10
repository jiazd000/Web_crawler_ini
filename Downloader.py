from urllib2 import *
from urllib import *
#from urllib2 import request

class Downloader:
	## ofer something function to get web information
	## like http status or html source
	
	def __init__(self):
	
		pass
		
	@staticmethod
	def GethttpStatus(url):
		##get the http code of url
		
		try:
		
			#return request.urlopen(url).status
			return urlopen(url)  #.status
			
		except Exception as e:
		
			print e
			
			return None
			
			
	@staticmethod
	def DownloadPageEx(url,retry_times=3,user_agent="wswp",charset='gbk'):
		# get the source of html
		
		headers={'User-agent':user_agent}
		
		#request_=request.Request(url,headers=headers)
		request_=Request(url,headers=headers)
		
		if retry_times>0:
		
			print'downloading...',url
			
			try:
			
				html=urlopen(url).read().decode(charset,'ignore')
				print'download successfully...'
			except Exception as e:
				
				print'download failed...'
				print e
				httpStatus=Downloader.GethttpStatus(url)
				if httpStatus==None:
				
					print'perhaps the url is not exit..'
				elif httpStatus>=500:
				
					print 'retry to download url'
					return DownloadPageEx(rul,retry_times=1)
					
				elif httpStatus>=400:
					print'the page is wrong'
				html=None
				
			return html
			
	@staticmethod
	def Crawlsitemap(url):
	
		sitemap=Downloader.DownloadPageEx(url)
		print sitemap
		if sitemap==None:
			print 'download failed...'
			return
			
		links=re.findall('<loc>(.*?)</loc>',sitemap)
		for link in links:
		
			html=WebInfo.DownloadPageEx(link)
			
	@staticmethod
	def DownloadSource(url,path):
	
		try:
		
			#request.urlretrieve(url,path)
			urlretrieve(url,path)
		except Exception as e:
		
			print'failed to download...'
	
	
	
	
	
	
	
	
		
		
		
		
		
		
		
		
		
					
				
				
				
				
				
				
				
	
	
	
	
	
	
	
	
	
	
	
	
	