Hercule
=======

Hercule is a robust Python wrapper for Riot Games League of Legends API

Making Calls
------------

It's simple! To start, from hercule, import Request - this is the class you'll use to make API calls

	from hercule import Request

Then, initialize your class - you'll need to have your API key, which you can get at https://developer.riotgames.com/sign-in

	r = Request(api_key)
