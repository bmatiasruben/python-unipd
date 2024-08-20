Names: Matías Rubén
Surnames: Bolaños Wagner
Affiliation: Università degli Studi di Padova
----------------------------------------------------------------------------------------------------
WARNING: Although I created my own classes, to import a database, I created a separate file (LibraryGen/libraryGeneration.py)
that uses the PokeAPI v2, and then translates the information to my own class format. I did this for base pokemons and moves
----------------------------------------------------------------------------------------------------

So, by the time of deliving this assignment, I already did some extra work on the entire program...
That is why on this version, there might be some stuff not being used.

To play, you run the game.py program. This will call the Main() function, which will allow you to create 
a Pokemon Trainer, and choose any Pokemon from the first generation, and the level in which you want to.

For the Pokemon Class, I added random IV generation at the init of the pokemon, and also for the moves.
The generateInitMoves() method of the class, searches from my own database which moves are available to the pokemon
just from level-ups. If there's more than 4, the method randomly selects 4 of those available.