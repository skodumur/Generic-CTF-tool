#!/usr/bin/python


from HTMLParser import HTMLParser
import urllib2

'''
This module makes an get request to the url provided using urllib2 library
then parses and prints the retrieved html using the myParser class
'''
class myParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if (tag == "input"):
            print("Found an input field ", tag)
            print(attrs)

url = "http://google.com/"
request = urllib2.Request(url)
handle = urllib2.urlopen(request)
parser = myParser()
parser.feed(handle.read())