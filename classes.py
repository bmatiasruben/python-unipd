from natureList import nature
from basePokemonList import basePokemonList
from movesList import moveList
from typeEffectiveness import typeEff
import random
from collections.abc import Iterable

statList = ['hp', 'atk', 'def', 'spAtk', 'spDef', 'speed', 'acc', 'eva']
critProb = {0: 1/24, 1: 1/8, 2: 1/2, 3: 1, 4: 1}
statModifier = {-6: 2/8, -5: 2/7, -4: 2/6, -3: 2/5, -2: 2/4, -1: 2/3, 0: 1, 1: 3/2, 2: 4/2, 3: 5/2, 4: 6/2, 5: 7/2, 6: 8/2}
battleStatModifier = {-6: 3/9, -5: 3/8, -4: 3/7, -3: 3/6, -4: 3/5, -1: 3/4, 0: 1, 1: 4/3, 2: 5/3, 3: 6/3, 4: 7/3, 5: 8/3, 6: 9/3}


class BasePokemon:
    def __init__(self, name, type1, type2, baseStats, experienceType):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.baseStats = baseStats
        self.experienceType = experienceType


class Stats:
    initStats = {'hp': 0, 'atk': 0, 'def': 0,
                 'spAtk': 0, 'spDef': 0, 'speed': 0}

    def __init__(self, baseStats=initStats, level=1, indivValues=initStats, effortValues=initStats, nature='hardy'):
        self.baseStats = baseStats
        self.indivValues = indivValues
        self.effortValues = effortValues
        self.level = level
        self.nature = nature

    def currentStats(self):
        hp = int((2*self.baseStats['hp'] +
                  self.indivValues['hp'] + self.effortValues['hp'] / 4) * self.level / 100 + self.level + 10)
        otherStats = ['atk', 'def', 'spAtk', 'spDef', 'speed']
        currentStats = {'hp': hp}
        for stat in otherStats:
            currentStats[stat] = int(((2 * self.baseStats[stat] + self.indivValues[stat] +
                                       self.effortValues[stat]) * self.level / 100 + 5) * nature[self.nature][stat])
        return currentStats


class Pokemon:
    initStats = {'hp': 0, 'atk': 0, 'def': 0,
                 'spAtk': 0, 'spDef': 0, 'speed': 0}
    initBattleStats = {'hp': 0, 'atk': 0, 'def': 0, 'spAtk': 0,
                       'spDef': 0, 'speed': 0, 'acc': 0, 'eva': 0}

    def __init__(self, name, level=1, indivValues=initStats, effortValues=initStats, nature='hardy', battleStats=initBattleStats, ailment=''):
        self.name = name
        self.type1 = basePokemonList[self.name].type1
        self.type2 = basePokemonList[self.name].type2
        self.baseStats = basePokemonList[self.name].baseStats
        self.level = level
        self.indivValues = indivValues
        self.effortValues = effortValues
        self.nature = nature
        self.battleStats = battleStats
        self.ailment = ailment
        self.updateStats()
        self.maxHp = self.currentStats['hp']

    def levelUp(self):
        self.level += 1
        self.updateStats()

    def updateStats(self):
        stats = Stats(self.baseStats, self.level, self.indivValues,
                      self.effortValues, self.nature)
        self.currentStats = stats.currentStats()

    def updateHp(self, amount):
        if amount > 0:
            if self.currentStats['hp'] + amount > self.maxHp:
                self.currentStats['hp'] = self.maxHp
            else:
                self.currentStats['hp'] += amount
        if amount < 0:
            if self.currentStats['hp'] + amount < 0:
                self.currentStats['hp'] = 0
            else:
                self.currentStats['hp'] += amount


class Move:
    def __init__(self, name, type, category, power, accuracy, priority, pp, crit, statChance, ailment, ailmentChance, flinchChance, healing, maxTurns, minTurns, maxHits, minHits, drain):
        self.name = name
        self.type = type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.priority = priority
        self.pp = pp
        self.crit = crit
        self.statChance = statChance
        self.ailment = ailment
        self.ailmentChance = ailmentChance
        self.flinchChance = flinchChance
        self.healing = healing
        self.maxTurns = maxTurns
        self.minTurns = minTurns
        self.maxHits = maxHits
        self.minHits = minHits
        self.drain = drain

    def useMove(self, sourcePkmn: Pokemon, targetPkmns: Iterable[Pokemon]):
        self.pp -= 1
        hits = random.randint(self.minHits, self.maxHits)
        if self.category.__contains__('physical'):
            targetBonus = 0.75 if len(targetPkmns) > 1 else 1
            for i in hits:
                for targetPkmn in targetPkmns:
                    self.damageCalculation(self, sourcePkmn, targetPkmn, 'atk', 'def', targetBonus)
        elif self.category.__contains__('special'):
            targetBonus = 0.75 if len(targetPkmns) > 1 else 1
            for i in hits:
                for targetPkmn in targetPkmns:
                    self.damageCalculation(self, sourcePkmn, targetPkmn, 'spAtk', 'spDef', targetBonus)
        else:
            if self.category.__contains__('ailment'):
                if random.random() < self.ailmentChance:
                    for targetPkmn in targetPkmns:
                        targetPkmn.ailment = self.ailment
            else:
                for stat in statList:
                    if self.category.__contains__(stat + '+'):
                        if random.random() < self.statChance:
                            sourcePkmn.battleStats[stat] += 1
                    if self.category.__contains__(stat + '-'):
                        for targetPkmn in targetPkmns:
                            if random.random() < self.statChance:
                                targetPkmn.battleStats[stat] -= 1

    def damageCalculation(self, sourcePkmn: Pokemon, targetPkmn: Pokemon, sourceStat, targetStat, targetBonus):
        critBonus = 1.5 if random.random() < critProb[self.crit] else 1
        randomBonus = random.randint(85, 100) / 100
        stabBonus = 1.5 if (self.type == sourcePkmn.type1 or self.type == sourcePkmn.type2) else 1
        if min(typeEff[self.type, targetPkmn.type1], typeEff[self.type, targetPkmn.type2]) == 0:
            typeBonus = 0
        else:
            typeBonus = max(typeEff[self.type, targetPkmn.type1], typeEff[self.type, targetPkmn.type2])
        modifier = critBonus * targetBonus * randomBonus * stabBonus * typeBonus
        damage = (2*sourcePkmn.level/5 + 2)*self.power * \
            sourcePkmn.currentStats[sourceStat]*statModifier[sourcePkmn.battleStats[sourceStat]] / \
            targetPkmn.currentStats[targetStat]/50 + 2
        damage *= modifier
        targetPkmn.updateHp(-damage)
        sourcePkmn.updateHp(damage * self.drain)


myBulb = Pokemon('bulbasaur', 10, {'hp': 1, 'atk': 3, 'def': 5, 'spAtk': 25, 'spDef': 2, 'speed': 10}, {
                 'hp': 4, 'atk': 200, 'def': 1, 'spAtk': 10, 'spDef': 10, 'speed': 252}, 'mild')
