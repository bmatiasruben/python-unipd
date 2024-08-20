#%%

from collections.abc import Iterable
import json
import pandas as pd

class BasePokemon:
    '''BasePokemon class is used to store the base stats of a pokemon at lvl 1.
    
    It also stores the moves that the pokemon learns at each level, the experience type, the base experience, the ev yield, and the type of the pokemon.
    '''
    def __init__(self, pokedexNumber, name, types: Iterable[str], baseStats, baseExp, growthRate, levelUpMoves, evolutionDetails, evYield, captureRate, **kwargs):
        self.pokedexNumber = pokedexNumber
        self.name = name
        self.types = types
        self.baseStats = baseStats
        self.baseExp = baseExp
        self.growthRate = growthRate
        self.levelUpMoves = levelUpMoves
        self.evolutionDetails = evolutionDetails
        self.evYield = evYield
        self.captureRate = captureRate
        self.args = {}
        for key, val in kwargs.items():
            self.args[key] = val
            setattr(self, key, val)

# Load basePokemon from basePokemon.json and create a pandas DataFrame with the data.
basePokemon = pd.read_json('basePokemon.json')
basePokemon.index = basePokemon['name']
basePokemon = basePokemon.drop(columns='name')
basePokemon = basePokemon.T





# %%
