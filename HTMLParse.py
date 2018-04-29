#!/usr/bin/python

from HTMLParser import HTMLParser
import urllib2

class myParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if (tag == "input"):
            print("Found an input field ", tag)
            print(attrs)

url = "http://batchwebpagetest.edpl.us/"
request = urllib2.Request(url)
handle = urllib2.urlopen(request)
parser = myParser()
parser.feed(handle.read())