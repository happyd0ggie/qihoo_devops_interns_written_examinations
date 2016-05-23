#!/usr/bin/env python3

import pexpect
import os

def push():
	password = os.environ['github_password']
	cmd = 'git push'
	git = pexpect.spawn(cmd)
	while True:
		index = git.expect(['Username', pexpect.TIMEOUT])
		if index == 0:
			break
		elif index == 1:
			pass
		else:
			pass
	git.sendline('shengdexiang')
	git.expect('Password.*')
	git.sendline(password)
	git.interact()

def main():
	push()

if __name__ == '__main__':
	main()
