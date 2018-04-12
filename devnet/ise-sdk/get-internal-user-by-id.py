#!/usr/bin/env python

###########################################################################
#                                                                         #
# This script demonstrates how to use the ISE ERS internal users          #
# API  by executing a Python script.                                      #
#                                                                         #
# SECURITY WARNING - DO NOT USE THIS SCRIPT IN PRODUCTION!                #
# The script allows connections to SSL sites without trusting             #
# the server certificates.                                                #
# For production, it is required to add certificate check.                #
#                                                                         #
# Usage: get-internal-user-by-id.py <ISE host> <ERS user> <ERS password>  #
#  <user ID>                                                              #
###########################################################################

import http.client
import base64
import ssl
import sys

#parameters
user_id = sys.argv[4]  # "d83da9b6-6fd0-4704-bc37-69ceaaa5f633"

# host and authentication credentials
host = sys.argv[1] # "10.20.30.40"
user = sys.argv[2] # "ersad"
password = sys.argv[3] # "Password1"


conn = http.client.HTTPSConnection("{}:9060".format(host), context=ssl.SSLContext(ssl.PROTOCOL_TLSv1))

creds = str.encode(':'.join((user, password)))
encodedAuth = bytes.decode(base64.b64encode(creds))

headers = {
    'accept': "application/json",
    'authorization': " ".join(("Basic",encodedAuth)),
    'cache-control': "no-cache",
    }

conn.request("GET", "/ers/config/internaluser/{}".format(user_id), headers=headers)

res = conn.getresponse()
data = res.read()

print("Status: {}".format(res.status))
print("Header:\n{}".format(res.headers))
print("Body:\n{}".format(data.decode("utf-8")))