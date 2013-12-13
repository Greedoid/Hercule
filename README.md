Hercule 0.1.0
=============

Hercule is a robust Python wrapper for Riot Games League of Legends API

Making Calls
------------

It's simple! To start, from hercule, import Request - this is the class you'll use to make API calls

	from hercule import Request

Then, initialize your class - you'll need to have your API key, which you can get at https://developer.riotgames.com/sign-in

	r = Request(api_key)

From this object, you can call any of Hercule's methods and receive your information as a string or a Python dict 
Here are a few examples - 

### Getting a summoner ID

	player_id = r.get_id_from_name('Greedoid')

What this method returns is simply the player's Riot ID - useful for other methods that take it as an argument

As a note, any methods that return player information default to the North American server - if you wish to query EU-West or EU-Northeast players, just pass the server in after the player name 

	player_id = r.get_id_from_name('Froggen', 'euw')

### Getting many summoner names from a list of IDs

	bunch_of_ids = [1, 2, 3, ... 140]
	list_of_ids = r.get_names_from_ids(bunch_of_ids)

This method returns a list of names corresponding to the list of summoner IDs passed to it.
**NOTE**: This API call takes in a max of 40 IDs per call. You can pass in as many IDs as you want to the method, but you may be rate-limited if you use very large lists of IDs
