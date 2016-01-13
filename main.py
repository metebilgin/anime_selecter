#!/usr/bin/python

import urllib
import urllib2
from bs4 import BeautifulSoup
url = 'http://www.animefreak.tv/'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
soup = BeautifulSoup(the_page, 'html.parser')
for link in soup.find_all('li', attrs={'class':'collapsed first last'}):
	urltmp = url + link.find("a").get('href')
	req = urllib2.Request(urltmp, data)
	response = urllib2.urlopen(req)
	the_page_temp = BeautifulSoup(response.read(), 'html.parser')
	if (float(the_page_temp.find("span", attrs={'class':'average-rating'}).find("span").getText()) >= 4.0):
		print the_page_temp.title.getText(), the_page_temp.find("span", attrs={'class':'average-rating'}).find("span").getText()
