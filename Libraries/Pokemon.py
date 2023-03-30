from BasePokemon import basePokemonList
from Moves import *
from Nature import natureList
from TypeEffectiveness import typeEff
from ExpCurves import expCurve
import random
from collections.abc import Iterable

statList = ['hp', 'atk', 'def', 'spAtk', 'spDef', 'speed', 'acc', 'eva']
critProb = {0: 1/24, 1: 1/8, 2: 1/2, 3: 1, 4: 1}
statModifier = {-6: 2/8, -5: 2/7, -4: 2/6, -3: 2/5, -2: 2/4, -
                1: 2/3, 0: 1, 1: 3/2, 2: 4/2, 3: 5/2, 4: 6/2, 5: 7/2, 6: 8/2}
battleStatModifier = {-6: 3/9, -5: 3/8, -4: 3/7, -3: 3/6, -4: 3 /
                      5, -1: 3/4, 0: 1, 1: 4/3, 2: 5/3, 3: 6/3, 4: 7/3, 5: 8/3, 6: 9/3}


class Stats:
    initStats = {'hp': 0, 'atk': 0, 'def': 0, 'spAtk': 0, 'spDef': 0, 'speed': 0}

    def __init__(self, baseStats=initStats, level=1, indivValues=initStats, effortValues=initStats, nature='hardy'):
        self.baseStats = baseStats
        self.indivValues = indivValues
        self.effortValues = effortValues
        self.level = level
        self.nature = nature

    def currentStats(self):
        hp = int((2*self.baseStats['hp'] + self.indivValues['hp'] + self.effortValues['hp'] / 4) * self.level / 100 + self.level + 10)
        currentStats = {'hp': hp}
        for stat in statList[1:6]: # Works on stats that are not HP
            currentStats[stat] = int(((2 * self.baseStats[stat] + self.indivValues[stat] + self.effortValues[stat]) * self.level / 100 + 5) * natureList[self.nature][stat])
        return currentStats


class Pokemon:
    initStats = {'hp': 0, 'atk': 0, 'def': 0, 'spAtk': 0, 'spDef': 0, 'speed': 0}
    initBattleStats = {'hp': 0, 'atk': 0, 'def': 0, 'spAtk': 0, 'spDef': 0, 'speed': 0, 'acc': 0, 'eva': 0}

    def __init__(self, name, expPoints=0, indivValues=initStats, effortValues=initStats, nature='hardy', battleStats=initBattleStats, ailment=''):
        self.name = name
        self.level = 1
        self.type1 = basePokemonList[self.name].type1
        self.type2 = basePokemonList[self.name].type2
        self.baseStats = basePokemonList[self.name].baseStats
        self.expPoints = expPoints
        self.indivValues = indivValues
        self.effortValues = effortValues
        self.nature = nature
        self.battleStats = battleStats
        self.ailment = ailment
        self.__updateStats()
        self.maxHp = self.currentStats['hp']

    def gainExperience(self, expGain):
        self.expPoints += expGain
        newLevel = next(x for x, val in enumerate(expCurve(basePokemonList[self.name].experienceType)))


    def levelUp(self):
        self.level += 1
        self.__updateStats()
        

    def __updateStats(self):
        stats = Stats(self.baseStats, self.level, self.indivValues, self.effortValues, self.nature)
        self.currentStats = stats.currentStats()
        self.maxHp = self.currentStats['hp']

    def updateHp(self, amount):
        updateValue(self.currentStats['hp'], amount, 0, self.maxHp)
    
    def useMove(self, move: Move, targetPkmns: Iterable['Pokemon']):
        if move.pp > 0:
            move.pp -= 1
            hits = random.randint(move.minHits, move.maxHits)
            if move.category != 'status':
                targetBonus = 0.75 if len(targetPkmns) > 1 else 1
                for targetPkmn in targetPkmns:
                    accuracyUser = battleStatModifier[updateValue(self.battleStats['acc'], -targetPkmn.battleStats['eva'],-6,6)]
                    hitChance = 1 if (move.acuracy == None) else move.acuracy * accuracyUser
                    if randomProb() < hitChance:
                        for i in hits:
                            if move.category=='physical':
                                self.damage(move, self, targetPkmn, 'atk', 'def', targetBonus)
                            elif move.category == 'special':
                                self.damage(move, self, targetPkmn, 'spAtk', 'spDef', targetBonus)
            if move.ailmentChance != None:
                for targetPkmn in targetPkmns:
                    if randomProb() < move.alimentChance:
                        targetPkmn.ailment = move.aliment
            statChangeProb = randomProb()
            for i in range(len(move.stats)):
                if statChangeProb < move.statsChance[i]/100.0:
                    if move.statsStage[i] > 0:
                        updateValue(
                            self.battleStats[move.stats[i]], move.statsStage[i], -6, 6)
                    else:
                        updateValue(
                            targetPkmn.battleStats[move.stats[i]], move.statsStage[i], -6, 6)

    def damage(self, move: Move, targetPkmn: 'Pokemon', sourceStat, targetStat, targetBonus):
        if (move.power == None):
            targetPkmn.updateHp(-targetPkmn.currentStats['hp'])
            self.updateHp(targetPkmn.currentStats['hp'] * move.drain)
        else:
            critBonus = 1.5 if random.random() < critProb[move.crit] else 1
            randomBonus = random.randint(85, 100) / 100
            stabBonus = 1.5 if (move.type == self.type1 or move.type == self.type2) else 1
            typeBonus = typeEff[move.type, targetPkmn.type1] * typeEff[move.type, targetPkmn.type2]
            burnBonus = 0.5 if (sourceStat == 'atk' and self.ailment == 'burn') else 1
            modifier = critBonus * targetBonus * randomBonus * stabBonus * typeBonus * burnBonus
            # Damage calculation from generation V onward. Ignored parental bond, weather, glaive rush, zMove, teraShield and other parameters.
            damageBase = (2*self.level/5 + 2) * move.power
            damageAtk = self.currentStats[sourceStat] * statModifier[self.battleStats[sourceStat]]
            damageDef = targetPkmn.currentStats[targetStat] * statModifier[targetPkmn.battleStats[targetStat]]
            damage = (damageBase * damageAtk * damageDef/50 + 2) * modifier
            targetPkmn.updateHp(-damage)
            if (move.drain != None): self.updateHp(damage * move.drain)


def randomProb():
    return random.uniform(0, 100)


def updateValue(value, update, valueMin, valueMax):
    if (value + update) < valueMin:
        value = valueMin
    elif (value + update) > valueMax:
        value = valueMax
    else:
        value += update
    return value


myBulb = Pokemon('bulbasaur', 10, {'hp': 1, 'atk': 3, 'def': 5, 'spAtk': 25, 'spDef': 2, 'speed': 10}, {
                 'hp': 4, 'atk': 200, 'def': 1, 'spAtk': 10, 'spDef': 10, 'speed': 252}, 'mild')

myStats = Stats({'hp': 45, 'atk': 49, 'def ': 49, 'spAtk': 65, 'spDef': 65, 'speed': 45}, 
                10, 
                {'hp': 1, 'atk': 3, 'def': 5, 'spAtk': 25, 'spDef': 2, 'speed': 10}, 
                {'hp': 4, 'atk': 200, 'def': 1, 'spAtk': 10, 'spDef': 10, 'speed': 252},
                 'mild')