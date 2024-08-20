
#%% Libraries and createCharacter function
from Libraries.PokemonSprites import *
from Libraries.BasePokemon import basePokemon
from Libraries.PokemonTrainer import PokemonTrainer
from Libraries.Pokemon import Pokemon
from Libraries.Moves import *
import random
from time import sleep
from Libraries.prints import *
from copy import deepcopy
import numpy as np
import pickle

def createCharacter(string, starterPokemon = 'bulbasaur', level = 1, amountOfBattles = 1000):
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
        mainCharacter.pokemons.append(deepcopy(Pokemon(starterPokemon, level, mode=string)))
        print(mainCharacter.pokemons[0].moves)
        for move in mainCharacter.pokemons[0].moves:
            print(move.name, move.power)
        mainCharacter.pokemons[0].owner = 'mainCharacter'
        facedPokemon, battleResults, turnsPerBattle, percentageHpLeft, usedMovesGame, currentHpPercentGame, damageDoneGame = autoExplore(mainCharacter, amountOfBattles)    
        return facedPokemon, battleResults, turnsPerBattle, percentageHpLeft, usedMovesGame, currentHpPercentGame, damageDoneGame
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
                            triedToGet = list(basePokemon)[choice + 1]
                        print(f'No cheating! I cannot give you a {triedToGet} as your first pokemon!')
                    except IndexError:
                        print(f'No cheating! This game only has first generation pokemon!')
                    sleep(2)
                else:
                    print(get_ascii_pokemon(basePokemon[options[choice]].pokedexNumber))
                    while True:
                        sure = input(f'Do you want to choose the {basePokemon[options[choice]].types[0].capitalize()} type pokemon {options[choice].capitalize()}? (y/n) ')
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
    usedMovesGame = []
    currentHpPercentGame = []
    damageDoneGame = []
    for i in range(amountOfBattles):
        usedMovesFight = []
        currentHpPercentFight = []
        damageDoneFight = []
        pokemonCenter(character, mode = 'randomExplore')
        opponentName = random.choice(list(basePokemon))
        randomLevel = random.randint(1, 20)
        opponent = deepcopy(Pokemon(opponentName, randomLevel, mode= 'randomExplore'))
        print(f'You found a wild {opponentName}!')
        pokemonInBattle = character.pokemons[0]
        turns = 0
        while True:
            turns += 1
            if amountOfBattles < 100:
                printReducedBattleUi(pokemonInBattle, opponent)
            pokemonInBattle, usedMoves, currentHpPercent, damageDone = fight(character, pokemonInBattle, opponent, mode='randomExplore')
            usedMovesFight.append(usedMoves)
            currentHpPercentFight.append(currentHpPercent)
            damageDoneFight.append(damageDone)
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
        usedMovesGame.append(usedMovesFight)
        currentHpPercentGame.append(currentHpPercentFight)
        damageDoneGame.append(damageDoneFight)
        print(usedMovesFight)
        print(currentHpPercentFight)
        print(damageDoneFight)
    return facedPokemon, battleResults, turnsPerBattle, percentageHpLeft, usedMovesGame, currentHpPercentGame, damageDoneGame

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
    opponentName = random.choice(list(basePokemon))
    pokemonInBattle = character.pokemons[0]
    opponent = deepcopy(Pokemon(opponentName, pokemonInBattle.level))
    print(get_ascii_pokemon(basePokemon[opponentName].pokedexNumber))
    print(f'You found a wild {opponentName}')
    while True:
        printBattleUi(pokemonInBattle, opponent)
        try:
            choice = int(input(f'What would {pokemonInBattle.name} like to do? '))
            if choice == 0:
                printBattleMoves(pokemonInBattle)
                pokemonInBattle, _, _, _ = fight(character, pokemonInBattle, opponent)
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
                            # If you have no more potions, it will not let you use a potion, and it goes to choosing another option in the battle
                            if np.sum([pkmn.currentHp for pkmn in character.pokemons]) == np.sum([pkmn.maxHp for pkmn in character.pokemons]):
                                print('All your pokemon are at full health!')
                                break
                            if character.items['Potion'] == 0:
                                print('You have no more potions!')
                                break
                            usePotion(character)
                            break
                        if list(character.items)[itemChoice] == 'Pokeball':
                            # I was going to implement the full catching system, but it would imply changing the whole BasePokemon list
                            # Nevertheless, I don't like the method proposed in the lectures since it's impossible to catch a pokemon with full HP.
                            # If you have no more pokeballs, it will not let you use a pokeball, and it goes to choosing another option in the battle
                            if character.items['Pokeball'] == 0:
                                print('You have no more pokeballs!')
                                break
                            else:
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
                    pokemonInBattle = check(character, pokemonInBattle, opponent)
            elif choice == 2:
                pokemonInBattle = swapPokemon(character)
                opponentMove = random.choice(opponent.moves)
                opponent.useMove(opponentMove, pokemonInBattle)
                pokemonInBattle = check(character, pokemonInBattle, opponent)
            elif choice == 3:
                if random.random() < 0.6:
                    print('You managed to escape!')
                    story(character)
                else:
                    print('You failed to escape!')
                    opponentMove = random.choice(opponent.moves)
                    opponent.useMove(opponentMove, pokemonInBattle)
                    check(character, pokemonInBattle, opponent)
        except ValueError:
            print('Please choose a valid option.')
            continue

def fight(character: PokemonTrainer, mainPkmn: Pokemon, opponent: Pokemon, mode = 'default'):
    usedMoves = ''
    currentHpPercent = 0
    damageDone = 0
    damageDealt = 0
    print('Starting Fight!')
    while True:
        try:
            if mode == 'randomExplore':
                choice = random.choice(range(len(mainPkmn.moves)))
                mainPkmn.moves[choice].pp = 999 # Ignores PP on the random battle mode
            else:
                choice = int(input('Choose an option: '))
            mainCurrentSpeed = mainPkmn.currentStats['speed']
            mainPriority = mainPkmn.moves[choice].priority if hasattr(mainPkmn.moves[choice], 'priority') else 0
            opponentMove = random.choice(opponent.moves)
            opponentCurrentSpeed = opponent.currentStats['speed']
            opponentPriority = opponentMove.priority if hasattr(opponentMove, 'priority') else 0
            mainSpeed = mainCurrentSpeed + 252 * mainPriority 
            opponentSpeed = opponentCurrentSpeed + 252 * opponentPriority
            currentPokemon = mainPkmn.name
            usedMoves = mainPkmn.moves[choice].name
            currentMainHp = mainPkmn.currentHp
            if mainSpeed > opponentSpeed:
                damageDealt = mainPkmn.useMove(mainPkmn.moves[choice], opponent)
                mainPkmn = check(character, mainPkmn, opponent, mode)
                if (mainPkmn != None and currentPokemon == mainPkmn.name and opponent.currentHp > 0): 
                    opponent.useMove(opponentMove, mainPkmn)
                    mainPkmn = check(character, mainPkmn, opponent, mode)
                    currentMainHp = mainPkmn.currentHp/mainPkmn.maxHp
                else:
                    currentMainHp = 0
            elif opponentSpeed > mainSpeed:
                opponent.useMove(opponentMove, mainPkmn)
                mainPkmn = check(character, mainPkmn, opponent, mode)
                if (mainPkmn != None and currentPokemon == mainPkmn.name and mainPkmn.currentHp > 0):
                    damageDealt = mainPkmn.useMove(mainPkmn.moves[choice], opponent)
                    mainPkmn = check(character, mainPkmn, opponent, mode)
                    currentMainHp = mainPkmn.currentHp/mainPkmn.maxHp
                else:
                    currentMainHp = 0
            else:
                if random.random() > 0.5:
                    damageDealt = mainPkmn.useMove(mainPkmn.moves[choice], opponent)
                    mainPkmn = check(character, mainPkmn, opponent, mode)
                    if (mainPkmn != None and currentPokemon == mainPkmn.name and opponent.currentHp > 0): 
                        opponent.useMove(opponentMove, mainPkmn)
                        mainPkmn = check(character, mainPkmn, opponent, mode)
                        currentMainHp = mainPkmn.currentHp/mainPkmn.maxHp
                    else:
                        currentMainHp = 0
                else:
                    opponent.useMove(opponentMove, mainPkmn)
                    mainPkmn = check(character, mainPkmn, opponent, mode)
                    if (mainPkmn != None and currentPokemon == mainPkmn.name and mainPkmn.currentHp > 0): 
                        damageDealt = mainPkmn.useMove(mainPkmn.moves[choice], opponent)
                        mainPkmn = check(character, mainPkmn, opponent, mode)
                        currentMainHp = mainPkmn.currentHp/mainPkmn.maxHp
                    else:
                        currentMainHp = 0
            currentHpPercent = currentMainHp
            damageDone = damageDealt
            break
        except ValueError:
            # Print the source of the error
            print('Please choose a valid option.')
            continue
    return mainPkmn, usedMoves, currentHpPercent, damageDone
        
def updateEvs(mainPkmn: Pokemon, defeatedPkmn: Pokemon):

    for stat in list(defeatedPkmn.basePokemon.evYield):
        mainPkmn.effortValues[stat] += basePokemon[defeatedPkmn.name].evYield[stat]

def check(character, pokemonInBattle, opponent, mode = 'default'):
    if pokemonInBattle.currentHp == 0:
        print(f'{pokemonInBattle.nickname} fainted!')
        if mode != 'randomExplore':
            if character.availablePokemon() == 0:
                print('All your pokemon fainted! Git good m8')
                print('You made your way to the Pokemon Center')
                pokemonCenter(character, mode)
            else:
                print('Choose another pokemon!')
                return swapPokemon(character)
        else:
            return pokemonInBattle
    if opponent.currentHp == 0:
        if mode != 'randomExplore':
            print(f'You defeated the wild {opponent.name}')
            print(f'{pokemonInBattle.name} gained {basePokemon[opponent.name].baseExp * opponent.level / 5} XP')
            pokemonInBattle.gainExperience(basePokemon[opponent.name].baseExp * opponent.level / 5)
            updateEvs(pokemonInBattle, opponent)
            story(character)
        else:
            return pokemonInBattle
    return pokemonInBattle

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
    catchProbability = (3 * opponent.maxHp - 2 * opponent.currentHp) * basePokemon[opponent.name].captureRate / (3 * opponent.maxHp * 255)
    print(f'Throwing a pokeball at the wild {opponent.name}...')
    print(f'Catch probability: {catchProbability}')
    character.items['Pokeball'] = updateValue(character.items['Pokeball'], -1, 0, 99)
    sleep(2)
    if random.random() < catchProbability:
        for i in range(3):
            print('.'*(i+1), end = '\r')
            sleep(1)
        print(f'You caught the wild {opponent.name}!')
        pokemonCaptured = True
        sleep(4)
        nicknameChoice = input(f'Would you like to give {opponent.name} a nickname? (y/n) ')
        if nicknameChoice == 'y':
            opponent.nickname = input('Please choose a nickname: ')
        # Checks if trainer already has 6 pokemons. If so, it asks to swap one of them
        if len(character.pokemons) == 6:
            print('Your party is full! Choose a pokemon to swap with the new one!')
            for index, pokemon in enumerate(character.pokemons):
                print(index, ': ', pokemon.name, f'HP: {pokemon.currentHp}/{pokemon.maxHp}')
            while True:
                try:
                    choice = int(input('Choose an option: '))
                    character.pokemons[choice] = deepcopy(opponent)
                    story(character)
                except ValueError or IndexError:
                    print('Please choose a valid option.')
                    continue
        else:
            character.pokemons.append(deepcopy(opponent))
            story(character)
        return True

    else:
        randomShakes = random.choice([0, 1, 2])
        for i in range(randomShakes):
            print('.'*(i+1), end = '\r')
            sleep(1)
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
            move.pp = moveList[move.name]['pp']
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
        amountOfGames = 1000
        amountOfBattles = 200
        starterPokemons = ['bulbasaur', 'charmander', 'squirtle']
        import sys, os
        sys.stdout = open(os.devnull, 'w')
        # Delete previous results
        for file in os.listdir('Results'):
            os.remove(f'Results\\{file}')
        gamesPerPokemon = {pokemon : 0 for pokemon in starterPokemons}
        fullResults = pd.
        for i in range(amountOfGames):
            starterPokemon = random.choice(starterPokemons)
            gamesPerPokemon[starterPokemon] += 1
            level = random.randint(1, 20)

            facedPokemon, battleResults, turnsPerBattle, percentageHpLeft, usedMovesGame, currentHpPercentGame, damageDoneGame = createCharacter('randomExplore', starterPokemon=starterPokemon, level=level, amountOfBattles=amountOfBattles)
            # Save data to pickle files
            with open(f'Results\\facedPokemon_{starterPokemon}_{i}_lvl{level}.pkl', 'wb') as f:
                pickle.dump(facedPokemon, f)
            with open(f'Results\\battleResults_{starterPokemon}_{i}_lvl{level}.pkl', 'wb') as f:
                pickle.dump(battleResults, f)
            with open(f'Results\\turnsPerBattle_{starterPokemon}_{i}_lvl{level}.pkl', 'wb') as f:
                pickle.dump(turnsPerBattle, f)
            with open(f'Results\\percentageHpLeft_{starterPokemon}_{i}_lvl{level}.pkl', 'wb') as f:
                pickle.dump(percentageHpLeft, f)
            with open(f'Results\\usedMovesGame_{starterPokemon}_{i}_lvl{level}.pkl', 'wb') as f:
                pickle.dump(usedMovesGame, f)
            with open(f'Results\\currentHpPercentGame_{starterPokemon}_{i}_lvl{level}.pkl', 'wb') as f:
                pickle.dump(currentHpPercentGame, f)
            with open(f'Results\\damageDoneGame_{starterPokemon}_{i}_lvl{level}.pkl', 'wb') as f:
                pickle.dump(damageDoneGame, f)
        if printResults:
            print('You have finished exploring! Let\'s see how you did!')
            print('You faced the following pokemons:', facedPokemon)
            print('The results of the battles were:', battleResults)
            print('The amount of turns per battle were:', turnsPerBattle)
            print('The percentage of HP left after the battle was:', percentageHpLeft)
            print('Now you are back to the Pokemon Center!')

# %%
