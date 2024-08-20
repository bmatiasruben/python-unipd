from time import sleep
from Libraries.Pokemon import Pokemon
from Libraries.PokemonSprites import *
from Libraries.BasePokemon import basePokemon
from Libraries.Moves import *
from tabulate import tabulate

def printOakStart():
    print('Hello there! Welcome to the world of pokemon!')
    sleep(1)
    print('My name is Oak! Pleople call me the pokemon Prof!')
    sleep(1)
    print('This world is inhabited by creatures called pokemon!')
    sleep(1)
    print('For some people, pokemon are pets. Other use them for fights')
    sleep(1)
    print('Myself... I study pokemon as a profession.')
    sleep(1)
    print('')
    sleep(1)
    print('This is the beggining of your own adventure...')
    sleep(1)

def printBattleUi(mainPkmn: Pokemon, opponentPkmn: Pokemon):
    print('__________________________________________')
    opponentSqrLen = len(opponentPkmn.name) + len(str(opponentPkmn.maxHp)) + len(str(opponentPkmn.currentHp)) + 4
    opponentSqrH = '_'*opponentSqrLen
    print(f'                      {opponentSqrH}')
    print(f'                      |{opponentPkmn.name.capitalize()} {opponentPkmn.currentHp}/{opponentPkmn.maxHp}|')
    opponentSqrH = '‾'*opponentSqrLen
    print(f'                      {opponentSqrH}')
    mainSqrLen = len(mainPkmn.name) + len(str(mainPkmn.maxHp)) + len(str(mainPkmn.currentHp)) + 4
    mainSqrH = '_'*mainSqrLen
    print(f'{mainSqrH}')
    print(f'|{mainPkmn.name.capitalize()} {mainPkmn.currentHp}/{mainPkmn.maxHp}|')
    mainSqrH = '‾'*mainSqrLen
    print(f'{mainSqrH}')
    print('______________________')
    print('|0: Fight  | 1: Items|')
    print('|2: Pokemon| 3: Run  |')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')

def printReducedBattleUi(mainPkmn: Pokemon, opponentPkmn: Pokemon):
    print('__________________________________________')
    opponentSqrLen = len(opponentPkmn.name) + len(str(opponentPkmn.maxHp)) + len(str(opponentPkmn.currentHp)) + 4
    opponentSqrH = '_'*opponentSqrLen
    print(f'                      {opponentSqrH}')
    print(f'                      |{opponentPkmn.name.capitalize()} {opponentPkmn.currentHp}/{opponentPkmn.maxHp}|')
    opponentSqrH = '‾'*opponentSqrLen
    print(f'                      {opponentSqrH}')
    mainSqrLen = len(mainPkmn.name) + len(str(mainPkmn.maxHp)) + len(str(mainPkmn.currentHp)) + 4
    mainSqrH = '_'*mainSqrLen
    print(f'{mainSqrH}')
    print(f'|{mainPkmn.name.capitalize()} {mainPkmn.currentHp}/{mainPkmn.maxHp}|')
    mainSqrH = '‾'*mainSqrLen
    print(f'{mainSqrH}')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')

def printPokemonSummary(pokemon: Pokemon):
    print(get_ascii_pokemon(basePokemon[pokemon.name].pokedexNumber))
    print('-----------------------------------------------')
    print(f'{pokemon.name.capitalize()}, Level {pokemon.level}')
    print(f'HP: {pokemon.currentHp}/{pokemon.maxHp}')
    print('Moves:')
    for move in pokemon.moves:
        print(f'  - {move.name}, PP:{move.pp}/{moveList[move.name].pp}')
    table = [['stat', 'IV', 'EV']]
    for stat in list(pokemon.currentStats):
        table.append([stat, f'{pokemon.indivValues[stat]}/31', f'{pokemon.effortValues[stat]}'])
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

def printBattleMoves(pokemon: Pokemon):
    for index, move in enumerate(pokemon.moves):
        moveString = f' {move.name}, Type: {move.type}, PP: {move.pp}/{moveList[move.name].pp}'
        if move.category != 'status':
            if hasattr(move, 'power'):
                moveString += f', power: {move.power}'
            else:
                moveString += ', power: OHKO'
            if hasattr(move, 'accuracy'):
                moveString += f', accuracy: {move.accuracy}'
            else:
                moveString += ', accuracy: auto-hit'
        else:
            moveString += ', status'
        print(index, ': ', moveString)

def printFirstStart():
    print('Hello there! Welcome to the world of pokemon!')
    sleep(1)
    print('This here is just a test for the Pokemon, Pokemon Trainer, and Move classes')
    sleep(1)
    print('Indeed! You are not in the real world, this is just a Python program')
    sleep(1)
    print('What? What\'s Python? Who am I? Where is your family?')
    sleep(1)
    print('No time for that! Save your existential crisis for later!')
    sleep(1)
    print('Let\'s test some pokemon shall, we?')
    sleep(1)

def printPokemonList(character):
    for index, pokemon in enumerate(character.pokemon):
        print(index, ': ', pokemon.name, ', Level: ', pokemon.level)

def printItems(character):
    for index, item in enumerate(character.items):
        print(index, ': ', item.key, ', Quantity: ', item.quantity)

def printPokeCenter():
    print('Welcome to the Pokemon Center')
    print('Wait while we heal your pokemon')

def printStore():
    print('Welcome to the Pokemon Store')
    print('Although you seem to have no money at all, have these free items!')
    print('Please don\'t come back, you\'ll ruin our business!')