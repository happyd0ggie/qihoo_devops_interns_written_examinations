#!usr/bin/env python3

import os
import sys
import re

access_log = None
ip_info = {}

def usage():
	'''
	./log_cutting.py /path/to/access_log
	return json format data
	'''
	print('''
	Usage:
	  ./log_cutting.py /path/to/access_log
	''')

def get_ip_count():
	global access_log
	global ip_info

	cmd = "cat %s | grep -Eio '^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | sort | uniq -c > ip_count.dat" % access_log
	os.system(cmd)
	with open('ip_count.dat', 'r') as f:
		for line in f:
			tmp = {}
			tmp['access_count'] = int(line.split()[0])
			tmp['access_time'] = []
			ip_info[line.split()[1]] = tmp

def get_access_time():
	global access_log
	global ip_info

	for ip in ip_info.keys():
		cmd = "grep -Ei '%s' %s | grep -Eio '[0-9]{4}\:[0-9]{2}\:[0-9]{2}\:[0-9]{2}' > %s_access_time" % (ip, access_log, ip)
		os.system(cmd)
		with open('%s_access_time' % ip, 'r') as f:
			for line in f:
				ip_info[ip]['access_time'].append(line.strip('\n'))

def get_client():
	pass

def main():
	global access_log
	if len(sys.argv) < 2:
		usage()
		sys.exit(1)
	access_log = sys.argv[1]
	get_ip_count()
	print(ip_info)
	get_access_time()
	print(ip_info)
	os.system('rm -f *_access_time 1>/dev/null 2>&1')
	os.system('rm -f ip_count.dat 1>/dev/null 2>&1')

if __name__ == '__main__':
	main()
