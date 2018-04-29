#!/usr/bin/python

import httplib

host = "www.google.com"

'''
This module defines classes which implement the client side of the HTTP and HTTPS protocols.
the module urllib uses it to handle URLs that use HTTP and HTTPS.
'''
# Instantiate the HTTP class with give host address
req = httplib.HTTP(host)

# sends a line to the server consisting of the request string, the selector string, and the HTTP version
req.putrequest("HEAD", "/")

# sends a line to the server consisting of the header, a colon and a space, and the first argument
req.putheader("Host", host)

# Send a blank line to the server, signalling the end of the headers
req.endheaders()

# Send data to the server. This should be used directly only after the endheaders()
req.send("")

# fetch reply from server and assign values respectively
statusCode, statusMsg, headers = req.getreply()

# Print the status code
print("Status: ", statusCode)
