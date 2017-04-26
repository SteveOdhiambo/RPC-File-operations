import rpyc
from time import strftime, localtime
from sys import argv

def main():
	try:
		conn = rpyc.connect('localhost', port = 8000)
	except:
		print "Could not establish a connection to the server"
		return "Process Exited"

	#The MENU 
	print '''

	\ \      / /__| | ___ ___  _ __ ___   ___ 
	 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \
	  \ V  V /  __/ | (_| (_) | | | | | |  __/
	   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|

		What would you like to do ?

		1. View your files
		2.Create a new file in the server
		3.Read the contents of a file
		4.Delete a file

	'''
	#Option selector
	choice = raw_input('option -> ')
	if len(choice) > 0:
		choice = int(choice)
	else:
		print "You did not give us an option :-( "
		return "Process Exited"

#Options made by the user

	if choice == 1 : #If the user chooses option 1 --> 1. View your files
		ret = list(conn.root.exposed_view_files()) #Type-cast to return a standard Python List		
		if len(ret) == 0: #Empty list
			print "No files here..Yet"
			return "Process Exited"
		print "Here are your files: "
		for pos, item in zip(range(0, len(ret)), ret):
			print '{}). {}'.format(pos + 1, item)



	elif choice == 2:  #If the user chooses option 2 --> 2.Create a new file in the server
		print "Enter contents of the file and press Enter"
		file_content = raw_input(':-> ')
		if len(file_content) < 1: #If no content is captured.
			print "We cannot create an empty file"
			print "Put in some content"
			print "|| To exit enter '-99' and press enter ||"
			nc = raw_input(" >> ")
			if '-99' in nc: #Exiting process
				
				print '''
							   ___    _  _         
							  | _ )  | || |  ___   
							  | _ \   \_, | / -_)  
							  |___/  _|__/  \___|  
							_|"""""|| """"||"""""| 
							"`-0-0-'"`-0-0-'"`-0-0-' 

				'''

				return "Process Exited"
			else:
				file_content = nc
		f_name = raw_input("Give your file a name. > ") 
		if len(f_name) < 1: #No name was given for the file
			print "Empty string again ?. We have give it a name only the server can understand "
			f_name = strftime("%d-%m-%Y--%H:%M:%S", localtime()) #Empty will automatically name it according to date
			print "Look for a file by the name : {0}".format(f_name)
			print "Goodbye"

		if conn.root.exposed_create_file(f_name, file_content) == '01-Failed' :
			print "Ooops...Could not create file..Don't know why"

	elif choice == 3: #If the user chooses option 3 ---> 3.Read the contents of a file
		print "Which file do you want to read from ?"
		tl = list(conn.root.exposed_view_files())
		for pos, item in zip(range(0, len(tl)), tl):
			print '{}). - {}'.format(pos + 1, item)
		#Lets get a list of the files.
		
		#Hahaha (Simple arithmetic | Arrays)
		to_read = raw_input('> ') 
		to_read = int(to_read)
		to_read = to_read -1 
		#Hahaha
		print str(conn.root.exposed_read_file(tl[to_read]))

	elif choice == 4: #If the user chooses option 4 ---> 4.Delete a file
		print 'Which file would you like to delete ?'
		tl = list(conn.root.exposed_view_files()) #Gets a list of all existing files
		for pos, item in zip(range(0, len(tl)), tl):
			print '{}). {}'.format(pos + 1, item)
		#Lets get a list of the files.

		#Hahaha (Simple arithmetic | Arrays)
		to_delete = raw_input('> ')
		to_delete = int(to_delete)
		to_delete = to_delete -1 
		#Hahaha
		conn.root.exposed_delete_file(tl[to_delete])
		print "Deleted"



		print "Current List : "
		tl = list(conn.root.exposed_view_files())
		for pos, item in zip(range(0, len(tl)), tl):
			print '{}). {}'.format(pos + 1, item)
		

	else :
		"No option like that"


if __name__ == '__main__': #Runs only if client is not an import module
	main()
