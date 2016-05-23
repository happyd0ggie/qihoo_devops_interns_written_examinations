#!/usr/bin/env python3

import os
import sys

def usage():
	'''
	1. stop a job temporary
	] ./cron_ctrl.py jobname1 --stop

	2. start a job
	] ./cron_ctrl.py jobname1 --start

	3. list a job detail
	] ./cron_ctrl.py jobname1 --list
	'''
	print('''
	Usage:
	  ./cron_ctrl.py jobname options

	Options:
	  --stop	stop job temporary
	  --start	start job
	  --list	list job detail
	''')

def save_alljob():
	cmd = 'crontab -l > /tmp/crontab_orgin.job'
	os.system(cmd)

def exclude(jobname):
	cmd = 'crontab -l | grep -iv %s > /tmp/crontab_%s_excluded.job' % (
			jobname, jobname)
	os.system(cmd)

def start_job(jobname):
	print('starting job [%s]...' % jobname, end = ' ')
	cmd = 'crontab < /tmp/crontab_orgin.job 1>/dev/null 2>&1'
	os.system(cmd)
	print('OK')

def stop_job(jobname):
	print('stopping job [%s]...' % jobname, end = ' ')
	exclude(jobname)
	cmd = 'crontab -r 1>/dev/null 2>&1'
	os.system(cmd)
	cmd = 'crontab < /tmp/crontab_%s_excluded.job 1>/dev/null 2>&1' % jobname
	os.system(cmd)
	os.system('rm -f /tmp/crontab_%s_excluded.job 1>/dev/null 2>&1' 
			% jobname)
	print('OK')

def list_job(jobname):
	cmd = 'crontab -l | grep -i %s 2>/dev/null' % jobname
	os.system(cmd)

def parser_parameter():
	if len(sys.argv) != 3:
		usage()
		sys.exit(1)
	jobname = sys.argv[1]
	command = sys.argv[2].replace('-', '')

	if command == 'stop':
		save_alljob()
		stop_job(jobname)
	elif command == 'start':
		start_job(jobname)
	elif command == 'list':
		list_job(jobname)
	else:
		pass

def main():
	parser_parameter()

if __name__ == '__main__':
	main()
