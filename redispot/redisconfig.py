#!/usr/bin/env python

import sys
import itertools
import fileinput
from ConfigParser import SafeConfigParser

DELIMITER = "\r\n"

class rediscommands():

#Code from redis_protocol parser by Young King modified :)
	@staticmethod
	def encode(res):
	    #"Pack a series of arguments into a value Redis command"
	    result = []
	    result.append("*")
	    result.append(str((len(res)-2)*2+3*2+1)) #Change required
	    result.append(DELIMITER)
	    for arg in res:
	    	for test in arg:
		        result.append("$")
		        result.append(str(len(test)))
		        result.append(DELIMITER)
		        result.append(test)
		        result.append(DELIMITER)
		"".join(result)
	    return "".join(result)
	@staticmethod
	def encode_new(res):
	    "Pack a series of arguments into a value Redis command"
	    result = []
	    result.append("*")
	    result.append(str(len(res)))
	    result.append(DELIMITER)
	    for arg in res:
		result.append("$")
		result.append(str(len(arg)))
		result.append(DELIMITER)
		result.append(arg)
		result.append(DELIMITER)
	    return "".join(result)
	@staticmethod
	def encode_keys(res):
	    result = []
	    result.append("*")
	    result.append(len(res))
	    result.append(DELIMITER)
	    for arg in res:
	        result.append("$")
	        result.append(str(len(arg)))
	        result.append(DELIMITER)
	        result.append(arg)
	        result.append(DELIMITER)
	    return "".join(result)
	@staticmethod
	def parse_config():
	#Parses the configuration file removes blank lines , converts to redis protocol format to be sent to client
		l=[]
		output=open("redispot/config/redis2.conf","w")
		input=open('redispot/config/redis.conf','r')
		data=input.readlines()
		for i in data:
			if i.startswith('#'):
				pass
			else:
				output.write(i)
		output.close()
		input.close()
		for line in fileinput.FileInput("redispot/config/redis2.conf",inplace=1):
		    if line.rstrip():
		        print line
		input=open('redispot/config/redis2.conf','r')
		data=input.readlines()
		for i in data:
			if len(i.strip().split()) > 1:
				l.append(i.strip().split())
		print len(l)
		red_enc_data=rediscommands.encode(l)
		return red_enc_data
	@staticmethod
	def parse_info(time,connections,cmds):
		s=[]
		#Simulation of INFO command in Redis (enables the user to add options)
		parser = SafeConfigParser()
		parser.read('redispot/config/info')
		print "test"
		parser.set('info','uptime_in_seconds',str(time))
		parser.set('info','total_connections_received',str(connections))
		parser.set('info','total_commands_processed',str(cmds))
		with open('redispot/config/info', 'wb') as configfile:
		    parser.write(configfile)
		parser.read('info')
		someinfo=parser.items('info')
		for i in someinfo:
			 s.append(":".join(i))
		data=rediscommands.encode_new(s)
		return data



"""
d={}

for i in l:
	d.update(dict(itertools.izip_longest(*[iter(i)] * 2, fillvalue="")))

print d
"""
