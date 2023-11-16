class Ressource:
    Wheat: int = 0
    Wood: int = 0
    Stone: int = 0
    Gold: int = 0

    def __init__(self, Wheat, Wood, Stone, Gold):
        self.Wheat = Wheat
        self.Wood = Wood
        self.Stone = Stone
        self.Gold = Gold
    
    def __add__(self, o):
        return Ressource(
            self.Wheat + o.Wheat,
            self.Wood + o.Wood,
            self.Stone + o.Stone,
            self.Gold + o.Gold,
        )
    
    def __mul__(self, o):
        return Ressource(
            self.Wheat * o,
            self.Wood * o,
            self.Stone * o,
            self.Gold * o,
        )
    
    def __ge__(self, o):
        return self.Wheat >= o.Wheat and self.Wood > o.Wood and self.Stone >= o.Stone and self.Gold >= o.Gold