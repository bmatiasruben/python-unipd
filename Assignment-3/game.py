#%% 
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
import pickle

def createCharacter(string, starterPokemon = 'bulbasaur'):
    if string == 'fast':
        mainCharacter = PokemonTrainer('Matias', [], [])
        mainCharacter.pokemons.append(deepcopy(Pokemon(starterPokemon, 15)))
        mainCharacter.pokemons.append(deepcopy(Pokemon('pidgey', 1)))
        mainCharacter.pokemons[0].owner = 'mainCharacter'
        mainCharacter.pokemons[1].owner = 'mainCharacter'
        mainCharacter.items = {'Pokeball': 10, 'Potion': 10}
        story(mainCharacter)
    elif string == 'randomExplore':
        mainCharacter = PokemonTrainer('Matias', [], [])
        mainCharacter.pokemons.append(deepcopy(Pokemon(starterPokemon, 1, mode=string)))
        print(mainCharacter.pokemons[0].moves)
        for move in mainCharacter.pokemons[0].moves:
            print(move.name, move.power)
        mainCharacter.pokemons[0].owner = 'mainCharacter'
        facedPokemon, battleResults, turnsPerBattle, percentageHpLeft = autoExplore(mainCharacter, amountOfBattles)    
        return facedPokemon, battleResults, turnsPerBattle, percentageHpLeft
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

#%% Automatic exploration mode, related to assignment 3
def autoExplore(character: PokemonTrainer, amountOfBattles):
    facedPokemon = []
    battleResults = []
    turnsPerBattle = []
    percentageHpLeft = []
    for i in range(amountOfBattles):
        pokemonCenter(character, mode = 'randomExplore')
        opponentName = random.choice(list(basePokemonList))
        opponent = deepcopy(Pokemon(opponentName, 1, mode= 'randomExplore'))
        print(f'You found a wild {opponentName}!')
        pokemonInBattle = character.pokemons[0]
        turns = 0
        while True:
            turns += 1
            if amountOfBattles < 100:
                printReducedBattleUi(pokemonInBattle, opponent)
            fight(character, pokemonInBattle, opponent, mode='randomExplore')
            if pokemonInBattle.currentHp == 0:
                print(f'{pokemonInBattle.nickname} fainted! You lost the battle!')
                facedPokemon.append(opponentName)
                battleResults.append('Lost')
                turnsPerBattle.append(turns)
                percentageHpLeft.append(100 * opponent.currentHp / opponent.maxHp)
                break
            if opponent.currentHp == 0:
                print(f'You defeated the wild {opponent.name}!')
                facedPokemon.append(opponentName)
                battleResults.append('Won')
                turnsPerBattle.append(turns)
                percentageHpLeft.append(100 * pokemonInBattle.currentHp / pokemonInBattle.maxHp)
                break
    return facedPokemon, battleResults, turnsPerBattle, percentageHpLeft

#%% Story stuff, related to assignments 1 and 2

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
    pokemonInBattle = character.pokemons[0]
    opponent = deepcopy(Pokemon(opponentName, pokemonInBattle.level))
    print(get_ascii_pokemon(basePokemonList[opponentName].pokedexNumber))
    print(f'You found a wild {opponentName}')
    pokemonAvailable = len(character.pokemons)
    while True:
        printBattleUi(pokemonInBattle, opponent)
        try:
            choice = int(input(f'What would {pokemonInBattle.name} like to do? '))
            if choice == 0:
                printBattleMoves(pokemonInBattle)
                fight(character, pokemonInBattle, opponent)
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

def fight(character: PokemonTrainer, mainPkmn: Pokemon, opponent: Pokemon, mode = 'default'):
    pokemonAvailable = len(character.pokemons)
    while True:
        try:
            if mode == 'default':
                choice = int(input('Choose an option: '))
            elif mode == 'randomExplore':
                choice = random.choice(range(len(mainPkmn.moves)))
                mainPkmn.moves[choice].pp = 999 # Ignores PP on the random battle mode
            mainCurrentSpeed = mainPkmn.currentStats['speed']
            mainPriority = mainPkmn.moves[choice].priority if hasattr(mainPkmn.moves[choice], 'priority') else 0
            opponentMove = random.choice(opponent.moves)
            opponentCurrentSpeed = opponent.currentStats['speed']
            opponentPriority = opponentMove.priority if hasattr(opponentMove, 'priority') else 0
            mainSpeed = mainCurrentSpeed + 252 * mainPriority 
            opponentSpeed = opponentCurrentSpeed + 252 * opponentPriority
            currentPokemon = mainPkmn.name
            if mainSpeed > opponentSpeed:
                mainPkmn.useMove(mainPkmn.moves[choice], opponent)
                mainPkmn, pokemonAvailable = check(character, mainPkmn, opponent, pokemonAvailable, mode)
                if (mainPkmn != None and currentPokemon == mainPkmn.name): 
                    opponent.useMove(opponentMove, mainPkmn)
                    mainPkmn, pokemonAvailable = check(character, mainPkmn, opponent, pokemonAvailable, mode)
            elif opponentSpeed > mainSpeed:
                opponent.useMove(opponentMove, mainPkmn)
                mainPkmn, pokemonAvailable = check(character, mainPkmn, opponent, pokemonAvailable, mode)
                if (mainPkmn != None and currentPokemon == mainPkmn.name): 
                    mainPkmn.useMove(mainPkmn.moves[choice], opponent)
                    mainPkmn, pokemonAvailable = check(character, mainPkmn, opponent, pokemonAvailable, mode)
            else:
                if random.random() > 0.5:
                    mainPkmn.useMove(mainPkmn.moves[choice], opponent)
                    mainPkmn, pokemonAvailable = check(character, mainPkmn, opponent, pokemonAvailable, mode)
                    if (mainPkmn != None and currentPokemon == mainPkmn.name): 
                        opponent.useMove(opponentMove, mainPkmn)
                        mainPkmn, pokemonAvailable = check(character, mainPkmn, opponent, pokemonAvailable, mode)
                else:
                    opponent.useMove(opponentMove, mainPkmn)
                    mainPkmn, pokemonAvailable = check(character, mainPkmn, opponent, pokemonAvailable, mode)
                    if (mainPkmn != None and currentPokemon == mainPkmn.name): 
                        mainPkmn.useMove(mainPkmn.moves[choice], opponent)
                        mainPkmn, pokemonAvailable = check(character, mainPkmn, opponent, pokemonAvailable, mode)
            break
        except ValueError:
            print('Please choose a valid option.')
            continue
        
def updateEvs(mainPkmn: Pokemon, defeatedPkmn: Pokemon):
    for stat in list(basePokemonList[defeatedPkmn.name].evYield):
        mainPkmn.effortValues[stat] += basePokemonList[defeatedPkmn.name].evYield[stat]

def check(character, pokemonInBattle, opponent, pokemonAvailable, mode = 'default'):
    if pokemonInBattle.currentHp == 0:
        pokemonAvailable -= 1
        print(f'{pokemonInBattle.nickname} fainted!')
        if mode != 'randomExplore':
            if pokemonAvailable == 0:
                print('All your pokemon fainted! Git good m8')
                print('You made your way to the Pokemon Center')
                pokemonCenter(character, mode)
        else:
            return None, pokemonAvailable
    if opponent.currentHp == 0:
        if mode != 'randomExplore':
            print(f'You defeated the wild {opponent.name}')
            print(f'{pokemonInBattle.name} gained {basePokemonList[opponent.name].baseExperience * opponent.level / 5} XP')
            pokemonInBattle.gainExperience(basePokemonList[opponent.name].baseExperience * opponent.level / 5)
            updateEvs(pokemonInBattle, opponent)
            story(character)
        else:
            return None, pokemonAvailable
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
#%% General game functions available when in Story mode (+ updateValue function)
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

def pokemonCenter(character: PokemonTrainer, mode = 'default'):
    if mode != 'randomExplore':
        printPokeCenter()
        sleep(3)
    for pkmn in character.pokemons:
        pkmn.currentHp = pkmn.maxHp
        for move in pkmn.moves:
            move.pp = moveList[move.name].pp
    if mode != 'randomExplore': 
        print('Your pokemon were healed. See you soon!')
        story(character)
    else:
        autoExplore

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

#%% Main function to run the game
if __name__ == "__main__":

    mode = 'randomExplore'
    if mode == 'default':
        createCharacter('default')
    elif mode == 'fast':
        createCharacter('fast')
    elif mode == 'randomExplore':
        printResults = False
        amountOfGames = 500
        amountOfBattles = 200
        starterPokemons = ['bulbasaur', 'charmander', 'squirtle']
        import sys, os
        sys.stdout = open(os.devnull, 'w')
        # If Results2 folder does not exist, create it
        if not os.path.exists('Results'):
            os.makedirs('Results')
        # Delete all files in the Results folder
        for file in os.listdir('Results'):
            os.remove(f'Results\\{file}')
        for starterPokemon in starterPokemons:
            for i in range(amountOfGames):
                facedPokemon, battleResults, turnsPerBattle, percentageHpLeft = createCharacter('randomExplore', starterPokemon=starterPokemon)
                # Save data to pickle files
                with open(f'Results\\facedPokemon_{starterPokemon}_{i}.pkl', 'wb') as f:
                    pickle.dump(facedPokemon, f)
                with open(f'Results\\battleResults_{starterPokemon}_{i}.pkl', 'wb') as f:
                    pickle.dump(battleResults, f)
                with open(f'Results\\turnsPerBattle_{starterPokemon}_{i}.pkl', 'wb') as f:
                    pickle.dump(turnsPerBattle, f)
                with open(f'Results\\percentageHpLeft_{starterPokemon}_{i}.pkl', 'wb') as f:
                    pickle.dump(percentageHpLeft, f)
        if printResults:
            print('You have finished exploring! Let\'s see how you did!')
            print('You faced the following pokemons:', facedPokemon)
            print('The results of the battles were:', battleResults)
            print('The amount of turns per battle were:', turnsPerBattle)
            print('The percentage of HP left after the battle was:', percentageHpLeft)
            print('Now you are back to the Pokemon Center!')
        



    

# %%
