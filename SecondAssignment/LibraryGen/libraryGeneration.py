import pokebase as pb
from collections import defaultdict
import json

moveList = {}
statDict = {'hp': 'hp', 'attack': 'atk', 'defense': 'def', 'special-attack': 'spAtk', 'special-defense': 'spDef', 'speed': 'speed', 'accuracy': 'acc', 'evasion': 'eva'}


with open('moves.json', 'w') as f:
    i = 1
    move = pb.APIResource('move', i)
    while (move):
        dictionary = {}
        dictionary['name'] = move.name
        dictionary['type'] = str(move.type)
        dictionary['category'] = str(move.damage_class)
        dictionary['pp'] = move.pp
        dictionary['power'] = move.power
        dictionary['accuracy'] = move.accuracy
        dictionary['priority'] = move.priority
        dictionary['crit_rate'] = move.meta.crit_rate
        j=0
        stats=[]
        statsStage = []
        try:
            while move.stat_changes[j]:
                stats.append(statDict[str(move.stat_changes[j].stat)])
                statsStage.append(move.stat_changes[j].change)
                j+=1
        except IndexError:
            pass
        dictionary['stats'] = stats
        dictionary['stats_stage'] = statsStage
        dictionary['stat_chance'] = move.meta.stat_chance
        dictionary['ailment'] = str(move.meta.ailment)
        dictionary['ailment_chance'] = move.meta.ailment_chance
        dictionary['flinch_chance'] = move.meta.flinch_chance
        dictionary['healing'] = move.meta.healing
        dictionary['min_turns'] = move.meta.min_turns
        dictionary['max_turns'] = move.meta.max_turns
        dictionary['min_hits'] = move.meta.min_hits
        dictionary['max_hits'] = move.meta.max_hits
        dictionary['drain'] = move.meta.drain
        json.dump(dictionary, f)
        print('', file=f)
        print(i)
        i += 1
        move = pb.APIResource('move', i)

pound = pb.APIResource('move', 423)
try:
    while move.stat_changes[j]:
        stats.append(str(move.stat_changes[j].stat))
        statsStage.append(move.stat_changes[j].change)
        j+=1
except IndexError:
    pass


with open('basePokemon.json', 'w') as f:
    for j in range(1, 152):
        dictionary = {}
        pokemon = pb.APIResource('pokemon', j)
        dictionary['pokedex_number'] = pokemon.id
        dictionary['name'] = pokemon.name
        dictionary['types'] = [pokemon.types[0].type.name]
        try:
            dictionary['types'].append(pokemon.types[1].type.name)
        except IndexError:
            pass
        statsDict = {}
        for stat in pokemon.stats:
            statsDict[statDict[str(stat.stat)]] = stat.base_stat
        dictionary['base_stats'] = statsDict
        dictionary['base_exp'] = pokemon.base_experience
        dictionary['growth_rate'] = pokemon.species.growth_rate.name.replace('-', ' ')
        levelUpMoves = defaultdict(list)
        machineMoves = []
        for move in pokemon.moves:
            if move.version_group_details[-1].move_learn_method.name == 'level-up':
                levelUpMoves[move.version_group_details[-1].level_learned_at].append(move.move.name)
            elif move.version_group_details[-1].move_learn_method.name == 'machine':
                machineMoves.append(move.move.name)
        dictionary['level_up_moves'] = levelUpMoves
        dictionary['machine_moves'] = machineMoves
        evolutionDetails = {'evolves_from': None, 'evolves_to': None, 'evolves_at': None}
        if pokemon.species.evolution_chain.chain.evolves_to != []:
            evolutionDetails['evolves_to'] = pokemon.species.evolution_chain.chain.evolves_to[0].species.name
            evolutionDetails['evolves_at'] = pokemon.species.evolution_chain.chain.evolves_to[0].evolution_details[0].min_level
        if pokemon.species.evolves_from_species != None:
            evolutionDetails['evolves_from'] = pokemon.species.evolves_from_species.name
        dictionary['evolution_details'] = evolutionDetails
        json.dump(dictionary, f)
        print('', file=f)
        print(j)

pokemons = []
for line in open('basePokemon.json'):
    pokemons.append(json.loads(line))