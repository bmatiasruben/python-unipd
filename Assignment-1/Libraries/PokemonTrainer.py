from Libraries.Pokemon import Pokemon
from collections.abc import Iterable

class PokemonTrainer():
    '''A class to represent a Pokemon Trainer.
    
    Contins the name, list of pokemons up to 6, and a list of items.
    '''
    def __init__(self, name, pokemons = Iterable[Pokemon], items = Iterable[str]):
        self.name = name
        self.pokemons = pokemons
        self.items = items