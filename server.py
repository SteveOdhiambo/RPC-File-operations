import os
import sys
import rpyc
#path = '/home/amolo/Projects/School/OS/OS Assignment/server.py/'
path = os.path.abspath(__file__)[:-9] + 'files/'
#00-List the files
#01-Create A File
#02-View a file
#03-Delete the file
class FileService(rpyc.Service):

	""" All methods in this class should begin with
	the 'exposed_' prefix so as to be able to 
	be consumed by the client directly """

	def exposed_view_files(self):
		desktop = []
		files = os.listdir(path)
		for filen in files:
			desktop.append(filen)

		return desktop


	def exposed_create_file(self, filename, content):
		try:
			with open(path + filename, 'w') as f:
				f.write(content)
				return '01'
		except:
			return '01-Failed'


	def exposed_read_file(self, filename):
		try:
			with open(path + filename, 'r') as f:
				return f.read()
				

		except:
			return "02-Failed"


	def exposed_delete_file(self, filename):
		os.remove(path + filename)

		return "Deleted"



if __name__ == '__main__':
	from rpyc.utils.server import ThreadedServer
	t = ThreadedServer(FileService, port = 6500 )
	t.start()