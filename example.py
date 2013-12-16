from hercule import Request
from config import api_key #This assumes you have an external config file that houses your API key. If you do not, to run this example, delete this line and input your API key when we initialize the Request object

def main():

	
	# Initialize your Request class by passing in the api key - visit https://developer.riotgames.com/sign-in in order to register for yours!
	
	r = Request(api_key)

	
	# Calling a function involves passing in a name whenever a function asks for it - all API calls will have a method that takes a summoner name as a sole argument
	
	player_id = r.get_id_from_name('The Rain Man')
	print player_id

	
	# Most functions return a dict or list of dicts. Most functions will take summoner ID's or player names as parameters
	
	masteries = r.get_masteries_from_id(player_id)
	print type(masteries)
	print type(masteries[0])

	
	# All summoner-based calls assume NA region. If you want another region, just pass it in after the summoner name
	
	current_runes = r.get_current_runes_from_name('Froggen', 'euw')
	print current_runes

	# Asking for any multi-page info (like teams or stats) of a player returns a multi-page json DTO 
	
	teams = r.get_teams_from_name('Dyrus')
	print teams[0]['name']

	# Asking for ranked stats or a player's stat summary will require a season, defaulted to season 4. As of this writing, season 4 has not started yet, so calling the default stat functions will not return anything particularly useful - pass in 'SEASON3' in order to get the previous season's statistics. 
	stats = r.get_ranked_summary_from_name('TheOddOne','na', 'SEASON3')
	print stats

if __name__ == ('__main__'):
	main()


