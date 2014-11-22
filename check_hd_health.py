import os
import time
import commands

from pymongo import MongoClient
from ConfigParser import SafeConfigParser

result=""

client = MongoClient()
database = client['mydb']
collection = database['hdhealth']

parser = SafeConfigParser()
parser.read('insider.conf')

hd = parser.get('HD_DEVICE', 'hd')
cmd = "smartctl -q errorsonly -H -A -a " + hd

print commands.getoutput(cmd)

if  commands.getoutput(cmd) == result :
	print "good"
	item = { "hd" : hd, "status" : "good"}
	collection.insert(item)
else:
	print "better watch out"
	item = { "hd": hd, "status" : "better watch out" }
        collection.insert(item)
