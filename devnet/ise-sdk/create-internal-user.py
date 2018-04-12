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
# Usage: create-internal-user.py <ISE host> <ERS user> <ERS password>     #
#  <username> <first name> <last name> <password> <email> <expiry date>   #
###########################################################################

import http.client
import base64
import ssl
import sys

#parameters
name = sys.argv[4]  # "chris"
first = sys.argv[5]  # "Chris"
last = sys.argv[6]  # "Colombus"
passwd = sys.argv[7]  # "Password1"
email = sys.argv[8]  # "chris@cisco.com"
expiry_date = sys.argv[9]  # "2017-01-29"

# host and authentication credentials
host = sys.argv[1] # "10.20.30.40"
user = sys.argv[2] # "ersad"
password = sys.argv[3] # "Password1"


conn = http.client.HTTPSConnection("{}:9060".format(host), context=ssl.SSLContext(ssl.PROTOCOL_TLSv1))

creds = str.encode(':'.join((user, password)))
encodedAuth = bytes.decode(base64.b64encode(creds))

req_body_json = """  {{
    "InternalUser" : {{
        "name" : "{}",
        "enabled" : true,
        "email" : "{}",
        "password" : "{}",
        "firstName" : "{}",
        "lastName" : "{}",
        "changePassword" : true,
        "expiryDateEnabled" : true,
        "expiryDate" : "{}",
        "enablePassword" : "{}",
        "customAttributes" : {{
        }},
        "passwordIDStore" : "Internal Users"
    }}
}}
""".format(name,email,passwd,first,last,expiry_date,passwd)

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'authorization': " ".join(("Basic",encodedAuth)),
    'cache-control': "no-cache",
    }

conn.request("POST", "/ers/config/internaluser/", headers=headers, body=req_body_json)

res = conn.getresponse()
data = res.read()

print("Status: {}".format(res.status))
print("Header:\n{}".format(res.headers))
print("Body:\n{}".format(data.decode("utf-8")))
