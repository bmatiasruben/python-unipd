from Libraries.BasePokemon import basePokemonList
from Libraries.Moves import *
from Libraries.Nature import natureList
from Libraries.TypeEffectiveness import typeEff
from Libraries.ExpCurves import expCurve
import random
from collections.abc import Iterable
from copy import deepcopy
from time import sleep

statList = ['hp', 'atk', 'def', 'spAtk', 'spDef', 'speed', 'acc', 'eva']
statsToPrint = {'hp': 'HP', 'atk': 'Attack', 'def': 'Defense', 'spAtk': 'Sp. Attack', 'spDef': 'Sp. Defense', 'speed': 'Speed', 'acc': 'Accuracy', 'eva': 'Evasion'}
critProb = {0: 1/24, 1: 1/8, 2: 1/2, 3: 1, 4: 1}
statModifier = {-6: 2/8, -5: 2/7, -4: 2/6, -3: 2/5, -2: 2/4, -
                1: 2/3, 0: 1, 1: 3/2, 2: 4/2, 3: 5/2, 4: 6/2, 5: 7/2, 6: 8/2}
battleStatModifier = {-6: 3/9, -5: 3/8, -4: 3/7, -3: 3/6, -4: 3 /
                      5, -1: 3/4, 0: 1, 1: 4/3, 2: 5/3, 3: 6/3, 4: 7/3, 5: 8/3, 6: 9/3}


class Stats:
    '''Class to represent and calculate the stats of a Pokemon'''
    initStats = {'hp': 0, 'atk': 0, 'def': 0, 'spAtk': 0, 'spDef': 0, 'speed': 0}

    def __init__(self, baseStats=initStats, level=1, indivValues=initStats, effortValues=initStats, nature='hardy'):
        self.baseStats = baseStats
        self.indivValues = indivValues
        self.effortValues = effortValues
        self.level = level
        self.nature = nature

    def maxHp(self):
        '''Calculates the maximum HP of a Pokemon'''
        hp = int((2*self.baseStats['hp'] + self.indivValues['hp'] + self.effortValues['hp'] / 4) * self.level / 100 + self.level + 10)
        return hp

    def currentStats(self):
        '''Calculates the current stats of a Pokemon including IVs, EVs, level and nature'''
        currentStats = {}
        for stat in statList[1:6]: # Works on stats that are not HP
            currentStats[stat] = int(((2 * self.baseStats[stat] + self.indivValues[stat] + self.effortValues[stat]) * self.level / 100 + 5) * natureList[self.nature][stat])
        return currentStats


class Pokemon:
    '''Class to represent a Pokemon'''
    def __init__(self, name, level = 1, ailment='', **kwargs):
        self.name = name
        self.level = level
        self.nickname = name
        self.moves = self.__generateInitMoves()
        self.type = basePokemonList[self.name].type
        self.baseStats = basePokemonList[self.name].baseStats
        self.expPoints = expCurve(basePokemonList[self.name].experienceType)[self.level - 1]
        self.indivValues = self.__getRandomIvs()
        self.effortValues = {'hp': 0, 'atk': 0, 'def': 0, 'spAtk': 0, 'spDef': 0, 'speed': 0}
        self.nature = random.choice(list(natureList))
        self.battleStats = {'hp': 0, 'atk': 0, 'def': 0, 'spAtk': 0, 'spDef': 0, 'speed': 0, 'acc': 0, 'eva': 0}
        self.ailment = ailment
        stats = Stats(self.baseStats, self.level, self.indivValues, self.effortValues, self.nature)
        self.currentStats = stats.currentStats()
        self.maxHp = stats.maxHp()
        self.currentHp = self.maxHp
        self.args = {}
        for key, val in kwargs.items():
            self.args[key] = val
            setattr(self, key, val)

    def gainExperience(self, expGain):
        '''Gain experience and level up if necessary
        
        Compares the experience gained with the experience needed to level up. Depends on the experience curve of the Pokemon.
        '''
        self.expPoints += expGain
        newLevel = next(x for x, val in enumerate(expCurve(basePokemonList[self.name].experienceType)) if val > self.expPoints)
        for i in range(self.level, newLevel):
            self.__levelUp()

    def __generateInitMoves(self):
        '''Generates the initial moves of a Pokemon.
        
        Includes lvl 1 and egg moves. If there are more than 4 moves, it randomly selects 4 of them.
        '''
        availableMoves = []
        initMoves = []
        for lvl in list(basePokemonList[self.name].learnedMoves):
            if int(lvl) < self.level + 1:
                availableMoves.extend(basePokemonList[self.name].learnedMoves[lvl])
        if len(availableMoves) > 4:
            toChoose = []
            while len(initMoves) < 4:
                r = random.randint(0, len(availableMoves) - 1)
                if r not in toChoose:
                    toChoose.append(r)
                    try:
                        initMoves.append(deepcopy(moveList[availableMoves[r]]))
                    except KeyError:
                        print(f'Error: {availableMoves[r]}')
        else:
            for move in availableMoves:
                try:
                    initMoves.append(deepcopy(moveList[move]))
                except KeyError:
                    print(f'Error: {move}')
        return initMoves

    def __levelUp(self):
        '''Level up a Pokemon. Checks if it evolves.'''
        self.level += 1
        self.__updateStats()
        print(f'Your {self.nickname} leveled up!')
        if basePokemonList[self.name].evolutionDetails['evolvesAt'] != None:
            if self.level >= basePokemonList[self.name].evolutionDetails['evolvesAt']:
                print(f'Wait... Your {self.name} is evolving...')
                sleep(3)
                self.__evolve()
                
        
    def __evolve(self):
        '''Evolves a Pokemon. if nicknamed, it will keep the nickname. Otherwise, it will change to the new name.'''
        oldName = self.nickname
        self.name = basePokemonList[self.name].evolutionDetails['evolvesTo']
        self.type = basePokemonList[self.name].type
        self.baseStats = basePokemonList[self.name].baseStats
        if self.nickname == oldName:
            self.nickname = self.name
        self.__updateStats()
        print(f'Congratulations! Your {oldName} evolved into {self.name}!')
        sleep(3)
        
    def __updateStats(self):
        '''Updates the stats of a Pokemon after leveling up or evolving. Includes IVs and EVs.'''
        stats = Stats(self.baseStats, self.level, self.indivValues, self.effortValues, self.nature)
        self.currentStats = stats.currentStats()
        hpGain = int((2*self.baseStats['hp'] + self.indivValues['hp'] + self.effortValues['hp'] / 4) / 100 + 1)
        self.currentHp += hpGain
        self.maxHp += hpGain

    def updateHp(self, amount):
        '''Updates the current HP of a Pokemon. It will not go below 0 or above the maximum HP.'''
        self.currentHp = updateValue(self.currentHp, int(amount), 0, self.maxHp)
    
    def useMove(self, move: Move, targetPkmn: 'Pokemon'):
        '''Uses a move on a target Pokemon. 
        
        Checks if the move has PP left and calculates the damage or ailment.
        Compares if the move is physical or special and calculates the damage accordingly.
        If the move has a status change, it will apply it to the target Pokemon, including stat changes.'''
        if move.pp > 0:
            move.pp -= 1
            ownerPrint(self, f'{self.nickname} used {move.name}')
            hits = random.randint(move.minHits, move.maxHits) if (move.minHits != None) else 1
            if move.category != 'status':
                accuracyUser = battleStatModifier[updateValue(self.battleStats['acc'], -targetPkmn.battleStats['eva'],-6,6)]
                hitChance = 100 if (move.accuracy == None) else move.accuracy * accuracyUser
                if randomProb() < hitChance:
                    for i in range(hits):
                        if move.category=='physical':
                            self.__damage(move, targetPkmn, 'atk', 'def')
                        elif move.category == 'special':
                            self.__damage(move, targetPkmn, 'spAtk', 'spDef')
                else:
                    print('But it failed!')
            if move.ailmentChance != 0:
                self.__ailment(move, targetPkmn)
            statChangeProb = randomProb()
            if move.stats != []:
                if move.statChance != 0:
                    statChance = move.statChance
                else:
                    statChance = 100
                for i in range(len(move.stats)):
                    if statChangeProb < statChance:
                        if move.statsStage[i] > 0:
                            if (self.battleStats[move.stats[i]] == 6):
                                ownerPrint(self, f'{self.nickname}\'s {statsToPrint[move.stats[i]]} won\'t go any higher!')
                                print()
                            else:
                                self.battleStats[move.stats[i]] = updateValue(self.battleStats[move.stats[i]], move.statsStage[i], -6, 6)
                                if move.statsStage[i] == 1: 
                                    ownerPrint(self, f'{self.nickname}\'s {statsToPrint[move.stats[i]]} rose!')
                                elif move.statsStage[i] == 2: 
                                    ownerPrint(self, f'{self.nickname}\'s {statsToPrint[move.stats[i]]} rose sharply!')
                                else: 
                                    ownerPrint(self, f'{self.nickname}\'s {statsToPrint[move.stats[i]]} rose drastically!')
                        else:
                            if (targetPkmn.battleStats[move.stats[i]] == -6):
                                ownerPrint(targetPkmn, f'{targetPkmn.nickname}\'s {statsToPrint[move.stats[i]]} won\'t go any lower!')
                            else:
                                targetPkmn.battleStats[move.stats[i]] = updateValue(targetPkmn.battleStats[move.stats[i]], move.statsStage[i], -6, 6)
                                if move.statsStage[i] == -1: 
                                    ownerPrint(targetPkmn, f'{targetPkmn.nickname}\'s {statsToPrint[move.stats[i]]} fell!')
                                elif move.statsStage[i] == -2: 
                                    ownerPrint(targetPkmn, f'{targetPkmn.nickname}\'s {statsToPrint[move.stats[i]]} harshly fell!')
                                else: 
                                    ownerPrint(targetPkmn, f'{targetPkmn.nickname}\'s {statsToPrint[move.stats[i]]} severely fell!')
        else:
            print('That move doesn\'t have any more PP left!')

    def __ailment(self, move: Move, pokemon: 'Pokemon'):
        '''Applies an ailment to a Pokemon. Not implemented yet.
        '''
        print('')

    def __damage(self, move: Move, targetPkmn: 'Pokemon', sourceStat, targetStat):
        '''Calculates the damage of a move and applies it to the target Pokemon.
        
        Checks if the move is a OHKO move. If it is, it will apply the damage to the target Pokemon.
        Otherwise, it will calculate the damage based on the move power, the source and target stats, the type effectiveness and other modifiers.
        Includes critical hits, random bonus, STAB, type effectiveness and burn bonus.
        '''
        if move.power == None:
            # Check first if it's a OHKO (i.e. move.power == None)
            # All other moves with no power will not be implemented
            if move.name in ohkoMoves:
                self.updateHp(targetPkmn.currentHp * move.drain)
                targetPkmn.updateHp(-targetPkmn.currentHp)
            else:
                print('But it failed!')
        else:
            # If it's not OHKO, check damage
            if move.critRate > 0:
                critBonus = 1.5 if randomProb() < critProb[move.critRate] * 100 else 1
            else:
                critBonus = 1
            randomBonus = random.randint(85, 100) / 100
            stabBonus = 1.5 if (move.type in self.type) else 1
            typeBonus = 1
            for i in range(len(targetPkmn.type)):
                typeBonus *= typeEff[move.type, targetPkmn.type[i]]
            burnBonus = 0.5 if (sourceStat == 'atk' and self.ailment == 'burn') else 1
            modifier = critBonus * randomBonus * stabBonus * typeBonus * burnBonus
            # Damage calculation from generation V onward. 
            # Ignored target bonus, parental bond, weather, glaive rush, zMove, teraShield and other parameters.
            damageBase = (2*self.level/5 + 2) * move.power
            damageAtk = self.currentStats[sourceStat] * statModifier[self.battleStats[sourceStat]]
            damageDef = targetPkmn.currentStats[targetStat] * statModifier[targetPkmn.battleStats[targetStat]]
            damage = (damageBase * damageAtk / (damageDef * 50) + 2) * modifier
            targetPkmn.updateHp(-int(damage))
            if move.drain > 0: self.updateHp(int(damage * move.drain / 100))
            if critBonus == 1.5: print('A critical hit!')
            if typeBonus == 0:
                print('It doesn\'t seem to have an effect...')
            elif typeBonus < 1:
                print('It\'s not very effective...')
            elif typeBonus > 1:
                print('It\'s very effective!')

    def __getRandomIvs(self):
        return {'hp': random.randint(0, 31), 'atk': random.randint(0, 31), 'def': random.randint(0, 31), 'spAtk': random.randint(0, 31), 'spDef': random.randint(0, 31), 'speed': random.randint(0, 31)}

def ownerPrint(pokemon, text):
        if hasattr(pokemon, 'owner'):
            if pokemon.owner == 'mainCharacter':
                print(text)
            elif pokemon.owner == 'opponent':
                print('The opponent\'s ' + text)
            else:
                print(f'The wild ' + text)
        else:
            print(f'The wild ' + text)

def randomProb():
    return random.uniform(0, 100)

def updateValue(value, update, valueMin, valueMax):
    '''Updates a value with a certain update. It will not go below the minimum or above the maximum.
    
    Used for stats, HP, etc.
    '''
    if (value + update) < valueMin:
        value = valueMin
    elif (value + update) > valueMax:
        value = valueMax
    else:
        value += update
    return value
