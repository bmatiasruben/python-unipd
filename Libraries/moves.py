#%%

import json 
import pandas as pd
import numpy as np

class Move:
    '''A class to represent a move in Pokemon.
    
    Includes power, accuracy, PP, type, category, and any additional effects.
    '''
    def __init__(self, name, type, category, pp=0, power=None, accuracy=100, priority=0, critRate=0, stats=[], statsStage=[], statChance=0, ailment="none", ailmentChance=0, flinchChance=0, healing=0, minTurns=None, maxTurns=None, minHits=None, maxHits=None, drain=0):
        self.name = name
        self.type = type
        self.category = category
        self.pp = pp
        self.power = power
        self.accuracy = accuracy
        self.priority = priority
        self.critRate = critRate
        self.stats = stats
        self.statsStage = statsStage
        self.statChance = statChance
        self.ailment = ailment
        self.ailmentChance = ailmentChance
        self.flinchChance = flinchChance
        self.healing = healing
        self.minTurns = minTurns
        self.maxTurns = maxTurns
        self.minHits = minHits
        self.maxHits = maxHits
        self.drain = drain

# List of moves, including ohko moves. All moves are from up to generation 6. Removed some moves that made the useMove function too complicated.

ohkoMoves = ['fissure', 'guillotine', 'horn-drill', 'sheer-cold']
moveList = pd.read_json('moves.json')
# Replace NaN values with None.
moveList = moveList.fillna(np.nan).replace([np.nan], [None])
moveList.index = moveList['name']
moveList = moveList.drop(columns='name')
moveList = moveList.T



# %%
