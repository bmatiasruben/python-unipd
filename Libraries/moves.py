from Libraries.basePokemon import basePokemonList
from collections.abc import Iterable
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

moveList = {'tackle': Move()}
