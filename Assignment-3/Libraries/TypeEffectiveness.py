typeEff = {}
types = ['normal', 'fire', 'water', 'grass', 'electric', 'ice', 'fighting', 'poison',
         'ground', 'flying', 'psychic', 'bug', 'rock', 'ghost', 'dragon', 'dark', 'steel', 'fairy']
effectiveness = {}

effectiveness['normal'] = {'strong': [], 'weak': ['rock', 'steel'], 'null': ['ghost']}
effectiveness['fire'] = {'strong': ['bug', 'steel', 'grass', 'ice'], 'weak': ['rock', 'fire', 'water', 'dragon'], 'null': []}
effectiveness['water'] = {'strong': ['ground', 'rock', 'fire'], 'weak': ['water', 'grass', 'dragon'], 'null': []}
effectiveness['grass'] = {'strong': ['ground', 'rock', 'water'], 'weak': [
    'flying', 'poison', 'bug', 'steel', 'fire', 'grass', 'dragon'], 'null': []}
effectiveness['electric'] = {'strong': ['flying', 'water'], 'weak': ['ground', 'grass', 'dragon'], 'null': ['electric']}
effectiveness['ice'] = {'strong': ['flying', 'ground', 'grass', 'dragon'], 'weak': ['steel', 'fire', 'water', 'ice'], 'null': []}
effectiveness['fighting'] = {'strong': ['normal', 'rock', 'steel', 'ice', 'dark'],
                             'weak': ['flying', 'poison', 'psychic', 'bug', 'fairy'], 'null': ['ghost']}
effectiveness['poison'] = {'strong': ['grass', 'fairy'], 'weak': ['poison', 'ground', 'rock', 'ghost'], 'null': ['steel']}
effectiveness['ground'] = {'strong': ['poison', 'rock', 'steel',
                                      'fire', 'electric'], 'weak': ['bug', 'grass'], 'null': ['flying']}
effectiveness['flying'] = {'strong': ['fighting', 'bug', 'grass'], 'weak': ['rock', 'steel', 'electric'], 'null': []}
effectiveness['psychic'] = {'strong': ['fighting', 'poison'], 'weak': ['steel', 'psychic'], 'null': ['dark']}
effectiveness['bug'] = {'strong': ['grass', 'psychic', 'dark'], 'weak': [
    'fighting', 'flying', 'poison', 'ghost', 'steel', 'fire', 'fairy'], 'null': []}
effectiveness['rock'] = {'strong': ['flying', 'bug', 'fire', 'ice'], 'weak': ['fighting', 'ground', 'steel'], 'null': []}
effectiveness['ghost'] = {'strong': ['ghost', 'psychic'], 'weak': ['dark'], 'null': ['normal']}
effectiveness['dragon'] = {'strong': ['dragon'], 'weak': ['steel'], 'null': ['fairy']}
effectiveness['dark'] = {'strong': ['ghost', 'psychic'], 'weak': ['fighting', 'dark', 'fairy'], 'null': []}
effectiveness['steel'] = {'strong': ['rock', 'ice', 'fairy'], 'weak': ['steel', 'fire', 'water', 'electric'], 'null': []}
effectiveness['fairy'] = {'strong': ['fighting', 'dragon', 'dark'], 'weak': ['poison', 'steel', 'fire'], 'null': []}

for srcType in types:
    for targetType in types:
        if targetType in effectiveness[srcType]['strong']:
            typeEff[srcType, targetType] = 2
        elif targetType in effectiveness[srcType]['weak']:
            typeEff[srcType, targetType] = 0.5
        elif targetType in effectiveness[srcType]['null']:
            typeEff[srcType, targetType] = 0
        else:
            typeEff[srcType, targetType] = 1
