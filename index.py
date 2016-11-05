import urllib2
import json
import subprocess
import socket
import os


def get_ip():
	ip_address = socket.gethostbyname(socket.gethostname())
	return ip_address

def get_enviorn_key_id():
	'''
	Set your enviornment variables in a unix terminal:

	$ export GLASSDOOR_API_ID="YOUR_API_ID"
	$ export GLASSDOOR_API_KEY="YOUR_API_KEY"
	'''
	api_id = os.getenv('GLASSDOOR_API_ID')
	api_key = os.getenv('GLASSDOOR_API_KEY')

	return api_id,api_key

def get_data():

	ip_address = get_ip()

	api_id,api_key = get_enviorn_key_id()

	action = 'employers'
	query = 'pharmaceuticals'
	base_url = 'http://api.glassdoor.com/api/api.htm?'
	useragent = 'Mozilla/%2F4.0'

	url = '{5}v=1&format=json&t.p={0}&t.k={1}&action={3}&q={4}&userip={2}&useragent={6}'.format(api_id,api_key,ip_address,action,query,base_url,useragent)
	hdr = {'User-Agent': 'Mozilla/5.0'}

	req = urllib2.Request(url,headers=hdr)
	response = urllib2.urlopen(req)
	json_data = json.load(response) 

	print json_data

get_data()


