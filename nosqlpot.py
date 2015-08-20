#!/usr/bin/env python
#NoSQL Honeypot FrameWork Copyright 2015 Francis Alexander
#This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import redispot
from redispot import redisdeploy
from couchpot import couchdeploy

def banner():
	print """
		 /$$   /$$          /$$$$$$$
		| $$$ | $$        | $$__  $$
		| $$$$| $$ /$$$$$$| $$  \ $$/$$$$$$
		| $$ $$ $$/$$__  $| $$$$$$$/$$__  $$
		| $$  $$$| $$  \ $| $$____| $$  \ $$
		| $$\  $$| $$  | $| $$    | $$  | $$
		| $$ \  $|  $$$$$$| $$    |  $$$$$$/
		|__/  \__/\______/|__/     \______/   v0.1(beta)


Usage : nopo.py -deploy redis

"""

def main():
	port=0
	out=""
	parser = argparse.ArgumentParser(description='Nosql HoneyPot Framework')
	parser.add_argument('-deploy','--deploy', help='Select Deploy Server', required=False)
	parser.add_argument('-port','--port', help='Port', required=False)
	parser.add_argument('-config','--config', help='Specify Configuration File', required=False)
	parser.add_argument('-out','--out', help='Specify Output To (stdout/file)', required=False)
	args = vars(parser.parse_args())
	if args['port']:
		port=int(args['port'])
	if args['out']:
		out=args['out']
	if args['deploy'] == 'redis':
		if port==0 and out=="":
			redisdeploy.reddeploy()
		else:
			redisdeploy.reddeploy(port,out)
	if args['deploy'] == 'couch':
		couchdeploy.coudeploy()
			

if __name__ == "__main__":
    banner()
    main()
