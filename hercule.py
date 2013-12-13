import sys
import requests

class Request:

	def __init__(self, api_key):
		self.max_names = 40
		self.prior = 'http://prod.api.pvp.net/api/lol/'
		self.vers = '/v1.1'
		self.vers2 = '/v2.1'
		self.api_key = str(api_key)

	def get_id_from_name(self, name, region='na'):
		request_string = region + self.vers + '/summoner/by-name/' + name 
		return self.make_request(request_string)['id']

	def get_level_from_name(self, name, region='na'):
		request_string = region + self.vers + '/summoner/by-name/' + name 
		return self.make_request(request_string)['summonerLevel']

	def get_masteries_from_name(self, name, region='na'):
		request_string = region + self.vers + '/summoner/' + str(self.get_id_from_name(name, region)) + '/masteries' 
		raw = self.make_request(request_string)
		pages = []
		for page in raw['pages']:
			pages.append(page)
		return pages

	def get_current_masteries_from_name(self, name, region='na'):
		request_string = region + self.vers + '/summoner/' + str(self.get_id_from_name(name, region)) + '/masteries' 
		raw = self.make_request(request_string)
		for page in raw['pages']:
			if page['current']: 
				return page

	def get_masteries_from_id(self, summoner_id, region='na'):
		request_string = region + self.vers + '/summoner/' + str(summoner_id) + '/masteries' 
		raw = self.make_request(request_string)
		pages = []
		for page in raw['pages']:
			pages.append(page)
		return pages
	
	def get_current_masteries_from_id(self, summoner_id, region='na'):
		request_string = region + self.vers + '/summoner/' + str(summoner_id) + '/masteries' 
		raw = self.make_request(request_string)
		for page in raw['pages']:
			if page['current']:
				return page

	def get_runes_from_name(self, name, region='na'):
		request_string = region + self.vers + '/summoner/' + str(self.get_id_from_name(name, region)) + '/runes'
		print request_string
		raw = self.make_request(request_string)
		pages = []
		for page in raw['pages']:
			pages.append(page)
		return pages

	def get_current_runes_from_name(self, name, region='na'):
		request_string = region + self.vers + '/summoner/' + str(self.get_id_from_name(name, region)) + '/runes' 
		raw = self.make_request(request_string)
		for page in raw['pages']:
			if page['current']: 
				return page

	def get_runes_from_id(self, summoner_id, region='na'):
		request_string = region + self.vers + '/summoner/' + str(summoner_id) + '/runes' 
		raw = self.make_request(request_string)
		pages = []
		for page in raw['pages']:
			pages.append(page)
		return pages
	
	def get_current_runes_from_id(self, summoner_id, region='na'):
		request_string = region + self.vers + '/summoner/' + str(summoner_id) + '/runes' 
		raw = self.make_request(request_string)
		for page in raw['pages']:
			if page['current']:
				return page

	def get_names_by_ids(self, summoner_ids, region='na'):
		name_list = []
		for id_list in [summoner_ids[i:i+self.max_names] for i in range (0, len(summoner_ids), self.max_names)]:
			request_string = region + self.vers + '/summoner/' + ','.join(map(str, id_list)) + '/name'
			names = self.make_request(request_string)
			for dto in names['summoners']:
				name_list.append(dto['name'])
		return name_list
			
	def make_request(self, request_info):
		try:
			r = requests.get((self.prior + request_info), params={'api_key': self.api_key})
		except requests.exceptions.RequestException as exception:
			print exception
			sys.exit(1)
		r.raise_for_status()
		return r.json()

