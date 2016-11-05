import urllib2
import json
import socket
import os
from pprint import pprint

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
	'''
	Getting dev job progressionls
	'''

	ip_address = get_ip()

	api_id,api_key = get_enviorn_key_id()

	action = 'jobs-prog'
	query = 'pharmaceuticals'
	base_url = 'http://api.glassdoor.com/api/api.htm?'
	useragent = 'Mozilla/%2F4.0'
	countryId = '1'
	jobTitle= 'developer'


	url = '{5}v=1&format=json&t.p={0}&t.k={1}&action={3}&q={4}&userip={2}&useragent={6}&countryId={7}&jobTitle={8}'.format(api_id,api_key,ip_address,action,query,base_url,useragent,countryId,jobTitle)
	hdr = {'User-Agent': 'Mozilla/5.0'}

	req = urllib2.Request(url,headers=hdr)
	response = urllib2.urlopen(req)
	json_data = json.load(response) 

	pprint(json_data)
	


get_data()


