class BasePokemon:
    def __init__(self, name, type, baseStats, baseExperience, experienceType, learnedMoves, tmMoves, eggMoves):
        self.name = name
        self.type = type
        self.baseStats = baseStats
        self.baseExperience = baseExperience
        self.experienceType = experienceType
        self.learnedMoves = learnedMoves
        self.tmMoves = tmMoves
        self.eggMoves = eggMoves

basePokemonList = {
    'bulbasaur': BasePokemon('bulbasaur', 'grass', 'poison', {'hp': 45, 'atk': 49, 'def': 49, 'spAtk': 65, 'spDef': 65, 'speed': 45}, 'medium slow'),
    'ivysaur': BasePokemon('ivysaur', 'grass', 'poison', {'hp': 60, 'atk': 62, 'def': 63, 'spAtk': 80, 'spDef': 80, 'speed': 60}, 'medium slow'),
    'venusaur': BasePokemon('venusaur', 'grass', 'poison', {'hp': 80, 'atk': 82, 'def': 83, 'spAtk': 100, 'spDef': 100, 'speed': 80}, 'medium slow'),
    'charmander': BasePokemon('charmander', 'fire', '', {'hp': 39, 'atk': 52, 'def': 43, 'spAtk': 60, 'spDef': 50, 'speed': 65}, 'medium slow'),
    'charmeleon': BasePokemon('charmeleon', 'fire', '', {'hp': 58, 'atk': 64, 'def': 58, 'spAtk': 80, 'spDef': 65, 'speed': 80}, 'medium slow'),
    'charizard': BasePokemon('charizard', 'fire', 'flying', {'hp': 78, 'atk': 84, 'def': 78, 'spAtk': 109, 'spDef': 85, 'speed': 100}, 'medium slow'),
    'squirtle': BasePokemon('squirtle', 'water', '', {'hp': 44, 'atk': 48, 'def': 65, 'spAtk': 50, 'spDef': 64, 'speed': 43}, 'medium slow'),
    'wartortle': BasePokemon('wartortle', 'water', '', {'hp': 59, 'atk': 63, 'def': 80, 'spAtk': 65, 'spDef': 80, 'speed': 58}, 'medium slow'),
    'blastoise': BasePokemon('blastoise', 'water', '', {'hp': 79, 'atk': 83, 'def': 100, 'spAtk': 85, 'spDef': 105, 'speed': 78}, 'medium slow'),
    'caterpie': BasePokemon('caterpie', 'bug', '', {'hp': 45, 'atk': 30, 'def': 35, 'spAtk': 20, 'spDef': 20, 'speed': 45}, 'medium fast'),
    'metapod': BasePokemon('metapod', 'bug', '', {'hp': 50, 'atk': 20, 'def': 55, 'spAtk': 25, 'spDef': 25, 'speed': 30}, 'medium fast'),
    'butterfree': BasePokemon('butterfree', 'bug', 'flying', {'hp': 60, 'atk': 45, 'def': 50, 'spAtk': 90, 'spDef': 80, 'speed': 70}, 'medium fast'),
    'weedle': BasePokemon('weedle', 'bug', 'poison', {'hp': 40, 'atk': 35, 'def': 30, 'spAtk': 20, 'spDef': 20, 'speed': 50}, 'medium fast'),
    'kakuna': BasePokemon('kakuna', 'bug', 'poison', {'hp': 45, 'atk': 25, 'def': 50, 'spAtk': 25, 'spDef': 25, 'speed': 35}, 'medium fast'),
    'beedrill': BasePokemon('beedrill', 'bug', 'poison', {'hp': 65, 'atk': 90, 'def': 40, 'spAtk': 45, 'spDef': 80, 'speed': 75}, 'medium fast'),
    'pidgey': BasePokemon('pidgey', 'normal', 'flying', {'hp': 40, 'atk': 45, 'def': 40, 'spAtk': 35, 'spDef': 35, 'speed': 56}, 'medium slow'),
    'pidgeotto': BasePokemon('pidgeotto', 'normal', 'flying', {'hp': 63, 'atk': 60, 'def': 55, 'spAtk': 50, 'spDef': 50, 'speed': 71}, 'medium slow'),
    'pidgeot': BasePokemon('pidgeot', 'normal', 'flying', {'hp': 83, 'atk': 80, 'def': 75, 'spAtk': 70, 'spDef': 70, 'speed': 101}, 'medium slow'),
    'rattata': BasePokemon('rattata', 'normal', '', {'hp': 30, 'atk': 56, 'def': 35, 'spAtk': 25, 'spDef': 35, 'speed': 72}, 'medium fast'),
    'raticate': BasePokemon('raticate', 'normal', '', {'hp': 55, 'atk': 81, 'def': 60, 'spAtk': 50, 'spDef': 70, 'speed': 97}, 'medium fast'),
    'spearow': BasePokemon('spearow', 'normal', 'flying', {'hp': 40, 'atk': 60, 'def': 30, 'spAtk': 31, 'spDef': 31, 'speed': 70}, 'medium fast'),
    'fearow': BasePokemon('fearow', 'normal', 'flying', {'hp': 65, 'atk': 90, 'def': 65, 'spAtk': 61, 'spDef': 61, 'speed': 100}, 'medium fast'),
    'ekans': BasePokemon('ekans', 'poison', '', {'hp': 35, 'atk': 60, 'def': 44, 'spAtk': 40, 'spDef': 54, 'speed': 55}, 'medium fast'),
    'arbok': BasePokemon('arbok', 'poison', '', {'hp': 60, 'atk': 85, 'def': 69, 'spAtk': 65, 'spDef': 79, 'speed': 80}, 'medium fast'),
    'pikachu': BasePokemon('pikachu', 'electric', '', {'hp': 35, 'atk': 55, 'def': 40, 'spAtk': 50, 'spDef': 50, 'speed': 90}, 'medium fast'),
    'raichu': BasePokemon('raichu', 'electric', '', {'hp': 60, 'atk': 90, 'def': 55, 'spAtk': 90, 'spDef': 80, 'speed': 110}, 'medium fast'),
    'sandshrew': BasePokemon('sandshrew', 'ground', '', {'hp': 50, 'atk': 75, 'def': 85, 'spAtk': 20, 'spDef': 30, 'speed': 40}, 'medium fast'),
    'sandslash': BasePokemon('sandslash', 'ground', '', {'hp': 75, 'atk': 100, 'def': 110, 'spAtk': 45, 'spDef': 55, 'speed': 65}, 'medium fast'),
    'nidoran (f),': BasePokemon('nidoran (f),', 'poison', '', {'hp': 55, 'atk': 47, 'def': 52, 'spAtk': 40, 'spDef': 40, 'speed': 41}, 'medium slow'),
    'nidorina': BasePokemon('nidorina', 'poison', '', {'hp': 70, 'atk': 62, 'def': 67, 'spAtk': 55, 'spDef': 55, 'speed': 56}, 'medium slow'),
    'nidoqueen': BasePokemon('nidoqueen', 'poison', 'ground', {'hp': 90, 'atk': 92, 'def': 87, 'spAtk': 75, 'spDef': 85, 'speed': 76}, 'medium slow'),
    'nidoran (m),': BasePokemon('nidoran (m),', 'poison', '', {'hp': 46, 'atk': 57, 'def': 40, 'spAtk': 40, 'spDef': 40, 'speed': 50}, 'medium slow'),
    'nidorino': BasePokemon('nidorino', 'poison', '', {'hp': 61, 'atk': 72, 'def': 57, 'spAtk': 55, 'spDef': 55, 'speed': 65}, 'medium slow'),
    'nidoking': BasePokemon('nidoking', 'poison', 'ground', {'hp': 81, 'atk': 102, 'def': 77, 'spAtk': 85, 'spDef': 75, 'speed': 85}, 'medium slow'),
    'clefairy': BasePokemon('clefairy', 'fairy', '', {'hp': 70, 'atk': 45, 'def': 48, 'spAtk': 60, 'spDef': 65, 'speed': 35}, 'fast'),
    'clefable': BasePokemon('clefable', 'fairy', '', {'hp': 95, 'atk': 70, 'def': 73, 'spAtk': 95, 'spDef': 90, 'speed': 60}, 'fast'),
    'vulpix': BasePokemon('vulpix', 'fire', '', {'hp': 38, 'atk': 41, 'def': 40, 'spAtk': 50, 'spDef': 65, 'speed': 65}, 'medium fast'),
    'ninetales': BasePokemon('ninetales', 'fire', '', {'hp': 73, 'atk': 76, 'def': 75, 'spAtk': 81, 'spDef': 100, 'speed': 100}, 'medium fast'),
    'jigglypuff': BasePokemon('jigglypuff', 'normal', 'fairy', {'hp': 115, 'atk': 45, 'def': 20, 'spAtk': 45, 'spDef': 25, 'speed': 20}, 'fast'),
    'wigglytuff': BasePokemon('wigglytuff', 'normal', 'fairy', {'hp': 140, 'atk': 70, 'def': 45, 'spAtk': 85, 'spDef': 50, 'speed': 45}, 'fast'),
    'zubat': BasePokemon('zubat', 'poison', 'flying', {'hp': 40, 'atk': 45, 'def': 35, 'spAtk': 30, 'spDef': 40, 'speed': 55}, 'medium fast'),
    'golbat': BasePokemon('golbat', 'poison', 'flying', {'hp': 75, 'atk': 80, 'def': 70, 'spAtk': 65, 'spDef': 75, 'speed': 90}, 'medium fast'),
    'oddish': BasePokemon('oddish', 'grass', 'poison', {'hp': 45, 'atk': 50, 'def': 55, 'spAtk': 75, 'spDef': 65, 'speed': 30}, 'medium slow'),
    'gloom': BasePokemon('gloom', 'grass', 'poison', {'hp': 60, 'atk': 65, 'def': 70, 'spAtk': 85, 'spDef': 75, 'speed': 40}, 'medium slow'),
    'vileplume': BasePokemon('vileplume', 'grass', 'poison', {'hp': 75, 'atk': 80, 'def': 85, 'spAtk': 110, 'spDef': 90, 'speed': 50}, 'medium slow'),
    'paras': BasePokemon('paras', 'bug', 'grass', {'hp': 35, 'atk': 70, 'def': 55, 'spAtk': 45, 'spDef': 55, 'speed': 25}, 'medium fast'),
    'parasect': BasePokemon('parasect', 'bug', 'grass', {'hp': 60, 'atk': 95, 'def': 80, 'spAtk': 60, 'spDef': 80, 'speed': 30}, 'medium fast'),
    'venonat': BasePokemon('venonat', 'bug', 'poison', {'hp': 60, 'atk': 55, 'def': 50, 'spAtk': 40, 'spDef': 55, 'speed': 45}, 'medium fast'),
    'venomoth': BasePokemon('venomoth', 'bug', 'poison', {'hp': 70, 'atk': 65, 'def': 60, 'spAtk': 90, 'spDef': 75, 'speed': 90}, 'medium fast'),
    'diglett': BasePokemon('diglett', 'ground', '', {'hp': 10, 'atk': 55, 'def': 25, 'spAtk': 35, 'spDef': 45, 'speed': 95}, 'medium fast'),
    'dugtrio': BasePokemon('dugtrio', 'ground', '', {'hp': 35, 'atk': 80, 'def': 50, 'spAtk': 50, 'spDef': 70, 'speed': 120}, 'medium fast'),
    'meowth': BasePokemon('meowth', 'normal', '', {'hp': 40, 'atk': 45, 'def': 35, 'spAtk': 40, 'spDef': 40, 'speed': 90}, 'medium fast'),
    'persian': BasePokemon('persian', 'normal', '', {'hp': 65, 'atk': 70, 'def': 60, 'spAtk': 65, 'spDef': 65, 'speed': 115}, 'medium fast'),
    'psyduck': BasePokemon('psyduck', 'water', '', {'hp': 50, 'atk': 52, 'def': 48, 'spAtk': 65, 'spDef': 50, 'speed': 55}, 'medium fast'),
    'golduck': BasePokemon('golduck', 'water', '', {'hp': 80, 'atk': 82, 'def': 78, 'spAtk': 95, 'spDef': 80, 'speed': 85}, 'medium fast'),
    'mankey': BasePokemon('mankey', 'fighting', '', {'hp': 40, 'atk': 80, 'def': 35, 'spAtk': 35, 'spDef': 45, 'speed': 70}, 'medium fast'),
    'primeape': BasePokemon('primeape', 'fighting', '', {'hp': 65, 'atk': 105, 'def': 60, 'spAtk': 60, 'spDef': 70, 'speed': 95}, 'medium fast'),
    'growlithe': BasePokemon('growlithe', 'fire', '', {'hp': 55, 'atk': 70, 'def': 45, 'spAtk': 70, 'spDef': 50, 'speed': 60}, 'slow'),
    'arcanine': BasePokemon('arcanine', 'fire', '', {'hp': 90, 'atk': 110, 'def': 80, 'spAtk': 100, 'spDef': 80, 'speed': 95}, 'slow'),
    'poliwag': BasePokemon('poliwag', 'water', '', {'hp': 40, 'atk': 50, 'def': 40, 'spAtk': 40, 'spDef': 40, 'speed': 90}, 'medium slow'),
    'poliwhirl': BasePokemon('poliwhirl', 'water', '', {'hp': 65, 'atk': 65, 'def': 65, 'spAtk': 50, 'spDef': 50, 'speed': 90}, 'medium slow'),
    'poliwrath': BasePokemon('poliwrath', 'water', 'fighting', {'hp': 90, 'atk': 95, 'def': 95, 'spAtk': 70, 'spDef': 90, 'speed': 70}, 'medium slow'),
    'abra': BasePokemon('abra', 'psychic', '', {'hp': 25, 'atk': 20, 'def': 15, 'spAtk': 105, 'spDef': 55, 'speed': 90}, 'medium slow'),
    'kadabra': BasePokemon('kadabra', 'psychic', '', {'hp': 40, 'atk': 35, 'def': 30, 'spAtk': 120, 'spDef': 70, 'speed': 105}, 'medium slow'),
    'alakazam': BasePokemon('alakazam', 'psychic', '', {'hp': 55, 'atk': 50, 'def': 45, 'spAtk': 135, 'spDef': 95, 'speed': 120}, 'medium slow'),
    'machop': BasePokemon('machop', 'fighting', '', {'hp': 70, 'atk': 80, 'def': 50, 'spAtk': 35, 'spDef': 35, 'speed': 35}, 'medium slow'),
    'machoke': BasePokemon('machoke', 'fighting', '', {'hp': 80, 'atk': 100, 'def': 70, 'spAtk': 50, 'spDef': 60, 'speed': 45}, 'medium slow'),
    'machamp': BasePokemon('machamp', 'fighting', '', {'hp': 90, 'atk': 130, 'def': 80, 'spAtk': 65, 'spDef': 85, 'speed': 55}, 'medium slow'),
    'bellsprout': BasePokemon('bellsprout', 'grass', 'poison', {'hp': 50, 'atk': 75, 'def': 35, 'spAtk': 70, 'spDef': 30, 'speed': 40}, 'medium slow'),
    'weepinbell': BasePokemon('weepinbell', 'grass', 'poison', {'hp': 65, 'atk': 90, 'def': 50, 'spAtk': 85, 'spDef': 45, 'speed': 55}, 'medium slow'),
    'victreebel': BasePokemon('victreebel', 'grass', 'poison', {'hp': 80, 'atk': 105, 'def': 65, 'spAtk': 100, 'spDef': 70, 'speed': 70}, 'medium slow'),
    'tentacool': BasePokemon('tentacool', 'water', 'poison', {'hp': 40, 'atk': 40, 'def': 35, 'spAtk': 50, 'spDef': 100, 'speed': 70}, 'slow'),
    'tentacruel': BasePokemon('tentacruel', 'water', 'poison', {'hp': 80, 'atk': 70, 'def': 65, 'spAtk': 80, 'spDef': 120, 'speed': 100}, 'slow'),
    'geodude': BasePokemon('geodude', 'rock', 'ground', {'hp': 40, 'atk': 80, 'def': 100, 'spAtk': 30, 'spDef': 30, 'speed': 20}, 'medium slow'),
    'graveler': BasePokemon('graveler', 'rock', 'ground', {'hp': 55, 'atk': 95, 'def': 115, 'spAtk': 45, 'spDef': 45, 'speed': 35}, 'medium slow'),
    'golem': BasePokemon('golem', 'rock', 'ground', {'hp': 80, 'atk': 120, 'def': 130, 'spAtk': 55, 'spDef': 65, 'speed': 45}, 'medium slow'),
    'ponyta': BasePokemon('ponyta', 'fire', '', {'hp': 50, 'atk': 85, 'def': 55, 'spAtk': 65, 'spDef': 65, 'speed': 90}, 'medium fast'),
    'rapidash': BasePokemon('rapidash', 'fire', '', {'hp': 65, 'atk': 100, 'def': 70, 'spAtk': 80, 'spDef': 80, 'speed': 105}, 'medium fast'),
    'slowpoke': BasePokemon('slowpoke', 'water', 'psychic', {'hp': 90, 'atk': 65, 'def': 65, 'spAtk': 40, 'spDef': 40, 'speed': 15}, 'medium fast'),
    'slowbro': BasePokemon('slowbro', 'water', 'psychic', {'hp': 95, 'atk': 75, 'def': 110, 'spAtk': 100, 'spDef': 80, 'speed': 30}, 'medium fast'),
    'magnemite': BasePokemon('magnemite', 'electric', 'steel', {'hp': 25, 'atk': 35, 'def': 70, 'spAtk': 95, 'spDef': 55, 'speed': 45}, 'medium fast'),
    'magneton': BasePokemon('magneton', 'electric', 'steel', {'hp': 50, 'atk': 60, 'def': 95, 'spAtk': 120, 'spDef': 70, 'speed': 70}, 'medium fast'),
    'farfetch\'d': BasePokemon('farfetch\'d', 'normal', 'flying', {'hp': 52, 'atk': 65, 'def': 55, 'spAtk': 58, 'spDef': 62, 'speed': 60}, 'medium fast'),
    'doduo': BasePokemon('doduo', 'normal', 'flying', {'hp': 35, 'atk': 85, 'def': 45, 'spAtk': 35, 'spDef': 35, 'speed': 75}, 'medium fast'),
    'dodrio': BasePokemon('dodrio', 'normal', 'flying', {'hp': 60, 'atk': 110, 'def': 70, 'spAtk': 60, 'spDef': 60, 'speed': 100}, 'medium fast'),
    'seel': BasePokemon('seel', 'water', '', {'hp': 65, 'atk': 45, 'def': 55, 'spAtk': 45, 'spDef': 70, 'speed': 45}, 'medium fast'),
    'dewgong': BasePokemon('dewgong', 'water', 'ice', {'hp': 90, 'atk': 70, 'def': 80, 'spAtk': 70, 'spDef': 95, 'speed': 70}, 'medium fast'),
    'grimer': BasePokemon('grimer', 'poison', '', {'hp': 80, 'atk': 80, 'def': 50, 'spAtk': 40, 'spDef': 50, 'speed': 25}, 'medium fast'),
    'muk': BasePokemon('muk', 'poison', '', {'hp': 105, 'atk': 105, 'def': 75, 'spAtk': 65, 'spDef': 100, 'speed': 50}, 'medium fast'),
    'shellder': BasePokemon('shellder', 'water', '', {'hp': 30, 'atk': 65, 'def': 100, 'spAtk': 45, 'spDef': 25, 'speed': 40}, 'slow'),
    'cloyster': BasePokemon('cloyster', 'water', 'ice', {'hp': 50, 'atk': 95, 'def': 180, 'spAtk': 85, 'spDef': 45, 'speed': 70}, 'slow'),
    'gastly': BasePokemon('gastly', 'ghost', 'poison', {'hp': 30, 'atk': 35, 'def': 30, 'spAtk': 100, 'spDef': 35, 'speed': 80}, 'medium slow'),
    'haunter': BasePokemon('haunter', 'ghost', 'poison', {'hp': 45, 'atk': 50, 'def': 45, 'spAtk': 115, 'spDef': 55, 'speed': 95}, 'medium slow'),
    'gengar': BasePokemon('gengar', 'ghost', 'poison', {'hp': 60, 'atk': 65, 'def': 60, 'spAtk': 130, 'spDef': 75, 'speed': 110}, 'medium slow'),
    'onix': BasePokemon('onix', 'rock', 'ground', {'hp': 35, 'atk': 45, 'def': 160, 'spAtk': 30, 'spDef': 45, 'speed': 70}, 'medium fast'),
    'drowzee': BasePokemon('drowzee', 'psychic', '', {'hp': 60, 'atk': 48, 'def': 45, 'spAtk': 43, 'spDef': 90, 'speed': 42}, 'medium fast'),
    'hypno': BasePokemon('hypno', 'psychic', '', {'hp': 85, 'atk': 73, 'def': 70, 'spAtk': 73, 'spDef': 115, 'speed': 67}, 'medium fast'),
    'krabby': BasePokemon('krabby', 'water', '', {'hp': 30, 'atk': 105, 'def': 90, 'spAtk': 25, 'spDef': 25, 'speed': 50}, 'medium fast'),
    'kingler': BasePokemon('kingler', 'water', '', {'hp': 55, 'atk': 130, 'def': 115, 'spAtk': 50, 'spDef': 50, 'speed': 75}, 'medium fast'),
    'voltorb': BasePokemon('voltorb', 'electric', '', {'hp': 40, 'atk': 30, 'def': 50, 'spAtk': 55, 'spDef': 55, 'speed': 100}, 'medium fast'),
    'electrode': BasePokemon('electrode', 'electric', '', {'hp': 60, 'atk': 50, 'def': 70, 'spAtk': 80, 'spDef': 80, 'speed': 140}, 'medium fast'),
    'exeggcute': BasePokemon('exeggcute', 'grass', 'psychic', {'hp': 60, 'atk': 40, 'def': 80, 'spAtk': 60, 'spDef': 45, 'speed': 40}, 'slow'),
    'exeggutor': BasePokemon('exeggutor', 'grass', 'psychic', {'hp': 95, 'atk': 95, 'def': 85, 'spAtk': 125, 'spDef': 65, 'speed': 55}, 'slow'),
    'cubone': BasePokemon('cubone', 'ground', '', {'hp': 50, 'atk': 50, 'def': 95, 'spAtk': 40, 'spDef': 50, 'speed': 35}, 'medium fast'),
    'marowak': BasePokemon('marowak', 'ground', '', {'hp': 60, 'atk': 80, 'def': 110, 'spAtk': 50, 'spDef': 80, 'speed': 45}, 'medium fast'),
    'hitmonlee': BasePokemon('hitmonlee', 'fighting', '', {'hp': 50, 'atk': 120, 'def': 53, 'spAtk': 35, 'spDef': 110, 'speed': 87}, 'medium fast'),
    'hitmonchan': BasePokemon('hitmonchan', 'fighting', '', {'hp': 50, 'atk': 105, 'def': 79, 'spAtk': 35, 'spDef': 110, 'speed': 76}, 'medium fast'),
    'lickitung': BasePokemon('lickitung', 'normal', '', {'hp': 90, 'atk': 55, 'def': 75, 'spAtk': 60, 'spDef': 75, 'speed': 30}, 'medium fast'),
    'koffing': BasePokemon('koffing', 'poison', '', {'hp': 40, 'atk': 65, 'def': 95, 'spAtk': 60, 'spDef': 45, 'speed': 35}, 'medium fast'),
    'weezing': BasePokemon('weezing', 'poison', '', {'hp': 65, 'atk': 90, 'def': 120, 'spAtk': 85, 'spDef': 70, 'speed': 60}, 'medium fast'),
    'rhyhorn': BasePokemon('rhyhorn', 'ground', 'rock', {'hp': 80, 'atk': 85, 'def': 95, 'spAtk': 30, 'spDef': 30, 'speed': 25}, 'slow'),
    'rhydon': BasePokemon('rhydon', 'ground', 'rock', {'hp': 105, 'atk': 130, 'def': 120, 'spAtk': 45, 'spDef': 45, 'speed': 40}, 'slow'),
    'chansey': BasePokemon('chansey', 'normal', '', {'hp': 250, 'atk': 5, 'def': 5, 'spAtk': 35, 'spDef': 105, 'speed': 50}, 'fast'),
    'tangela': BasePokemon('tangela', 'grass', '', {'hp': 65, 'atk': 55, 'def': 115, 'spAtk': 100, 'spDef': 40, 'speed': 60}, 'medium fast'),
    'kangaskhan': BasePokemon('kangaskhan', 'normal', '', {'hp': 105, 'atk': 95, 'def': 80, 'spAtk': 40, 'spDef': 80, 'speed': 90}, 'medium fast'),
    'horsea': BasePokemon('horsea', 'water', '', {'hp': 30, 'atk': 40, 'def': 70, 'spAtk': 70, 'spDef': 25, 'speed': 60}, 'medium fast'),
    'seadra': BasePokemon('seadra', 'water', '', {'hp': 55, 'atk': 65, 'def': 95, 'spAtk': 95, 'spDef': 45, 'speed': 85}, 'medium fast'),
    'goldeen': BasePokemon('goldeen', 'water', '', {'hp': 45, 'atk': 67, 'def': 60, 'spAtk': 35, 'spDef': 50, 'speed': 63}, 'medium fast'),
    'seaking': BasePokemon('seaking', 'water', '', {'hp': 80, 'atk': 92, 'def': 65, 'spAtk': 65, 'spDef': 80, 'speed': 68}, 'medium fast'),
    'staryu': BasePokemon('staryu', 'water', '', {'hp': 30, 'atk': 45, 'def': 55, 'spAtk': 70, 'spDef': 55, 'speed': 85}, 'slow'),
    'starmie': BasePokemon('starmie', 'water', 'psychic', {'hp': 60, 'atk': 75, 'def': 85, 'spAtk': 100, 'spDef': 85, 'speed': 115}, 'slow'),
    'mr. mime': BasePokemon('mr. mime', 'psychic', 'fairy', {'hp': 40, 'atk': 45, 'def': 65, 'spAtk': 100, 'spDef': 120, 'speed': 90}, 'medium fast'),
    'scyther': BasePokemon('scyther', 'bug', 'flying', {'hp': 70, 'atk': 110, 'def': 80, 'spAtk': 55, 'spDef': 80, 'speed': 105}, 'medium fast'),
    'jynx': BasePokemon('jynx', 'ice', 'psychic', {'hp': 65, 'atk': 50, 'def': 35, 'spAtk': 115, 'spDef': 95, 'speed': 95}, 'medium fast'),
    'electabuzz': BasePokemon('electabuzz', 'electric', '', {'hp': 65, 'atk': 83, 'def': 57, 'spAtk': 95, 'spDef': 85, 'speed': 105}, 'medium fast'),
    'magmar': BasePokemon('magmar', 'fire', '', {'hp': 65, 'atk': 95, 'def': 57, 'spAtk': 100, 'spDef': 85, 'speed': 93}, 'medium fast'),
    'pinsir': BasePokemon('pinsir', 'bug', '', {'hp': 65, 'atk': 125, 'def': 100, 'spAtk': 55, 'spDef': 70, 'speed': 85}, 'slow'),
    'tauros': BasePokemon('tauros', 'normal', '', {'hp': 75, 'atk': 100, 'def': 95, 'spAtk': 40, 'spDef': 70, 'speed': 110}, 'slow'),
    'magikarp': BasePokemon('magikarp', 'water', '', {'hp': 20, 'atk': 10, 'def': 55, 'spAtk': 15, 'spDef': 20, 'speed': 80}, 'slow'),
    'gyarados': BasePokemon('gyarados', 'water', 'flying', {'hp': 95, 'atk': 125, 'def': 79, 'spAtk': 60, 'spDef': 100, 'speed': 81}, 'slow'),
    'lapras': BasePokemon('lapras', 'water', 'ice', {'hp': 130, 'atk': 85, 'def': 80, 'spAtk': 85, 'spDef': 95, 'speed': 60}, 'slow'),
    'ditto': BasePokemon('ditto', 'normal', '', {'hp': 48, 'atk': 48, 'def': 48, 'spAtk': 48, 'spDef': 48, 'speed': 48}, 'medium fast'),
    'eevee': BasePokemon('eevee', 'normal', '', {'hp': 55, 'atk': 55, 'def': 50, 'spAtk': 45, 'spDef': 65, 'speed': 55}, 'medium fast'),
    'vaporeon': BasePokemon('vaporeon', 'water', '', {'hp': 130, 'atk': 65, 'def': 60, 'spAtk': 110, 'spDef': 95, 'speed': 65}, 'medium fast'),
    'jolteon': BasePokemon('jolteon', 'electric', '', {'hp': 65, 'atk': 65, 'def': 60, 'spAtk': 110, 'spDef': 95, 'speed': 130}, 'medium fast'),
    'flareon': BasePokemon('flareon', 'fire', '', {'hp': 65, 'atk': 130, 'def': 60, 'spAtk': 95, 'spDef': 110, 'speed': 65}, 'medium fast'),
    'porygon': BasePokemon('porygon', 'normal', '', {'hp': 65, 'atk': 60, 'def': 70, 'spAtk': 85, 'spDef': 75, 'speed': 40}, 'medium fast'),
    'omanyte': BasePokemon('omanyte', 'rock', 'water', {'hp': 35, 'atk': 40, 'def': 100, 'spAtk': 90, 'spDef': 55, 'speed': 35}, 'medium fast'),
    'omastar': BasePokemon('omastar', 'rock', 'water', {'hp': 70, 'atk': 60, 'def': 125, 'spAtk': 115, 'spDef': 70, 'speed': 55}, 'medium fast'),
    'kabuto': BasePokemon('kabuto', 'rock', 'water', {'hp': 30, 'atk': 80, 'def': 90, 'spAtk': 55, 'spDef': 45, 'speed': 55}, 'medium fast'),
    'kabutops': BasePokemon('kabutops', 'rock', 'water', {'hp': 60, 'atk': 115, 'def': 105, 'spAtk': 65, 'spDef': 70, 'speed': 80}, 'medium fast'),
    'aerodactyl': BasePokemon('aerodactyl', 'rock', 'flying', {'hp': 80, 'atk': 105, 'def': 65, 'spAtk': 60, 'spDef': 75, 'speed': 130}, 'slow'),
    'snorlax': BasePokemon('snorlax', 'normal', '', {'hp': 160, 'atk': 110, 'def': 65, 'spAtk': 65, 'spDef': 110, 'speed': 30}, 'slow'),
    'articuno': BasePokemon('articuno', 'ice', 'flying', {'hp': 90, 'atk': 85, 'def': 100, 'spAtk': 95, 'spDef': 125, 'speed': 85}, 'slow'),
    'zapdos': BasePokemon('zapdos', 'electric', 'flying', {'hp': 90, 'atk': 90, 'def': 85, 'spAtk': 125, 'spDef': 90, 'speed': 100}, 'slow'),
    'moltres': BasePokemon('moltres', 'fire', 'flying', {'hp': 90, 'atk': 100, 'def': 90, 'spAtk': 125, 'spDef': 85, 'speed': 90}, 'slow'),
    'dratini': BasePokemon('dratini', 'dragon', '', {'hp': 41, 'atk': 64, 'def': 45, 'spAtk': 50, 'spDef': 50, 'speed': 50}, 'slow'),
    'dragonair': BasePokemon('dragonair', 'dragon', '', {'hp': 61, 'atk': 84, 'def': 65, 'spAtk': 70, 'spDef': 70, 'speed': 70}, 'slow'),
    'dragonite': BasePokemon('dragonite', 'dragon', 'flying', {'hp': 91, 'atk': 134, 'def': 95, 'spAtk': 100, 'spDef': 100, 'speed': 80}, 'slow'),
    'mewtwo': BasePokemon('mewtwo', 'psychic', '', {'hp': 106, 'atk': 110, 'def': 90, 'spAtk': 154, 'spDef': 90, 'speed': 130}, 'slow'),
    'mew': BasePokemon('mew', 'psychic', '', {'hp': 100, 'atk': 100, 'def': 100, 'spAtk': 100, 'spDef': 100, 'speed': 100}, 'medium slow')
}
