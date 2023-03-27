from Libraries.basePokemon import basePokemon
from Libraries.moves import move
from Libraries.nature import nature
from Libraries.typeEffectiveness import typeEff
import random
from collections.abc import Iterable

statList = ['hp', 'atk', 'def', 'spAtk', 'spDef', 'speed', 'acc', 'eva']
critProb = {0: 1/24, 1: 1/8, 2: 1/2, 3: 1, 4: 1}
statModifier = {-6: 2/8, -5: 2/7, -4: 2/6, -3: 2/5, -2: 2/4, -
                1: 2/3, 0: 1, 1: 3/2, 2: 4/2, 3: 5/2, 4: 6/2, 5: 7/2, 6: 8/2}
battleStatModifier = {-6: 3/9, -5: 3/8, -4: 3/7, -3: 3/6, -4: 3 /
                      5, -1: 3/4, 0: 1, 1: 4/3, 2: 5/3, 3: 6/3, 4: 7/3, 5: 8/3, 6: 9/3}


class BasePokemon:
    def __init__(self, name, type1, type2, baseStats, experienceType):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.baseStats = baseStats
        self.experienceType = experienceType


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
        otherStats = ['atk', 'def', 'spAtk', 'spDef', 'speed']
        currentStats = {'hp': hp}
        for stat in otherStats:
            currentStats[stat] = int(((2 * self.baseStats[stat] + self.indivValues[stat] + self.effortValues[stat]) * self.level / 100 + 5) * nature[self.nature][stat])
        return currentStats


class Pokemon:
    initStats = {'hp': 0, 'atk': 0, 'def': 0, 'spAtk': 0, 'spDef': 0, 'speed': 0}
    initBattleStats = {'hp': 0, 'atk': 0, 'def': 0, 'spAtk': 0, 'spDef': 0, 'speed': 0, 'acc': 0, 'eva': 0}

    def __init__(self, name, level=1, indivValues=initStats, effortValues=initStats, nature='hardy', battleStats=initBattleStats, ailment=''):
        self.name = name
        self.type1 = basePokemon[self.name].type1
        self.type2 = basePokemon[self.name].type2
        self.baseStats = basePokemon[self.name].baseStats
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
        stats = Stats(self.baseStats, self.level, self.indivValues, self.effortValues, self.nature)
        self.currentStats = stats.currentStats()

    def updateHp(self, amount):
        updateValue(self.currentStats['hp'], amount, 0, self.maxHp)


class Move:
    def __init__(self, name, type, category, power, accuracy, priority, pp, crit, stats: Iterable[str], statsStage: Iterable[str], statsChance: Iterable[str], ailment, ailmentChance, flinchChance, healing, maxTurns, minTurns, maxHits, minHits, drain):
        self.name = name
        self.type = type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.priority = priority
        self.pp = pp
        self.crit = crit
        self.stats = stats
        self.statsStage = statsStage
        self.statsChance = statsChance
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
        if self.pp > 0:
            self.pp -= 1
            hits = random.randint(self.minHits, self.maxHits)
            if self.category.__contains__('physical'):
                targetBonus = 0.75 if len(targetPkmns) > 1 else 1
                for targetPkmn in targetPkmns:
                    accuracyUser = updateValue(battleStatModifier[sourcePkmn.battleStats['acc']], -battleStatModifier[targetPkmn.battleStats['eva']], -6, 6)
                    hitChance = self.accuracy * accuracyUser
                    if random.random() < hitChance:
                        for i in hits:
                            self.damage(
                                self, sourcePkmn, targetPkmn, 'atk', 'def', targetBonus)
            elif self.category.__contains__('special'):
                targetBonus = 0.75 if len(targetPkmns) > 1 else 1
                for targetPkmn in targetPkmns:
                    accuracyUser = updateValue(battleStatModifier[sourcePkmn.battleStats['acc']], -battleStatModifier[targetPkmn.battleStats['eva']], -6, 6)
                    hitChance = self.accuracy * accuracyUser
                    if random.random() < hitChance:
                        for i in hits:
                            self.damage(
                                self, sourcePkmn, targetPkmn, 'spAtk', 'spDef', targetBonus)
            for targetPkmn in targetPkmns:
                if random.random() < self.ailmentChance:
                    targetPkmn.ailment = self.ailment
            statChangeProb = random.random()
            for i in range(len(self.stats)):
                if statChangeProb < self.statsChance[i]:
                    if self.statsStage[i] > 0:
                        updateValue(
                            sourcePkmn.battleStats[self.stats[i]], self.statsStage[i], -6, 6)
                    else:
                        updateValue(
                            targetPkmn.battleStats[self.stats[i]], self.statsStage[i], -6, 6)

    def damage(self, sourcePkmn: Pokemon, targetPkmn: Pokemon, sourceStat, targetStat, targetBonus):
        critBonus = 1.5 if random.random() < critProb[self.crit] else 1
        randomBonus = random.randint(85, 100) / 100
        stabBonus = 1.5 if (self.type == sourcePkmn.type1 or self.type == sourcePkmn.type2) else 1
        if min(typeEff[self.type, targetPkmn.type1], typeEff[self.type, targetPkmn.type2]) == 0:
            typeBonus = 0
        else:
            typeBonus = max(typeEff[self.type, targetPkmn.type1], typeEff[self.type, targetPkmn.type2])
        burnBonus = 0.5 if (sourceStat == 'atk' and sourcePkmn.ailment == 'burn') else 1
        modifier = critBonus * targetBonus * randomBonus * stabBonus * typeBonus * burnBonus
        # Damage calculation from generation V onward. Ignored parental bond, weather, glaive rush, zMove, teraShield and other parameters.
        damageBase = (2*sourcePkmn.level/5 + 2) * self.power
        damageAtk = sourcePkmn.currentStats[sourceStat] * statModifier[sourcePkmn.battleStats[sourceStat]]
        damageDef = targetPkmn.currentStats[targetStat] * statModifier[targetPkmn.battleStats[targetStat]]
        damage = (damageBase * damageAtk * damageDef/50 + 2) * modifier
        targetPkmn.updateHp(-damage)
        sourcePkmn.updateHp(damage * self.drain)


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
