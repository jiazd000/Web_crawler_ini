from MatchModel import *
from Downloader import *
import threading
import re
import os

class crawer(threading.Thread):

	def __init__(self,url,name):
	
		threading.Thread.__init__(self)
		self.url=url
		self.name=name
		self.image_list1=[]
		self.image_list2=[]
		
		self.__initialize()

		
	def __initialize(self):
	
		content=Downloader.DownloadPageEx(self.url,charset='gb2312')
		#print self.name
		#if self.name=='1':
			#print content
			#print'test1'
			#os._exit()
		self.image_list11=re.findall(COMMON_PICTURE_JPG,content)
		self.image_list22=re.findall(COMMON_PICTURE_PNG,content)
		
		for i in self.image_list11:
		
			#print i
			
			self.image_list1.append(i.split("\t")[0])
			
		for i in self.image_list22:
		
			self.image_list2.append(i.split("\t")[0])
		
		
	def run(self):
		
		index=0
		
		for url in self.image_list1:
			
			filepath="d:\PIC\\"+self.name+str(index)+".jpg"
			Downloader.DownloadSource(url,filepath)
			index+=1
			
			
		for url in self.image_list2:
			
			filepath="d:\PIC\\"+self.name+str(index)+".png"
			Downloader.DownloadSource(url,filepath)
			index+=1
			
			
			
class Spider:

	def __init__(self,root_url):
	
		self.url=root_url
		self.url_list=[]
		self.__initialize()
		
	def __initialize(self):
	
		content=Downloader.DownloadPageEx(self.url,charset='utf-8')
		post=r'href="/p/[0-9]*"'
		ls=re.findall(post,content)
		for i in ls:
			
			url="http://tieba.baidu.com"
			card_url=url+i.split("\"")[1]
			self.url_list.append(card_url)
			
		
	def StartDownloading(self):
	
		index=0
		for url in self.url_list:
		
			temp=crawer(url,str(index))
			temp.start()
			index+=1
			
#x=Spider("https://tieba.baidu.com/f?ie=utf-8&kw=%E4%BC%AA%E5%A8%98")
x=Spider("https://tieba.baidu.com/f?ie=utf-8&kw=%E5%A5%B3%E8%A3%85%E5%AD%90&fr=search")
x.StartDownloading()

		
