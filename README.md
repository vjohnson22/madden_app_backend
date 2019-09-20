# Madden Stats Backend


The goal of this project was to build a full stack application from start to finish. This is the backend, while the frontend repository can be found at https://github.com/vjohnson22/madden-stats. My app is designed to track the statistics from user vs user games in a Madden 20 (for video game on Playstation 4) league that I have with several college friends. I created this application because the statistics captured on the game do not specifically track user vs user games, and I wanted to do visualizations using Charts.js, as well as some more complex backend queries (coming soon)


## Getting Started
To use this API, go to https://maddenstats.herokuapp.com/owners to get information on all of the users in the league. You can then add an owner number to the end (owners/1 for example), to query a specific owner. You can do the same actions for games, gamestats, seasonstats as well 



'/' has full CRUD, so you can use the following requests:
```
*GET: '/' to get all owners
*GET: '/:name' to get a owner
*POST: '/' with a request with the key values in the body to create a new entry
*PATCH: '/:name' with the changed key value pairing in the request body to *update a record
*DELETE: '/:name' to delete a record
```

## Getting Started Locally
```
1.Fork and clone repository
2. pipenv Install
3. pipenv shell
```

## Built With

* Django
* Python


## Author

* Victor Johnson
