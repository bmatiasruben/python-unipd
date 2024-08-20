#%%
import pickle
import matplotlib.pyplot as plt
import glob
import numpy as np
starterPokemons = ['bulbasaur', 'charmander', 'squirtle']
# Load the data 
totalBattleResults = {}
totalFacedPokemon = {}
totalPercentageHpLeft = {}
totalTurnsPerBattle = {}
totalCurrentHpPercentGame = {}
totalDamageDoneGame = {}
totalUsedMovesGame = {}

for pokemon in starterPokemons:
    battleResultsFilenames = glob.glob(f'Results\\battleResults_{pokemon}*.pkl')
    facedPokemonFilenames = glob.glob(f'Results\\facedPokemon_{pokemon}*.pkl')
    percentageHpLeftFilenames = glob.glob(f'Results\\percentageHpLeft_{pokemon}*.pkl')
    turnsPerBattleFilenames = glob.glob(f'Results\\turnsPerBattle_{pokemon}*.pkl')
    currentHpPercentGameFilenames = glob.glob(f'Results\\currentHpPercentGame_{pokemon}*.pkl')
    damageDoneGameFilenames = glob.glob(f'Results\\damageDoneGame_{pokemon}*.pkl')
    usedMovesGameFilenames = glob.glob(f'Results\\usedMovesGame_{pokemon}*.pkl')
    totalBattleResults[pokemon] = {}
    totalFacedPokemon[pokemon] = {}
    totalPercentageHpLeft[pokemon] = {}
    totalTurnsPerBattle[pokemon] = {}
    totalCurrentHpPercentGame[pokemon] = {}
    totalDamageDoneGame[pokemon] = {}
    totalUsedMovesGame[pokemon] = {}
    index = 0
    for battleResultsFilename, facedPokemonFilename, percentageHpLeftFilename, turnsPerBattleFilename in zip(battleResultsFilenames, facedPokemonFilenames, percentageHpLeftFilenames, turnsPerBattleFilenames):
        with open(battleResultsFilename, 'rb') as f:
            battleResults = pickle.load(f)
        with open(facedPokemonFilename, 'rb') as f:
            facedPokemon = pickle.load(f)
        with open(percentageHpLeftFilename, 'rb') as f:
            percentageHpLeft = pickle.load(f)
        with open(turnsPerBattleFilename, 'rb') as f:
            turnsPerBattle = pickle.load(f)
        with open(currentHpPercentGameFilenames[index], 'rb') as f:
            currentHpPercentGame = pickle.load(f)
        with open(damageDoneGameFilenames[index], 'rb') as f:
            damageDoneGame = pickle.load(f)
        with open(usedMovesGameFilenames[index], 'rb') as f:
            usedMovesGame = pickle.load(f)
        totalBattleResults[pokemon][index] = battleResults
        totalFacedPokemon[pokemon][index] = facedPokemon
        totalPercentageHpLeft[pokemon][index] = percentageHpLeft
        totalTurnsPerBattle[pokemon][index] = turnsPerBattle
        totalCurrentHpPercentGame[pokemon][index] = currentHpPercentGame
        totalDamageDoneGame[pokemon][index] = damageDoneGame
        totalUsedMovesGame[pokemon][index] = usedMovesGame
        index += 1

# %% First plot (simple plot)

# Display the average (+- std) reduction of the percentage player's HP along the battle runs, for each starter pokemon
# Use totalCurrentHpPercentGame to calculate the average and std. Mind that each element of hp inside the battles is a list of the hp of the player, so to obtain hp reduction you need to calculate the difference between consecutive elements of the list
# Use the function plt.errorbar to display the results

for pokemon in starterPokemons:
    hpReduction = []
    meanHpReduction = []
    stdHpReduction = [] 
    numberOfGames = len(totalCurrentHpPercentGame[pokemon])
    for i in range(numberOfGames):
        numberOfBattles = len(totalCurrentHpPercentGame[pokemon][i])
        for j in range(numberOfBattles):
            hpArray = totalCurrentHpPercentGame[pokemon][i][j]
            hpReduction.extend(np.diff(hpArray))
        meanHpReduction.append(np.mean(hpReduction))
        stdHpReduction.append(np.std(hpReduction))
    x_data = np.arange(1, numberOfGames + 1)
    plt.plot(x_data, meanHpReduction, label=pokemon)
    plt.fill_between(x_data, np.subtract(meanHpReduction, stdHpReduction), np.add(meanHpReduction, stdHpReduction), alpha=0.2)
plt.xlabel('Game')
plt.ylabel('HP reduction')
plt.title('Average HP reduction along the games')
plt.legend()
plt.show()

#%% Second plot (pie plot)

# For each starter pokemon, display in the same figure the percentage of times each attack of the pokemon was used and the percentage of total damage done by each attack
# Use totalUsedMovesGame and totalDamageDoneGame to calculate the percentages
colors = ['green', 'red', 'blue']
fig, axs = plt.subplots(3, 2)
fig.suptitle(pokemon)
for pokemon in starterPokemons:
    numberOfGames = len(totalUsedMovesGame[pokemon])
    totalUsedMoves = {}
    totalDamageDone = {}
    for i in range(numberOfGames):
        numberOfBattles = len(totalUsedMovesGame[pokemon][i])
        for j in range(numberOfBattles):
            for move in totalUsedMovesGame[pokemon][i][j]:
                if move not in totalUsedMoves:
                    totalUsedMoves[move] = 1
                else:
                    totalUsedMoves[move] += 1
            # Append the damage done by each move. If the move is not in the dictionary, add it with the damage done
            # totalDamageDoneGame[pokemon][i][j] is an array with the damage done by each move in totalUsedMovesGame[pokemon][i][j]
            for move, damage in zip(totalUsedMovesGame[pokemon][i][j], totalDamageDoneGame[pokemon][i][j]):
                if move not in totalDamageDone:
                    totalDamageDone[move] = damage
                else:
                    totalDamageDone[move] += damage

    # Color the pie plot with different shades of the same color. For bulbasaur, use green, for charmander, use red and for squirtle, use blue
    axs[starterPokemons.index(pokemon), 0].pie(totalUsedMoves.values(), labels=totalUsedMoves.keys(), autopct='%1.1f%%')
    axs[starterPokemons.index(pokemon), 0].set_title(f'{pokemon} - Used moves')
    axs[starterPokemons.index(pokemon), 1].pie(totalDamageDone.values(), labels=totalDamageDone.keys(), autopct='%1.1f%%')
    axs[starterPokemons.index(pokemon), 1].set_title(f'{pokemon} - Damage done')    

# Set size of the figure
fig.set_size_inches(15, 15)
plt.show()



# %%
