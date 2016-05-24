#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pexpect
import sys
import os

def usage():
	'''
	1. set variable password for current shell
	] export password='your_password'

	2. run this script
	] chmod u+x ssh.py
	] ./ssh.py username@example.com

	3. done
	'''
	print('''
	Usage:
	  ./ssh.py user@example.com

	Note:
	  We use default sshd port 22.
	''')

def login():
	# get password
	password = os.environ['password']
	cmd = 'ssh %s' % sys.argv[1]

	# login server
	ssh = pexpect.spawn(cmd)
	patterns = [
		'.*password:',
		'.*continue connecting (yes/no)?',
		pexpect.TIMEOUT
	]
	while True:
		index = ssh.expect(patterns)
		if index == 0:
			break
		elif index == 1:
			ssh.sendline('yes')
			ssh.expect('.*password:')
			break
		else:
			pass
	ssh.sendline(password)
	ssh.interact()

def main():
	if len(sys.argv) < 2:
		usage()
		sys.exit(1)
	login()

if __name__ == '__main__':
	main()
