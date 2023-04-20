from Libraries.Pokemon import Pokemon
from collections.abc import Iterable

class PokemonTrainer():
    def __init__(self, name, pokemons = Iterable[Pokemon], items = Iterable[str]):
        self.name = name
        self.pokemons = pokemons
        self.items = items