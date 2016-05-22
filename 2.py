#!/usr/bin/env python

import os
import re

ifconfig_output_filtered = ''
device_names = None
ip_info = {}
# get ifconfig output
def get_ifconfig_output():
	global ifconfig_output_filtered
	os.system('ifconfig > ifconfig.output')
	with open('ifconfig.output', 'r') as f:
		for line in f:
			if 'eth' in line or 'inet' in line:
				ifconfig_output_filtered += line

# get device name
def get_device_name():
	global ifconfig_output_filtered
	global device_names
	device_names = re.findall(r'eth[0-9]', ifconfig_output_filtered)

# get device ip address
def get_device_ip():
	global ifconfig_output_filtered
	global device_names
	global ip_info

	ip_pattern = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
	ip_addresses = [ip for ip in re.findall(ip_pattern, ifconfig_output_filtered) if '255' not in ip and ip != '127.0.0.1']
	for i in range(len(device_names)):
		ip_info[device_names[i]] = ip_addresses[i]

def main():
	get_ifconfig_output()
	get_device_name()
	get_device_ip()
	print(ip_info)

if __name__ == '__main__':
	main()
