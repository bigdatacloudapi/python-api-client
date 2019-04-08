import requests
import re
import json

class Client:
	def __init__(
		self,
		apiKey,
		nameSpace='data',
		server='api.bigdatacloud.net'
		):
		self.apiKey=apiKey
		self.nameSpace=nameSpace
		self.server=server

	def __getattr__(self,p):
         def mm(params):
         	def conversion(m):
         		return "-"+m.group(1).lower()

         	key = re.sub('([A-Z])',conversion,p)
         	segs = key.split('-')
         	method = segs.pop(0).upper()

         	return self.communicate('-'.join(segs),method,params)
         return mm

	def communicate(self,endpoint,method,payload):
		url='https://'+self.server+'/'+self.nameSpace+'/'+endpoint

		headers={'X-BDC-Key':self.apiKey}

		if (method=='POST' or method=='PUT' or method=='PATCH'):
			headers['content-type']='application/x-www-form-urlencoded'

		r=getattr(requests,method.lower())(url,headers=headers,params=payload,data=payload)

		return [r.json(),r.status_code]