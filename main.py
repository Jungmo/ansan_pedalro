# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import string
import urllib2

dict = {}
url='http://www.pedalro.kr/station/station.do?method=stationState&menuIdx=st_01'# + str(page)

for line in urllib2.urlopen(url):
	if "			title : " in line :
		s = line.lstrip()
		s = s.lstrip("title : '")
		s = s.rstrip("\n")
		s = s.split("|")
		dict[s[0]] = s[3]

ts = time.strftime("%Y-%m-%d-%I:%M", time.localtime())
filename = str(ts) + ".csv"
f = open(filename, "w")

for i in dict.keys():
	f.write(str(i) +","+ str(dict[i]))
	f.write("\n")

