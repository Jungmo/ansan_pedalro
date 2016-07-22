# -*- coding: utf-8 -*-
import time
import string
import urllib2
import argparse
import sys
parser = argparse.ArgumentParser()

parser.add_argument('--interval', type=int, default='300', help='seconds')
args = parser.parse_args()

dict = {}
url = 'http://www.pedalro.kr/station/station.do?method=stationState&menuIdx=st_01'

ts = time.strftime("%Y-%m-%d-%I-%M", time.localtime())
filename = str(ts) + ".csv"
f = open(filename, "w")
count = 1
f.write("ts,")
while True:
    print("%d번째 저장입니다.") % (count)
    ts = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())

    for line in urllib2.urlopen(url):
        if "			title : " in line:
            s = line.lstrip()
            s = s.lstrip("title : '")
            s = s.rstrip("\n")
            s = s.split("|")
            dict[s[0]] = s[3]
    if count == 1:
        for i in dict.keys():
            f.write(str(i) + ",")
        f.write("\n")
        f.write(ts + ",")
        for i in dict.keys():
            f.write(str(dict[i]) + ",")
        f.write("\n")

    else:
        f.write(ts + ",")
        for i in dict.keys():
             f.write(str(dict[i]) + ",")
        f.write("\n")

    count += 1
    dict.clear()
    time.sleep(args.interval)

