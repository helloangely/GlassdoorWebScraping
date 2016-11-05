import urllib2
import json
import socket
import os
from Queue import Queue
from pprint import pprint

def get_ip():
	# use socket to grab ip address, required for url 
	ip_address = socket.gethostbyname(socket.gethostname())
	return ip_address

def get_enviorn_key_id():
	'''
	Set your enviornment variables in terminal:

	$ export GLASSDOOR_API_ID="YOUR_API_ID"
	$ export GLASSDOOR_API_KEY="YOUR_API_KEY"
	'''
	api_id = os.getenv('GLASSDOOR_API_ID')
	api_key = os.getenv('GLASSDOOR_API_KEY')

	return api_id,api_key

def get_data(jobTitle,ip_address,api_id,api_key):
	'''
	Get next job progression
	'''

	action = 'jobs-prog'
	query = 'pharmaceuticals'
	base_url = 'http://api.glassdoor.com/api/api.htm?'
	useragent = 'Mozilla/%2F4.0'
	countryId = '1'


	url = '{5}v=1&format=json&t.p={0}&t.k={1}&action={3}&q={4}&userip={2}&useragent={6}&countryId={7}&jobTitle={8}'.format(api_id,api_key,ip_address,action,query,base_url,useragent,countryId,jobTitle)
	hdr = {'User-Agent': 'Mozilla/5.0'}

	req = urllib2.Request(url,headers=hdr)
	response = urllib2.urlopen(req)
	json_data = json.load(response) 
	result = json_data['response']['results']

	# uncomment lines below to return highest frequency of next career option
	# most_freq = result[0]
	# return most_freq

	max_salary = max(result, key=lambda s:s['medianSalary'])
	return max_salary

def replace_space(job_title):
	# formatting title for url
	return job_title.replace(' ', '%20')

def get_results(job_titles,ran=4):

	ip_address = get_ip()
	api_id,api_key = get_enviorn_key_id()

	# initialize dictionary and populate q
	q = Queue()
	res = {}
	for i in job_titles:
		res[i]=[]
		replaced_i = replace_space(i)
		q.put(replaced_i)

	# get new data and populate q
	for i in range(ran):
		for job in job_titles:
			most_freq_job = get_data(q.get(),ip_address,api_id,api_key)
			next_job_title = most_freq_job['nextJobTitle']
			replaced = replace_space(next_job_title)
			q.put(replaced)
			res[job].append(most_freq_job)
	
	return res

def main():
	job_titles=['engineer','systems engineer','safety representative','web applications developer','electrical engineer','journalist','marketing analyst', 'software engineer', 'architect']
	num_runs=4
	final_res = get_results(job_titles,num_runs)
	pprint(final_res)

main()






