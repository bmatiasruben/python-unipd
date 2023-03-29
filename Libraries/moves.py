class Move:
    def __init__(self, name, type, category, pp, **kwargs):
        self.name = name
        self.type = type
        self.category = category
        self.pp = pp
        self.stats = {}
        for key, val in kwargs.items():
            setattr(self, key, val)
            self.stats[key] = val

