#!/usr/bin/env python3

from pexpect import spawn
import sys
import os

# determine arguments number
def usage():
	'''
	1. set variable password for current shell
	] export password='your_password'

	2. run this script
	] chmod u+x ssh.py
	] ./ssh.py username@example.com

	3. done
	'''
	print('./ssh.py user@example.com')
	sys.exit(1)

def login():
	# get password
	password = os.environ['password']
	cmd = 'ssh %s' % sys.argv[1]

	# login server
	ssh = spawn(cmd)
	ssh.expect('.*password:')
	ssh.sendline(password)
	ssh.sendline('\n')
	ssh.interact()

def main():
	if len(sys.argv) < 2:
		usage()
	login()

if __name__ == '__main__':
	main()
