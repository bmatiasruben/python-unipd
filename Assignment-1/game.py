from Libraries.PokemonSprites import *
from Libraries.BasePokemon import basePokemonList
from Libraries.PokemonTrainer import PokemonTrainer
from Libraries.Pokemon import Pokemon
from Libraries.Moves import *
import random
from time import sleep
from Libraries.prints import *
from copy import deepcopy

def Main():
    printFirstStart()
    name = input('First, tell me your name: ')
    mainCharacter = PokemonTrainer(name, [], [])
    sleep(1)
    print('Perfect... Now I\'ll let you choose any pokemon from first generation')
    sleep(1)
    choiceSure = False
    while not choiceSure:
        try:
            choice = int(input('Choose any pokemon from the first generation by ID (0-150): '))
            try:
                chosenPokemon = deepcopy(basePokemonList[list(basePokemonList)[choice]])
            except IndexError:
                print(f'No cheating! Remember, this is only a simulation, you have no free will.')
            print(get_ascii_pokemon(chosenPokemon.pokedexNumber))
            while True:
                sure = input(f'Do you want to choose the {chosenPokemon.type[0].capitalize()} type pokemon {chosenPokemon.name.capitalize()}? (y/n) ')
                if sure == 'y':
                    while True:
                        try:
                            level = int(input('At which level? '))
                            if level not in range(1, 100):
                                print('Try again, this time put a number from 1 to 100.')
                                continue
                            break
                        except ValueError:
                            print('Try again, this time put a number from 1 to 100.')
                    mainCharacter.pokemons.append(Pokemon(chosenPokemon.name, level))
                    print(f'You obtained the pokemon {chosenPokemon.name.capitalize()}!')
                    while True:
                        nicknameYN = input(f'Would you like to give {chosenPokemon.name.capitalize()} a nickname? (y/n) ')
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
            print('Please choose a valid option. Hint: you should put an integer from 0 to 150')
    sleep(1)
    print('Great. Now fight some random pokemon.')
    sleep(1)
    print('They will be the same level as your pokemon.')
    sleep(1)
    print('Oh! And also, they could be legendaries. Good luck, you might need it...')
    wildBattle(mainCharacter)

def wildBattle(character: PokemonTrainer):
    opponentName = random.choice(list(basePokemonList))
    opponent = deepcopy(Pokemon(opponentName, character.pokemons[0].level))
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
                            checkAlive(character, pokemonInBattle, opponent, pokemonAvailable)
                            opponent.useMove(opponentMove, pokemonInBattle)
                            checkAlive(character, pokemonInBattle, opponent, pokemonAvailable)
                        elif opponentSpeed > mainSpeed:
                            opponent.useMove(opponentMove, pokemonInBattle)
                            checkAlive(character, pokemonInBattle, opponent, pokemonAvailable)
                            pokemonInBattle.useMove(pokemonInBattle.moves[choice], opponent)
                            checkAlive(character, pokemonInBattle, opponent, pokemonAvailable)
                        else:
                            if random.random() > 0.5:
                                pokemonInBattle.useMove(pokemonInBattle.moves[choice], opponent)
                                checkAlive(character, pokemonInBattle, opponent, pokemonAvailable)
                                opponent.useMove(opponentMove, pokemonInBattle)
                                checkAlive(character, pokemonInBattle, opponent, pokemonAvailable)
                            else:
                                opponent.useMove(opponentMove, pokemonInBattle)
                                checkAlive(character, pokemonInBattle, opponent, pokemonAvailable)
                                pokemonInBattle.useMove(pokemonInBattle.moves[choice], opponent)
                                checkAlive(character, pokemonInBattle, opponent, pokemonAvailable)
                        break
                    except ValueError:
                        print('Please choose a valid option.')
                        continue
            elif choice == 1:
                opponentMove = random.choice(opponent.moves)
                opponent.useMove(opponentMove, pokemonInBattle)
                checkAlive(character, pokemonInBattle, opponent, pokemonAvailable)
            elif choice == 2:
                pokemonInBattle = swapPokemon(character)
                opponentMove = random.choice(opponent.moves)
                opponent.useMove(opponentMove, pokemonInBattle)
                checkAlive(character, pokemonInBattle, opponent, pokemonAvailable)
            elif choice == 3:
                if random.random() < 0.6:
                    print('You managed to escape... for now.')
                    wildBattle(character)
                else:
                    print('You failed to escape!')
                    opponentMove = random.choice(opponent.moves)
                    opponent.useMove(opponentMove, pokemonInBattle)
                    checkAlive(character, pokemonInBattle, opponent, pokemonAvailable)
        except ValueError:
            print('Please choose a valid option.')
            continue

def updateEvs(mainPkmn: Pokemon, defeatedPkmn: Pokemon):
    for stat in list(basePokemonList[defeatedPkmn.name].evYield):
        mainPkmn.effortValues[stat] += basePokemonList[defeatedPkmn.name].evYield[stat]

def checkAlive(character, pokemonInBattle, opponent, pokemonAvailable):
    if pokemonInBattle.currentHp == 0:
        pokemonAvailable -= 1
        print(f'{pokemonInBattle.nickname} fainted!')
        if pokemonAvailable == 0:
            print('All your pokemon fainted! Git good m8.')
            exit()
        else:
            pokemonInBattle = swapPokemon(character)
    if opponent.currentHp == 0:
        print(f'You defeated the wild {opponent.name}')
        print(f'{pokemonInBattle.name} gained {basePokemonList[opponent.name].baseExperience * opponent.level / 5} XP')
        pokemonInBattle.gainExperience(basePokemonList[opponent.name].baseExperience * opponent.level / 5)
        updateEvs(pokemonInBattle, opponent)
        wildBattle(character)
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

if __name__ == "__main__":
    Main()