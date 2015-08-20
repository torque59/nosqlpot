import cherrypy
import uuid
import httplib, urllib
import os.path
import ConfigParser	


global config
config = ConfigParser.ConfigParser()
config.read("couchpot/couch.conf")

class Couchpot:

	
	def index(self):
	# Connection Test 
		#return '''{"couchdb":"Welcome","uuid":"%s","version":"1.6.1","vendor":{"name":"Ubuntu","version":"14.04"}}\n''' % uuid.uuid1().hex
		return config.get('main','index')%(uuid.uuid1().hex)

	index.exposed = True

	def _uuids(self):
		return '{"uuids":["%s"]}'%(uuid.uuid1().hex)
	_uuids.exposed= True

	def _all_dbs(self):
		return config.get('main','dbs')
	_all_dbs.exposed = True

	def _cp_dispatch(self, vpath):
       		if len(vpath) == 1:
            		cherrypy.request.params['name'] = vpath.pop()
            		return vpath

	def newdb(self):
	#new database creation
		if cherrypy.request.method == 'GET':
			return '''{"ok":true}\n'''

	newdb.exposed = True

def coudeploy():

	serverconf = os.path.join(os.path.dirname(__file__), 'server.conf')
	def error_404(status, message, traceback, version):
		return '''{"error":"not_found","reason":"no_db_file"}'''
	error_404.exposed = True

	cherrypy.config.update({'error_page.404':error_404})
	access_log = cherrypy.log.access_log
	cherrypy.quickstart(Couchpot(), config=serverconf)


