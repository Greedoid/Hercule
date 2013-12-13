from hercule import Request
from config import api_key

def main():

	'''
	Initialize your Request class by passing in the api key - visit https://developer.riotgames.com/sign-in in order to register for yours!
	'''
	r = Request(api_key)

	'''
	Calling a function involves passing in a name whenever a function asks for it - all API calls will have a method that takes a summoner name as a sole argument
	'''
	player_id = r.get_id_from_name('Dyrus')
	print player_id

	'''
	Most functions return a dict. Most functions will take summoner ID's or player names as parameters
	'''
	masteries = r.get_masteries_from_id(player_id)
	print type(masteries)
	print type(masteries[0])

	'''
	All summoner-based calls assume NA region. If you want another region, just pass it in after the summoner name
	'''
	current_runes = r.get_current_runes_from_name('Froggen', 'euw')
	print current_runes

if __name__ == ('__main__'):
	main()


