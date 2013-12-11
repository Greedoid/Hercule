import requests
import urllib2
import sys


class Request:

	def __init__(self, api_key):
		self.prior = 'http://prod.api.pvp.net/api/lol/'
		self.vers = '/v1.1'
		self.posterior = '?api_key=' + str(api_key)

	def get_id_from_name(self, name, region='na'):
		request_string = self.prior + region + self.vers + '/summoner/by-name/' + name + self.posterior
		return self.make_request(request_string)['id']

	def get_level_from_name(self, name, region='na'):
		request_string = self.prior + region + self.vers + '/summoner/by-name/' + name + self.posterior
		return self.make_request(request_string)['summonerLevel']

	def make_request(self, request_string):
		req = urllib2.Request(request_string)
		response = urllib2.urlopen(req)
		return eval(response.read())
