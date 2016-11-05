import urllib2
import json
import subprocess
import socket


def get_ip():
	ip_address = socket.gethostbyname(socket.gethostname())
	return ip_address

def get_data(api_id,api_key):

	ip_address = get_ip()
	
	action = 'employers'
	query = 'pharmaceuticals'
	base_url = 'http://api.glassdoor.com/api/api.htm?'
	useragent = 'Mozilla/%2F4.0'

	url = '{5}v=1&format=json&t.p={0}&t.k={1}&action={3}&q={4}&userip={2}&useragent={6}'.format(api_id,api_key,ip_address,action,query,base_url,useragent)
	hdr = {'User-Agent': 'Mozilla/5.0'}

	req = urllib2.Request(url,headers=hdr)
	response = urllib2.urlopen(req)
	data = response.read()

	print type(data)

get_data()


