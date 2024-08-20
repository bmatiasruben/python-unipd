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
for pokemon in starterPokemons:
    battleResultsFilenames = glob.glob(f'Results\\battleResults_{pokemon}*.pkl')
    facedPokemonFilenames = glob.glob(f'Results\\facedPokemon_{pokemon}*.pkl')
    percentageHpLeftFilenames = glob.glob(f'Results\\percentageHpLeft_{pokemon}*.pkl')
    turnsPerBattleFilenames = glob.glob(f'Results\\turnsPerBattle_{pokemon}*.pkl')
    totalBattleResults[pokemon] = {}
    totalFacedPokemon[pokemon] = {}
    totalPercentageHpLeft[pokemon] = {}
    totalTurnsPerBattle[pokemon] = {}
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
        totalBattleResults[pokemon][index] = battleResults
        totalFacedPokemon[pokemon][index] = facedPokemon
        totalPercentageHpLeft[pokemon][index] = percentageHpLeft
        totalTurnsPerBattle[pokemon][index] = turnsPerBattle
        index += 1

# %% Do the first plot (simple plot)
colors = ['g', 'r', 'b']

for i, pokemon in enumerate(starterPokemons):
    victories = []
    for game in totalBattleResults[pokemon].values():
        victories.append(sum([1 for battle in game if battle == 'Won']))
    plt.plot(victories, color=colors[i], label=f'{pokemon} \nAvg wins = {np.mean(victories)}', alpha=0.5)
    plt.title(f'Number of victories for all starters')
    plt.xlabel('Game')
    plt.ylabel('Number of victories')

plt.gcf().set_size_inches(12, 8)
plt.tight_layout()
plt.legend()
# save the plot as pdf
plt.savefig('Results\\victories.pdf')
plt.show()

# %% Do the second plot (box plot)

# Display the distribution of the number of turns in each battle
for i, pokemon in enumerate(starterPokemons):
    turns = []
    for game in totalTurnsPerBattle[pokemon].values():
        turns.extend(game)
    plt.boxplot(turns, positions=[i], widths=0.6, showfliers=False)
    plt.title(f'Number of turns per battle for all starters')
    plt.xlabel('Pokemon')
    plt.ylabel('Number of turns')
plt.xticks(range(len(starterPokemons)), starterPokemons)
plt.gcf().set_size_inches(12, 8)
plt.tight_layout()
plt.savefig('Results\\turnsPerBattle.pdf')
plt.show()

# Display the distribution of the residual player's HP in each battle. This has to take elements from totalPercentageHpLeft where battleResults == 'Won'
for i, pokemon in enumerate(starterPokemons):
    percentageHpLeft = []
    for game, gameResults in zip(totalPercentageHpLeft[pokemon].values(), totalBattleResults[pokemon].values()):
        percentageHpLeft.extend([percentage for percentage, result in zip(game, gameResults) if result == 'Won'])
    plt.boxplot(percentageHpLeft, positions=[i], widths=0.6, showfliers=False)
    plt.title(f'Percentage of HP left for all starters')
    plt.xlabel('Pokemon')
    plt.ylabel('Percentage of HP left')
plt.xticks(range(len(starterPokemons)), starterPokemons)
plt.gcf().set_size_inches(12, 8)
plt.tight_layout()
plt.savefig('Results\\percentageHpLeft.pdf')
plt.show()

# Compute and show the distributions mean, median, 25th and 75th quantiles
for i, pokemon in enumerate(starterPokemons):
    percentageHpLeft = []
    for game, gameResults in zip(totalPercentageHpLeft[pokemon].values(), totalBattleResults[pokemon].values()):
        percentageHpLeft.extend([percentage for percentage, result in zip(game, gameResults) if result == 'Won'])
    plt.boxplot(percentageHpLeft, positions=[i], widths=0.6)
    plt.title(f'Percentage of HP left for all starters')
    plt.xlabel('Pokemon')
    plt.ylabel('Percentage of HP left')
    plt.axhline(y=np.mean(percentageHpLeft), color='r', linestyle='--', label='Mean')
    plt.axhline(y=np.median(percentageHpLeft), color='g', linestyle='--', label='Median')
    plt.axhline(y=np.quantile(percentageHpLeft, 0.25), color='b', linestyle='--', label='25th quantile')
    plt.axhline(y=np.quantile(percentageHpLeft, 0.75), color='b', linestyle='--', label='75th quantile')
plt.xticks(range(len(starterPokemons)), starterPokemons)
plt.gcf().set_size_inches(12, 8)
plt.tight_layout()
plt.legend()
plt.savefig('Results\\percentageHpLeftWithStats.pdf')
plt.show()

# %% Do the third plot (bar charts)
from Libraries.BasePokemon import basePokemonList

# Get the unique enemy pokemons
uniqueFacedPokemon = {}
for pokemon in starterPokemons:
    uniqueFacedPokemon[pokemon] = set()
    for game in totalFacedPokemon[pokemon].values():
        uniqueFacedPokemon[pokemon].update(game)
    uniqueFacedPokemon[pokemon] = list(uniqueFacedPokemon[pokemon])
    # Sort the unique enemy pokemons by pokedex number. The info is stored in basePokemonList
    uniqueFacedPokemon[pokemon].sort(key=lambda x: basePokemonList[x].pokedexNumber)

# Create a dictionary to store the number of battles won by each starter against each unique enemy pokemon
battlesWon = {}
totalBattles = {}
for pokemon in starterPokemons:
    battlesWon[pokemon] = {}
    totalBattles[pokemon] = {}
    for enemyPokemon in uniqueFacedPokemon[pokemon]:
        battlesWon[pokemon][enemyPokemon] = 0
        totalBattles[pokemon][enemyPokemon] = 0
        for game, gameResults in zip(totalFacedPokemon[pokemon].values(), totalBattleResults[pokemon].values()):
            battlesWon[pokemon][enemyPokemon] += sum([1 for facedPokemon, battle in zip(game, gameResults) if facedPokemon == enemyPokemon and battle == 'Won'])
            totalBattles[pokemon][enemyPokemon] += sum([1 for facedPokemon in game if facedPokemon == enemyPokemon])

# Create a dictionary to store the residual player's HP at the end of each battle. This has to take elements from totalPercentageHpLeft where battleResults == 'Won'
percentageHpLeft = {}
for pokemon in starterPokemons:
    percentageHpLeft[pokemon] = {}
    for enemyPokemon in uniqueFacedPokemon[pokemon]:
        percentageHpLeft[pokemon][enemyPokemon] = []
        for game, gameResults, gameHpLeft in zip(totalFacedPokemon[pokemon].values(), totalBattleResults[pokemon].values(), totalPercentageHpLeft[pokemon].values()):
            percentageHpLeft[pokemon][enemyPokemon].extend([percentage for facedPokemon, result, percentage in zip(game, gameResults, gameHpLeft) if facedPokemon == enemyPokemon and result == 'Won'])

# Create a dictionary to store the number of turns in each battle. This has to take elements from totalTurnsPerBattle where battleResults == 'Won'
turnsPerBattle = {}
for pokemon in starterPokemons:
    turnsPerBattle[pokemon] = {}
    for enemyPokemon in uniqueFacedPokemon[pokemon]:
        turnsPerBattle[pokemon][enemyPokemon] = []
        for game, gameResults, gameTurns in zip(totalFacedPokemon[pokemon].values(), totalBattleResults[pokemon].values(), totalTurnsPerBattle[pokemon].values()):
            turnsPerBattle[pokemon][enemyPokemon].extend([turns for facedPokemon, result, turns in zip(game, gameResults, gameTurns) if facedPokemon == enemyPokemon and result == 'Won'])

# Create the bar chart. One graph for each starter pokemon
for i, pokemon in enumerate(starterPokemons):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    x = np.arange(len(uniqueFacedPokemon[pokemon]))
    barWidth = 0.4
    ax1.bar(x - barWidth/2, [100*battlesWon[pokemon][enemyPokemon]/totalBattles[pokemon][enemyPokemon] for enemyPokemon in uniqueFacedPokemon[pokemon]], width=barWidth, color='b', label='Battles won', alpha=0.5)
    ax2.bar(x + barWidth/2, [np.mean(percentageHpLeft[pokemon][enemyPokemon]) for enemyPokemon in uniqueFacedPokemon[pokemon]], width=barWidth, color='r', label='Mean HP left', alpha=0.5)
    ax2.errorbar(x + barWidth/2, [np.mean(percentageHpLeft[pokemon][enemyPokemon]) for enemyPokemon in uniqueFacedPokemon[pokemon]], yerr=[np.std(percentageHpLeft[pokemon][enemyPokemon]) for enemyPokemon in uniqueFacedPokemon[pokemon]], fmt='none', color='black', alpha=0.5)
    for j, enemyPokemon in enumerate(uniqueFacedPokemon[pokemon]):
        if battlesWon[pokemon][enemyPokemon]/totalBattles[pokemon][enemyPokemon] > 0.7 and np.mean(percentageHpLeft[pokemon][enemyPokemon]) > 70:
            ax1.annotate(f'{enemyPokemon} (N)', (j, 100*battlesWon[pokemon][enemyPokemon]/totalBattles[pokemon][enemyPokemon]), textcoords="offset points", xytext=(0,10), ha='center', rotation=90)
        if 0.7 > battlesWon[pokemon][enemyPokemon]/totalBattles[pokemon][enemyPokemon] > 0.5 and np.mean(turnsPerBattle[pokemon][enemyPokemon]) > np.mean([turn for game in totalTurnsPerBattle[pokemon].values() for turn in game]):
            ax1.annotate(f'{enemyPokemon} (S)', (j, 100*battlesWon[pokemon][enemyPokemon]/totalBattles[pokemon][enemyPokemon]), textcoords="offset points", xytext=(0,10), ha='center', rotation=90)
    ax1.set_xlabel('Enemy Pokemon')
    ax1.set_ylabel('Number of battles won')
    ax2.set_ylabel('Mean HP left')
    ax1.set_title(f'Number of battles won and mean HP left for {pokemon}')
    ax1.set_xticks(x)
    ax1.set_xticklabels(uniqueFacedPokemon[pokemon], rotation=90)
    ax1.set_ylim(0, 122)
    ax2.set_ylim(0, 122)
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    fig.set_size_inches(20, 8)
    plt.tight_layout()
    plt.savefig(f'Results\\battlesWonAndMeanHpLeft_{pokemon}.pdf')
    plt.show()




# %%
