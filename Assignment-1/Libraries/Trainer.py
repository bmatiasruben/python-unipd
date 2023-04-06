from Libraries.Pokemon import Pokemon

class Trainer():
    def __init__(self, name, pokemonTeam = list(Pokemon), items = []):
        self.name = name
        self.pokemonTeam = pokemonTeam
        self.items = items