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
count = 1

while True:
    print("%d번째 저장입니다.") % (count)
    ts = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    str = ''

    for line in urllib2.urlopen(url):
        if "			title : " in line:
            s = line.lstrip()
            s = s.lstrip("title : '")
            s = s.rstrip("\n")
            s = s.split("|")
            dict[s[0]] = s[3]
    if count == 1:
        str += 'ts,' + ",".join(dict.keys()) + '\n'

    str += ts + "," + ",".join(dict.values()) + '\n'

    count += 1
    print(str)
    f = open(filename, "a")
    f.write(str)
    f.close()
    dict.clear()
    time.sleep(args.interval)
