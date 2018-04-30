from pexpect import pxssh
import getpass

try:
	s=pxssh.pxssh()
	hostname = 'xxx.xxx.x.x'
	username = 'username'
	password = 'password'
	
	s.login(hostname,username,password)
	s.sendline('cd path_to_directory')
	s.prompt()
	print s.before
	s.sendline('pwd') #check if the path is changed
	s.prompt()
	print s.before
	s.sendline('cat filename.txt')
	s.prompt() 
	print s.before
	
	s.logout()

except pxssh.ExceptionPxssh, e:
	print "Fail"
	print str(e)
	

