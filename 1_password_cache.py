#!/usr/bin/env python3

from pexpect import spawn
import sys
import os

# determine arguments number
def usage():
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
