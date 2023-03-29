import pokebase as pb

moveList = {}
statDict = {'attack': 'atk', 'defense': 'def', 'special-attack': 'spAtk', 'special-defense': 'spDef', 'speed': 'speed', 'accuracy': 'acc', 'evasion': 'eva'}

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
