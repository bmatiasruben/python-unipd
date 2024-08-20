from Libraries.PokemonSprites import *
from Libraries.BasePokemon import basePokemonList
from Libraries.PokemonTrainer import PokemonTrainer
from Libraries.Pokemon import Pokemon
from Libraries.Moves import *
import random
from time import sleep
from Libraries.prints import *
from copy import deepcopy
import numpy as np

def createCharacter(string):
    if string == 'fast':
        mainCharacter = PokemonTrainer('Matias', [], [])
        mainCharacter.pokemons.append(deepcopy(Pokemon('bulbasaur', 15)))
        mainCharacter.pokemons.append(deepcopy(Pokemon('pidgey', 1)))
        mainCharacter.pokemons[0].owner = 'mainCharacter'
        mainCharacter.pokemons[1].owner = 'mainCharacter'
    else:
        printOakStart()
        name = input('Please tell me your name: ')
        mainCharacter = PokemonTrainer(name, [], [])
        print(f'Good to meet you {mainCharacter.name}! Let\'s begin!')
        sleep(1)
        options=['bulbasaur', 'charmander', 'squirtle']
        choiceSure = False
        while not choiceSure:
            print('Please select your first pokemon:')
            for i, opt in enumerate(options):
                print(i, ':', opt.capitalize())
            try:
                choice = int(input('Choose your starter: '))
                if choice not in range(len(options)):
                    try:
                        if choice == 3:
                            triedToGet = 'ivysaur'
                        elif choice == 4:
                            triedToGet = 'venusaur'
                        elif choice == 5:
                            triedToGet = 'charmeleon'
                        elif choice == 6:
                            triedToGet = 'charizard'
                        elif choice == 7:
                            triedToGet = 'wartortle'
                        elif choice == 8:
                            triedToGet = 'blastoise'
                        else:
                            triedToGet = list(basePokemonList)[choice + 1]
                        print(f'No cheating! I cannot give you a {triedToGet} as your first pokemon!')
                    except IndexError:
                        print(f'No cheating! This game only has first generation pokemon!')
                    sleep(2)
                else:
                    print(get_ascii_pokemon(basePokemonList[options[choice]].pokedexNumber))
                    while True:
                        sure = input(f'Do you want to choose the {basePokemonList[options[choice]].type[0].capitalize()} type pokemon {options[choice].capitalize()}? (y/n) ')
                        if sure == 'y':
                            mainCharacter.pokemons.append(Pokemon(options[choice], 1))
                            print(f'You obtained the pokemon {options[choice].capitalize()}!')
                            while True:
                                nicknameYN = input(f'Would you like to give {options[choice].capitalize()} a nickname? (y/n) ')
                                if nicknameYN == 'y':
                                    mainCharacter.pokemons[0].nickname = input('Please choose a Nickname: ')
                                    break
                                elif nicknameYN == 'n':
                                    break
                                else:
                                    print('Please choose a valid option.')
                                    continue
                            print(f'{mainCharacter.pokemons[0].nickname} has been added to your party!')
                            choiceSure = True
                            break
                        if sure == 'n':
                            continue
                        else:
                            print('Please choose a valid option.')
                            continue
            except ValueError:
                print('Please choose a valid option. Hint: you should put an integer from 0 to 2')
    mainCharacter.items = {'Pokeball': 10, 'Potion': 10}
    story(mainCharacter)

def story(character):
    options=['Explore', 'Pokemon Center', 'Pokemon Store', 'Check Pokemons', 'Check Items']
    print('What would you like to do?')
    for i, opt in enumerate(options):
        print(i, ':', opt.capitalize())
    try:
        choice = int(input('Choose an option: '))
        if choice not in range(len(options)):
            print('Please choose a valid option.')
            story(character)
        else:
            if choice == 0:
                if random.random() < 0.80:
                    wildBattle(character)
                # Extra possibility to add a 5% chance of finding another trainer. 
                # Trainers will have the same amount of pokemon as the player
                # Still not implemented
                # elif random.random() < 0.85:
                #     print('Hey, you! We made eye contact for a microsecond, let\'s fight!')
                else:
                    print('You found nothing...')
                    story(character)
            if choice == 1:
                pokemonCenter(character)
            if choice == 2:
                pokemonStore(character)
            if choice == 3:
                checkPokemon(character)
            if choice == 4:
                checkItems(character)
    except ValueError:
        print('Please choose a valid option.')
        story(character)

def wildBattle(character: PokemonTrainer):
    opponentName = random.choice(list(basePokemonList))
    opponent = deepcopy(Pokemon(opponentName, 15))
    print(get_ascii_pokemon(basePokemonList[opponentName].pokedexNumber))
    print(f'You found a wild {opponentName}')
    pokemonAvailable = len(character.pokemons)
    pokemonInBattle = character.pokemons[0]
    while True:
        printBattleUi(pokemonInBattle, opponent)
        try:
            choice = int(input(f'What would {pokemonInBattle.name} like to do? '))
            if choice == 0:
                printBattleMoves(pokemonInBattle)
                while True:
                    try:
                        choice = int(input('Choose an option: '))
                        mainCurrentSpeed = pokemonInBattle.currentStats['speed']
                        mainPriority = pokemonInBattle.moves[choice].priority if hasattr(pokemonInBattle.moves[choice], 'priority') else 0
                        opponentMove = random.choice(opponent.moves)
                        opponentCurrentSpeed = opponent.currentStats['speed']
                        opponentPriority = opponentMove.priority if hasattr(opponentMove, 'priority') else 0
                        mainSpeed = mainCurrentSpeed + 252 * mainPriority 
                        opponentSpeed = opponentCurrentSpeed + 252 * opponentPriority
                        currentPokemon = pokemonInBattle.name
                        if mainSpeed > opponentSpeed:
                            pokemonInBattle.useMove(pokemonInBattle.moves[choice], opponent)
                            pokemonInBattle, pokemonAvailable = check(character, pokemonInBattle, opponent, pokemonAvailable)
                            if currentPokemon == pokemonInBattle.name: opponent.useMove(opponentMove, pokemonInBattle)
                            pokemonInBattle, pokemonAvailable = check(character, pokemonInBattle, opponent, pokemonAvailable)
                        elif opponentSpeed > mainSpeed:
                            opponent.useMove(opponentMove, pokemonInBattle)
                            pokemonInBattle, pokemonAvailable = check(character, pokemonInBattle, opponent, pokemonAvailable)
                            if currentPokemon == pokemonInBattle.name: pokemonInBattle.useMove(pokemonInBattle.moves[choice], opponent)
                            pokemonInBattle, pokemonAvailable = check(character, pokemonInBattle, opponent, pokemonAvailable)
                        else:
                            if random.random() > 0.5:
                                pokemonInBattle.useMove(pokemonInBattle.moves[choice], opponent)
                                pokemonInBattle, pokemonAvailable = check(character, pokemonInBattle, opponent, pokemonAvailable)
                                if currentPokemon == pokemonInBattle.name: opponent.useMove(opponentMove, pokemonInBattle)
                                pokemonInBattle, pokemonAvailable = check(character, pokemonInBattle, opponent, pokemonAvailable)
                            else:
                                opponent.useMove(opponentMove, pokemonInBattle)
                                pokemonInBattle, pokemonAvailable = check(character, pokemonInBattle, opponent, pokemonAvailable)
                                if currentPokemon == pokemonInBattle.name: pokemonInBattle.useMove(pokemonInBattle.moves[choice], opponent)
                                pokemonInBattle, pokemonAvailable = check(character, pokemonInBattle, opponent, pokemonAvailable)
                        break
                    except ValueError:
                        print('Please choose a valid option.')
                        continue
            elif choice == 1:
                pokemonCaptured = False
                if np.sum(list(character.items.values())) == 0:
                    print('You have no items!')
                else:
                    print('Your items are:')
                    for index, item in enumerate(character.items):
                        print(f'  - {index}: {item} x{character.items[item]}')
                    while True:
                        itemChoice = int(input('Choose an item: '))
                        if character.items[list(character.items)[itemChoice]] == 0:
                            print('You have no more of that item!')
                            continue
                        if list(character.items)[itemChoice] == 'Potion':
                            # If all pokemon are full HP, it will not let you use a potion, and it goes to choosing another option in the battle
                            if np.sum([pkmn.currentHp for pkmn in character.pokemons]) == np.sum([pkmn.maxHp for pkmn in character.pokemons]):
                                print('All your pokemon are at full health!')
                                break
                            usePotion(character)
                            break
                        if list(character.items)[itemChoice] == 'Pokeball':
                            # I was going to implement the full catching system, but it would imply changing the whole BasePokemon list
                            # Nevertheless, I don't like the method proposed in the lectures since it's impossible to catch a pokemon with full HP.
                            pokemonCaptured = usePokeball(character, opponent)
                            if pokemonCaptured:
                                # If the pokemon was captured, it will break the loop and go back to the story
                                story(character)
                                break
                            else:
                                break
                if not pokemonCaptured:
                    # If the pokemon was not captured, it will go back to the battle
                    opponentMove = random.choice(opponent.moves)
                    opponent.useMove(opponentMove, pokemonInBattle)
                    pokemonInBattle, pokemonAvailable = check(character, pokemonInBattle, opponent, pokemonAvailable)
            elif choice == 2:
                pokemonInBattle = swapPokemon(character)
                opponentMove = random.choice(opponent.moves)
                opponent.useMove(opponentMove, pokemonInBattle)
                pokemonInBattle, pokemonAvailable = check(character, pokemonInBattle, opponent, pokemonAvailable)
            elif choice == 3:
                if random.random() < 0.6:
                    print('You managed to escape!')
                    story(character)
                else:
                    print('You failed to escape!')
                    opponentMove = random.choice(opponent.moves)
                    opponent.useMove(opponentMove, pokemonInBattle)
                    check(character, pokemonInBattle, opponent, pokemonAvailable)
        except ValueError:
            print('Please choose a valid option.')
            continue

def updateEvs(mainPkmn: Pokemon, defeatedPkmn: Pokemon):
    for stat in list(basePokemonList[defeatedPkmn.name].evYield):
        mainPkmn.effortValues[stat] += basePokemonList[defeatedPkmn.name].evYield[stat]

def check(character, pokemonInBattle, opponent, pokemonAvailable):
    if pokemonInBattle.currentHp == 0:
        pokemonAvailable -= 1
        print(f'{pokemonInBattle.nickname} fainted!')
        if pokemonAvailable == 0:
            print('All your pokemon fainted! Git good m8')
            print('You made your way to the Pokemon Center')
            pokemonCenter(character)
        else:
            pokemonInBattle = swapPokemon(character)
    if opponent.currentHp == 0:
        print(f'You defeated the wild {opponent.name}')
        print(f'{pokemonInBattle.name} gained {basePokemonList[opponent.name].baseExperience * opponent.level / 5} XP')
        pokemonInBattle.gainExperience(basePokemonList[opponent.name].baseExperience * opponent.level / 5)
        updateEvs(pokemonInBattle, opponent)
        story(character)
    return pokemonInBattle, pokemonAvailable

def swapPokemon(character : PokemonTrainer):
    print('Which pokemon do you want to switch to?')
    for index, pokemon in enumerate(character.pokemons):
        print(index, ': ', pokemon.name, f'HP: {pokemon.currentHp}/{pokemon.maxHp}')
    while True:
        try:
            choice = int(input('Choose an option: '))
            if choice not in range(len(character.pokemons)):
                print('Please choose a valid option.')
                continue
            if character.pokemons[choice].currentHp == 0:
                print('That pokemon fainted! Choose another one.')
                continue
            return character.pokemons[choice]
        except ValueError:
            print('Please choose a valid option.')
            continue

def usePotion(character: PokemonTrainer):
    print('Which pokemon would you like to heal?')
    for index, pokemon in enumerate(character.pokemons):
        print(index, ': ', pokemon.name, f'HP: {pokemon.currentHp}/{pokemon.maxHp}')
    while True:
        try:
            choice = int(input('Choose an option: '))
            if choice not in range(len(character.pokemons)):
                print('Please choose a valid option.')
                continue
            if character.pokemons[choice].currentHp == character.pokemons[choice].maxHp:
                print('That pokemon is already at full health! Choose another one.')
                continue
            character.pokemons[choice].updateHp(20)
            character.items['Potion'] = updateValue(character.items['Potion'], -1, 0, 99)
            print(f'{character.pokemons[choice].name} was healed!')
            break
        except ValueError:
            print('Please choose a valid option.')
            continue

def usePokeball(character: PokemonTrainer, opponent: Pokemon):
    catchProbability = (3 * opponent.maxHp - 2 * opponent.currentHp) * basePokemonList[opponent.name].captureRate / (3 * opponent.maxHp * 255)
    print(f'Throwing a pokeball at the wild {opponent.name}...')
    print(f'Catch probability: {catchProbability}')
    sleep(2)
    if random.random() < catchProbability:
        print(f'You caught the wild {opponent.name}!')
        pokemonCaptured = True
        sleep(4)
        # Checks if trainer already has 6 pokemons. If so, it asks to swap one of them
        if len(character.pokemons) == 6:
            print('Your party is full! Choose a pokemon to swap with the new one!')
            for index, pokemon in enumerate(character.pokemons):
                print(index, ': ', pokemon.name, f'HP: {pokemon.currentHp}/{pokemon.maxHp}')
            while True:
                try:
                    choice = int(input('Choose an option: '))
                    if character.pokemons[choice].currentHp == 0:
                        print('That pokemon fainted! Choose another one.')
                        continue
                    else:
                        character.pokemons[choice] = deepcopy(opponent)
                        story(character)
                except ValueError:
                    print('Please choose a valid option.')
                    continue
        else:
            character.pokemons.append(opponent)
        character.items['Pokeball'] = updateValue(character.items['Pokeball'], -1, 0, 99)
        return True

    else:
        character.items['Pokeball'] = updateValue(character.items['Pokeball'], -1, 0, 99)
        print('The wild pokemon broke free!')
        sleep(2)
        return False

def updateValue(value, update, valueMin, valueMax):
    '''Updates a value with a certain update. It will not go below the minimum or above the maximum.
    
    Used for stats, HP, etc.
    '''
    if (value + update) < valueMin:
        value = valueMin
    elif (value + update) > valueMax:
        value = valueMax
    else:
        value += update
    return value

def pokemonCenter(character: PokemonTrainer):
    printPokeCenter()
    sleep(3)
    for pkmn in character.pokemons:
        pkmn.currentHp = pkmn.maxHp
        for move in pkmn.moves:
            move.pp = moveList[move.name].pp
    print('Your pokemon were healed. See you soon!')
    story(character)

def pokemonStore(character: PokemonTrainer):
    printStore()
    character.items['Potion'] = 10
    character.items['Pokeball'] = 10
    print('You bought 10 potions and 10 pokeballs!')
    print('Yes! With literally no money!')
    story(character)

def checkPokemon(character: PokemonTrainer):
    print('Your pokemon are:')
    for i in range(len(character.pokemons)):
        if character.pokemons[i].name != character.pokemons[i].nickname:
            print(i, ':', character.pokemons[i].nickname, '(', character.pokemons[i].name,')')
        else:
            print(i, ':', character.pokemons[i].name)
    try:
        print('Woud you like to check (0) or swap (1) the order of your pokemon?')
        choice = int(input('Choose an option (0/1): '))
        if choice not in range(2):
            print('Please choose a valid option.')
            checkPokemon(character)
        if choice == 0:
            pokeChoice = int(input('Choose a pokemon to check: '))
            printPokemonSummary(character.pokemons[pokeChoice])
            input('Whenever you are done, press Enter')
        if choice == 1:
            pokemonIndex1 = int(input('Enter the index of the first pokemon: '))
            pokemonIndex2 = int(input('Enter the index of the second pokemon: '))
            if pokemonIndex1 not in range(len(character.pokemons)) or pokemonIndex2 not in range(len(character.pokemons)):
                print('Invalid pokemon index.')
            else:
                character.pokemons[pokemonIndex1], character.pokemons[pokemonIndex2] = character.pokemons[pokemonIndex2], character.pokemons[pokemonIndex1]
                print('Pokemon order swapped successfully!')
    except ValueError:
        print('Please choose a valid option.')
    
    story(character)

def checkItems(character: PokemonTrainer):
    if np.sum(list(character.items.values())) == 0:
        print('You have no items!')
    else:
        print('Your items are:')
        for item in character.items:
            print(f'  - {item} x{character.items[item]}')
    sleep(5)
    story(character)

if __name__ == "__main__":
    createCharacter('fast')