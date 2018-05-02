#!/usr/bin/python

import httplib

'''
This module takes in the user provided headers like user agent 
and makes an request to the server using httplib. This way the server can manipulate 
the response based on the request header.
'''


h = "www.infiniteskills.com"

req = httplib.HTTP(h)
req.putrequest("GET", "/")
req.putheader("Host", h)
req.putheader("User-Agent", "Garbage browser: 5.6")
req.putheader("My-Header", "My value")
req.endheaders()
req.send("")

statusCode, statusMsg, headers = req.getreply()
print("Response: ", statusMsg)

