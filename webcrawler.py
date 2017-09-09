# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import re
print ('This program is for web crawl and is specifically designed for the online forum' + " http://forum.iask.ca/")

addressList = ['http://forum.iask.ca/forums/埃德蒙顿.19/',
                'http://forum.iask.ca/forums/温哥华.14/',
               'http://forum.iask.ca/forums/多伦多.15/',
               'http://forum.iask.ca/forums/卡尔加里.13/',
               'http://forum.iask.ca/forums/工作求职.98/',
               'http://forum.iask.ca/forums/求学深造.36/',]
baseurl = addressList[0]
keyword = []
key = ""
print('Enter the key word you want to search(enter "q" if done):')
while key != 'q':
    key = raw_input().decode('utf-8')
    keyword.append(key)
keyword.remove('q')
exclu_word = ('min')
print ('searching... ')
root_url = "http://forum.iask.ca/"
for index in range(0,5):
  baseurl = addressList[index]
  print('now searching in the link: ' + baseurl)
  r = urllib2.Request(baseurl)
  resp = urllib2.urlopen(r)
  txt = resp.read()
  soup = BeautifulSoup(txt,"html.parser")
  d = soup.find('span',{'class':'pageNavHeader'})
  end = d.text
  endpage = re.search(u'共 (\d+)',end)
  print('There are totally ' + endpage.groups(1)[0] + ' pages to be searched.' )
  for page in range(1, int(endpage.groups(1)[0])):
      url = baseurl+'page-'+str(page)
      request = urllib2.Request(url)
      response = urllib2.urlopen(request)
      text = response.read()
      soup = BeautifulSoup(text,"html.parser")
      d = soup.find('span',{'class':'pageNavHeader'})
      end = d.text
      pattern = re.search(u'共 (\d+)',end)
      for link in soup.find_all('a',{'class':'PreviewTooltip'}):
          targetText = link.text.lower()
          if any(key in targetText for key in keyword) and all(exc not in targetText for exc in exclu_word):
              print("--------------------------------------------------------------")
              print(link.text+"\n" +
                    root_url+link['href'])