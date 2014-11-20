import os
import time
import commands
from ConfigParser import SafeConfigParser

result = 1

parser = SafeConfigParser()
parser.read('insider.conf')

ip = parser.get('IP_ADDR', 'ip[2]')
#cmd = "ping "+ ip +" -c 1| grep -E -o '[0-9]+ received' | cut -f1 -d' '"
cmd = "ping 9.8.8.8 -c 1| grep -E -o '[0-9]+ received' | cut -f1 -d' '"

print commands.getoutput(cmd)

if  int(commands.getoutput(cmd)) == int(result) :
	print "up"
else:
	print "down"
