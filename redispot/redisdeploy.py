#!/usr/bin/env python
from twisted.python import log
from twisted.internet.protocol import Protocol, ServerFactory
from twisted.internet import reactor
import redis_protocol
import sys
import fakeredis
import time
from redisconfig import rediscommands

### Protocol Implementation of NoPo-Redis Server

global con_count
con_count = 0

global time_elapse,cmd_count
time_elapse = time.time()

cmd_count = 0

class RedisServer(Protocol):
    
    connectionNb = 0
    
    def __init__(self):
        pass
    
    def connectionMade(self):
        self.connectionNb += 1
        print "New connection: %s from %s"%(format(self.connectionNb),self.transport.getPeer().host)

    #Handling of Client Requests , Data 
    def dataReceived(self, rcvdata):
        cmd_count = 0   
        r = fakeredis.FakeStrictRedis()
        cmd_count = cmd_count + 1
        print "original data:"+str(rcvdata),
        #print "Data received:", str(redis_protocol.decode(rcvdata))
        try:
            data=redis_protocol.decode(rcvdata)
            command=" ".join(redis_protocol.decode(rcvdata))
            print str(command)
        except:
            data=rcvdata
	    command=rcvdata
        if command.lower == "quit":
            self.transport.loseConnection()

        else:
            if command.lower() == "ping" or rcvdata.find('PING') == 0:
                snddata = "+PONG\r\n"  
                #redis_protocol.encode("PONG crime")    
                #print redis_protocol.encode("PONG")
                self.transport.write(snddata) 
            elif command.lower() == "config get *" or rcvdata.find('config')==0:
                self.transport.write(rediscommands.parse_config())
            elif command.lower().startswith('set') and len(data) == 3:
                if r.set(data[1],data[2]):
                    self.transport.write("+OK\r\n")
            elif command.lower().startswith('get') and (len(data) == 2 or len(data) == 1):
                if r.get(data[1]):
                    s=r.get(data[1])
                    self.transport.write('+"%s"\r\n'%(s))
            elif command.lower().startswith('info'):
                diff = round(time.time() - time_elapse) % 60
                self.transport.write(rediscommands.parse_info(diff,self.connectionNb,cmd_count))
            elif command.lower().startswith('keys') and (len(data) == 2 or len(data) == 1):
                if r.keys() and (data[1] in r.keys() or data[1] == '*') :
                    keys=r.keys()
                    self.transport.write(rediscommands.encode_keys(keys))
                elif len(r.keys()) == 0:
                    self.transport.write("+(empty list or set)\r\n")
                else:
                    self.transport.write("-ERR wrong number of arguments for 'keys' command\r\n")
            else:
                self.transport.write("-ERR unknown command '%s'\r\n"%(data[0]))
    def connectionLost(self, reason):
        self.connectionNb -= 1
        print "End connection: ", reason.getErrorMessage()


class RedisServerFactory(ServerFactory):
    
    protocol = RedisServer

def reddeploy(port=6109,method='stdout'):
    if method != 'stdout':
	log.startLogging(open('redis.log', 'a'))  
    else:
	log.startLogging(sys.stdout)
    reactor.listenTCP(port, RedisServerFactory())
    reactor.run()
