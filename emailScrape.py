#!/usr/bin/python

import sys
import urllib2
import re
import fileinput

def getAddress(url):
	http = "http://"
	https = "https://"

	if http in url:
		return url
	elif https in url:
		return url
	else:
		url = "http://" + url
		return url

def parseAddress(url):
	try:
		website = urllib2.urlopen(getAddress(url))
		html = website.read()

		addys = re.findall('''[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?''', html, flags=re.IGNORECASE)

		print addys
                f = open('output.txt', 'a+')
                f.write(str(addys) + "\n")
                f.close

	except urllib2.HTTPError, err:
		print "Cannot retrieve URL: HTTP Error Code: ", err.code
	except urllib2.URLError, err:
		print "Cannot retrive URL: " + err.reason[1]

def execute():
        for line in fileinput.input():
            parseAddress(line)

### MAIN

def main():
	execute()

main()
