# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import string
import urllib2
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--interval', type = int, default='300', help='seconds')
args = parser.parse_args()

dict = {}
url='http://www.pedalro.kr/station/station.do?method=stationState&menuIdx=st_01'# + str(page)

ts = time.strftime("%Y-%m-%d-%I:%M", time.localtime())
filename = str(ts) + ".csv"
f = open(filename, "w")


while(1) 
	for line in urllib2.urlopen(url):
		if "			title : " in line :
			s = line.lstrip()
			s = s.lstrip("title : '")
			s = s.rstrip("\n")
			s = s.split("|")
			dict[s[0]] = s[3]

		for i in dict.keys():
		f.write(ts + ",")
		f.write(str(i) +","+ str(dict[i]))
		f.write("\n")
	
	time.sleep(args.interval)
