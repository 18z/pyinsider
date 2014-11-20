import os
import time
import commands

from pymongo import MongoClient
from ConfigParser import SafeConfigParser

result = 1

client = MongoClient()
database = client['mydb']
collection = database['name']


parser = SafeConfigParser()
parser.read('insider.conf')

ip = parser.get('IP_ADDR', 'ip[1]')
cmd = "ping "+ ip +" -c 1| grep -E -o '[0-9]+ received' | cut -f1 -d' '"
#cmd = "ping 9.8.8.8 -c 1| grep -E -o '[0-9]+ received' | cut -f1 -d' '"

print commands.getoutput(cmd)

if  int(commands.getoutput(cmd)) == int(result) :
	print "up"
	item = { "ip" : ip, "status" : "down"}
	collection.insert(item)
else:
	print "down"
	item = { "ip": ip, "status" : "up" }
        collection.insert(item)
