#%%
import pokebase as pb
from collections import defaultdict
import json
from pokebase import cache
cache.API_CACHE

moveList = {}
statDict = {'hp': 'hp', 'attack': 'atk', 'defense': 'def', 'special-attack': 'spAtk', 'special-defense': 'spDef', 'speed': 'speed', 'accuracy': 'acc', 'evasion': 'eva'}

generateMoves = True
generatePokemon = True
#%%
if generateMoves:
    moves = []
    i = 1
    move = pb.APIResource('move', i)
    while (move):
        try:
            dictionary = {}
            dictionary['name'] = move.name
            dictionary['type'] = str(move.type)
            dictionary['category'] = str(move.damage_class)
            dictionary['pp'] = move.pp
            dictionary['power'] = move.power
            dictionary['accuracy'] = move.accuracy
            dictionary['priority'] = move.priority
            dictionary['critRate'] = move.meta.crit_rate
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
            dictionary['statsStage'] = statsStage
            dictionary['statChance'] = move.meta.stat_chance
            dictionary['ailment'] = str(move.meta.ailment)
            dictionary['ailmentChance'] = move.meta.ailment_chance
            dictionary['flinchChance'] = move.meta.flinch_chance
            dictionary['healing'] = move.meta.healing
            dictionary['minTurns'] = move.meta.min_turns
            dictionary['maxTurns'] = move.meta.max_turns
            dictionary['minHits'] = move.meta.min_hits
            dictionary['maxHits'] = move.meta.max_hits
            dictionary['drain'] = move.meta.drain
            moves.append(dictionary)
            print(i)
            i += 1
            move = pb.APIResource('move', i)
        except:
            break
    with open('moves.json', 'w') as f:
        json.dump(moves, f, indent=4)

#%%
if generatePokemon:
    pokemons = []
    for j in range(1, 152):
        dictionary = {}
        pokemon = pb.APIResource('pokemon', j)
        dictionary['pokedexNumber'] = pokemon.id
        dictionary['name'] = pokemon.name
        dictionary['types'] = [pokemon.types[0].type.name]
        try:
            dictionary['types'].append(pokemon.types[1].type.name)
        except IndexError:
            pass
        statsDict = {}
        for stat in pokemon.stats:
            statsDict[statDict[str(stat.stat)]] = stat.base_stat
        dictionary['baseStats'] = statsDict
        dictionary['baseExp'] = pokemon.base_experience
        dictionary['growthRate'] = pokemon.species.growth_rate.name.replace('-', ' ')
        levelUpMoves = defaultdict(list)
        machineMoves = []
        for move in pokemon.moves:
            if move.version_group_details[-1].move_learn_method.name == 'level-up':
                levelUpMoves[move.version_group_details[-1].level_learned_at].append(move.move.name)
            elif move.version_group_details[-1].move_learn_method.name == 'machine':
                machineMoves.append(move.move.name)
        dictionary['levelUpMoves'] = levelUpMoves
        dictionary['machineMoves'] = machineMoves
        evolutionDetails = {'evolvesFrom': None, 'evolvesTo': None, 'evolvesAt': None}
        if pokemon.species.evolution_chain.chain.evolves_to != []:
            evolutionDetails['evolvesTo'] = pokemon.species.evolution_chain.chain.evolves_to[0].species.name
            evolutionDetails['evolvesAt'] = pokemon.species.evolution_chain.chain.evolves_to[0].evolution_details[0].min_level
        if pokemon.species.evolves_from_species != None:
            evolutionDetails['evolvesFrom'] = pokemon.species.evolves_from_species.name
        dictionary['evolutionDetails'] = evolutionDetails
        evYield = {}
        for stat in pokemon.stats:
            evYield[statDict[str(stat.stat)]] = stat.effort
        dictionary['evYield'] = evYield
        dictionary['captureRate'] = pokemon.species.capture_rate
        pokemons.append(dictionary)
        print(j)
    with open('basePokemon.json', 'w') as f:
        json.dump(pokemons, f, indent=4)
    

# %%
