#!/usr/bin/python

import urllib2

'''
This module makes an proxy call to the given url with the 
through the provided proxy details using the python's urllib2 library
'''
proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
handle = urllib2.urlopen('http://www.microsoft.com')

print(handle.read())

