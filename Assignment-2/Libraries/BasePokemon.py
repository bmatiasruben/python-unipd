from collections.abc import Iterable
import json

class BasePokemon:
    '''BasePokemon class is used to store the base stats of a pokemon at lvl 1.
    
    It also stores the moves that the pokemon learns at each level, the experience type, the base experience, the ev yield, and the type of the pokemon.
    '''
    def __init__(self, pokedexNumber, name, type: Iterable[str], baseStats, baseExperience, experienceType, learnedMoves, evolutionDetails, evYield, captureRate, **kwargs):
        self.pokedexNumber = pokedexNumber
        self.name = name
        self.type = type
        self.baseStats = baseStats
        self.baseExperience = baseExperience
        self.experienceType = experienceType
        self.learnedMoves = learnedMoves
        self.evolutionDetails = evolutionDetails
        self.evYield = evYield
        self.captureRate = captureRate
        self.args = {}
        for key, val in kwargs.items():
            self.args[key] = val
            setattr(self, key, val)

# Load moves from moves.json and create a dictionary of moves.
basePokemonList = {}
with open('basePokemon.json', 'r') as f:
    pokemons = json.load(f)
    for pokemon in pokemons:
        basePokemonList[pokemon['name']] = BasePokemon(pokedexNumber=pokemon['pokedexNumber'], 
                                                       name=pokemon['name'], 
                                                       type=pokemon['types'], 
                                                       baseStats=pokemon['baseStats'], 
                                                       baseExperience=pokemon['baseExp'], 
                                                       experienceType=pokemon['growthRate'], 
                                                       learnedMoves=pokemon['levelUpMoves'],
                                                       evolutionDetails=pokemon['evolutionDetails'],
                                                       evYield=pokemon['evYield'],
                                                       captureRate=pokemon['captureRate'])
