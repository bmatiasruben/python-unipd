import pokebase as pb
from collections import defaultdict

# This script generates the text files for the Pokemon and Move classes in the Pokemon library.

# These are then called by the main scripts to create the Pokemon and Move objects.
# Does NOT need to be run by the user. This is for the developer to update the library.

moveList = {}
statDict = {'hp': 'hp', 'attack': 'atk', 'defense': 'def', 'special-attack': 'spAtk', 'special-defense': 'spDef', 'speed': 'speed', 'accuracy': 'acc', 'evasion': 'eva'}

i = 1
move = pb.APIResource('move', i)
with open('moves.txt', 'w') as f:
    while (move):
        name = move.name
        type = str(move.type)
        category = str(move.damage_class)
        pp = move.pp
        string = f'\'{name}\': Move(\'{name}\', \'{type}\', \'{category}\', {pp}'
        if move.power != None: string += f', power={move.power}'
        if move.accuracy != None: string += f', accuracy={move.accuracy}'
        if move.priority != 0: string += f', priority={move.priority}'
        if move.meta.crit_rate != 0: string += f', critRate={move.meta.crit_rate}'
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
        if stats != []: string += f', stats={stats}'
        if statsStage != []: string += f', statsStage={statsStage}'
        if move.meta.stat_chance != 0: string += f', statsChance={move.meta.stat_chance}'
        if str(move.meta.ailment) != 'none': string += f', ailment=\'{move.meta.ailment}\''
        if move.meta.ailment_chance != 0: string += f', ailmentChance={move.meta.ailment_chance}'
        if move.meta.flinch_chance != 0: string += f', flinchChance={move.meta.flinch_chance}'
        if move.meta.healing != 0: string += f', healing={move.meta.healing}'
        if move.meta.min_turns != None: string += f', minTurns={move.meta.min_turns}'
        if move.meta.max_turns != None: string += f', maxTurns={move.meta.max_turns}'
        if move.meta.min_hits != None: string += f', minHits={move.meta.min_hits}'
        if move.meta.max_hits != None: string += f', maxHits={move.meta.max_hits}'
        if move.meta.drain != 0: string += f', dragin={move.meta.drain}'
        string += '),'
        print(string, file= f)
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

with open('basePokemon.txt', 'w') as f:
    for j in range(1, 152):
        pokemon = pb.APIResource('pokemon', j)
        string = f'\'{pokemon.name}\': BasePokemon({pokemon.id}, \'{pokemon.name}\', [\'{str(pokemon.types[0].type)}\''
        try:
            string += f', \'{str(pokemon.types[1].type)}\''
        except IndexError:
            pass
        string += '], {'
        for stat in pokemon.stats[:-1]:
            string += f'\'{statDict[str(stat.stat)]}\': {stat.base_stat}, '
        string += f'\'{statDict[str(pokemon.stats[-1].stat)]}\': {pokemon.stats[-1].base_stat}'
        string += '}'
        string += f', {pokemon.base_experience}, \'{pokemon.species.growth_rate.name.replace("-", " ")}\', '
        levelUpMoves = defaultdict(list)
        machineMoves = []
        for move in pokemon.moves:
            if move.version_group_details[-1].move_learn_method.name == 'level-up':
                levelUpMoves[move.version_group_details[-1].level_learned_at].append(move.move.name)
            elif move.version_group_details[-1].move_learn_method.name == 'machine':
                machineMoves.append(move.move.name)
        string += str(levelUpMoves)[28:-1]
        string += ', {'
        for stat in pokemon.stats:
            string += f'\'{statDict[stat.stat.name]}\': {stat.effort}, '
        string = string[:len(string) - 2]
        string += '}'
        if pokemon.species.evolution_chain.chain.evolves_to != []:
            string += ', evolution={'
            string += f'\'level\': {pokemon.species.evolution_chain.chain.evolves_to[0].evolution_details[0].min_level}, \'evolvesTo\': \'{pokemon.species.evolution_chain.chain.evolves_to[0].species.name}\''
            string += '}'
        if machineMoves != []:
            string += ', machineMoves='
            string += str(machineMoves)
        string += '),'
        print(string, file= f)
        print(j)