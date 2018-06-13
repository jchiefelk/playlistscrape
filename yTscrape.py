#
#   Scrapes Video Links from user Playlist
#   and Tests Youtube functionality on Google Chrome
#   Also Downloads audio using youtube-dl
#
#
import os,sys,time,unittest,bs4
import urllib.request,urllib.response, urllib.error
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
#
# Classes 
#
#
# Selenium for Browser Automation
class SelTest(unittest.TestCase):

	def setUp(self):
			self.driver=webdriver.Firefox()

	def test_search_in_python_org(self):
            # Open Browser
        	driver = self.driver
        	driver.get("https://www.youtube.com/playlist?list=PLIQGt7Pv8OM9waKZbKgXBofPfrJWi7a5T")
        	
        	

	def tearDown(self):
       	 	self.driver.close()

# Beautiful Soup for Scrpaing Web Data and youtube-dl for downloading mp3
class SoupScrape:

    link_list = []

   # Scrape video links 
    def GetLinks(self):
        #
        startpage = urllib.request.urlopen(arg1)
        soup = BeautifulSoup(startpage.read())
        table = soup.find('table', {'class': 'pl-video-table'})
        links = table.findAll('a')
        index = 0
        for link in links:
            fullLink = link.get('href')
            if fullLink[0] == '/' and fullLink[1]=='w' and fullLink[2]=='a' and fullLink[3]=='t':
                # print(fullLink)
                self.link_list.append(fullLink)

          
    
    def Download(self):
        #
        # First get rid of redundant links
        #
        unique_list =[]
        for x in range(0,len(self.link_list)-1):

            if self.link_list[x] != self.link_list[x+1]:
                unique_list.append((self.link_list[x]))
                unique_list.append((self.link_list[x+1]))

        # Download Tunes 
        #        
        for x in range(0,len(unique_list)):

            url = 'http://www.youtube.com' + unique_list[x]
            os.system('youtube-dl -x --extract-audio --audio-format mp3 ' + url)


# Main Program
# class RipScrape():

if __name__ == "__main__":

    arg1 = sys.argv[1]
    mp3fetch = SoupScrape()
    mp3fetch.GetLinks()
    thread1 = Thread(mp3fetch.Download())
    thread2 = Thread(unittest.main(argv=['mytestapp']))
    thread1.start()
    thread2.start()
   
