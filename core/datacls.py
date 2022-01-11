import dataclasses

@dataclasses.dataclass
class Weapon:
    name : str
    price : int = -1
     