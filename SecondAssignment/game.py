from Libraries.PokemonSprites import *
from Libraries.BasePokemon import basePokemonList
from Libraries.PokemonTrainer import PokemonTrainer
from Libraries.Pokemon import Pokemon
from Libraries.Moves import *
import random
from time import sleep
from Libraries.prints import *
from copy import deepcopy

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
                            break
                        else:
                            print('Please choose a valid option.')
                            continue
            except ValueError:
                print('Please choose a valid option. Hint: you should put an integer from 0 to 2')
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
                        if mainSpeed > opponentSpeed:
                            pokemonInBattle.useMove(pokemonInBattle.moves[choice], opponent)
                            check(character, pokemonInBattle, opponent, pokemonAvailable)
                            opponent.useMove(opponentMove, pokemonInBattle)
                            check(character, pokemonInBattle, opponent, pokemonAvailable)
                        elif opponentSpeed > mainSpeed:
                            opponent.useMove(opponentMove, pokemonInBattle)
                            check(character, pokemonInBattle, opponent, pokemonAvailable)
                            pokemonInBattle.useMove(pokemonInBattle.moves[choice], opponent)
                            check(character, pokemonInBattle, opponent, pokemonAvailable)
                        else:
                            if random.random() > 0.5:
                                pokemonInBattle.useMove(pokemonInBattle.moves[choice], opponent)
                                check(character, pokemonInBattle, opponent, pokemonAvailable)
                                opponent.useMove(opponentMove, pokemonInBattle)
                                check(character, pokemonInBattle, opponent, pokemonAvailable)
                            else:
                                opponent.useMove(opponentMove, pokemonInBattle)
                                check(character, pokemonInBattle, opponent, pokemonAvailable)
                                pokemonInBattle.useMove(pokemonInBattle.moves[choice], opponent)
                                check(character, pokemonInBattle, opponent, pokemonAvailable)
                        break
                    except ValueError:
                        print('Please choose a valid option.')
                        continue
            elif choice == 1:
                opponentMove = random.choice(opponent.moves)
                opponent.useMove(opponentMove, pokemonInBattle)
                check(character, pokemonInBattle, opponent, pokemonAvailable)
            elif choice == 2:
                pokemonInBattle = swapPokemon(character)
                opponentMove = random.choice(opponent.moves)
                opponent.useMove(opponentMove, pokemonInBattle)
                check(character, pokemonInBattle, opponent, pokemonAvailable)
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
    return pokemonInBattle

def swapPokemon(character : PokemonTrainer):
    print('Which pokemon do you want to switch to?')
    for index, pokemon in enumerate(character.pokemons):
        print(index, ': ', pokemon.name, f'HP: {pokemon.currentHp}/{pokemon.maxHp}')
    while True:
        try:
            choice = int(input('Choose an option: '))
            if character.pokemons[choice].currentHp == 0:
                print('That pokemon fainted! Choose another one.')
                continue
            return character.pokemons[choice]
        except ValueError:
            print('Please choose a valid option.')
            continue

def pokemonCenter(character: PokemonTrainer):
    print('Welcome to the Pokemon Center')
    print('Wait while we heal your pokemon')
    sleep(3)
    for pkmn in character.pokemons:
        pkmn.currentHp = pkmn.maxHp
        for move in pkmn.moves:
            move.pp = moveList[move.name].pp
    print('Your pokemon were healed. See you soon!')
    story(character)

def pokemonStore(character: PokemonTrainer):
    print('Welcome to the Pokemon Store')
    print('Although you seem to have no money at all, have these free items!')
    print('Please don\'t come back, you\'ll ruin our business!')
    story(character)

def checkPokemon(character: PokemonTrainer):
    print('Your pokemon are:')
    for i in range(len(character.pokemons)):
        if character.pokemons[i].name != character.pokemons[i].nickname:
            print(i, ':', character.pokemons[i].nickname, '(', character.pokemons[i].name,')')
        else:
            print(i, ':', character.pokemons[i].name)
    try:
        choice = int(input('Which pokemon would you like to check? '))
        printPokemonSummary(character.pokemons[choice])
        input('Whenever you are done, press Enter')
    except ValueError:
        print('Please choose a valid option.')
    story(character)

if __name__ == "__main__":
    createCharacter('fast')