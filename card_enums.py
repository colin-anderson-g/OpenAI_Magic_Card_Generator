from enum import Enum

class Colors(Enum):
    White = "White"
    Blue = "Blue"
    Black = "Black"
    Red = "Red"
    Green = "Green"

class Types(Enum):
    Land = "Land"
    Artifact = "Artifact"
    Creature = "Creature"
    Enchantment = "Enchantment"
    Instant = "Instant"
    Sorcery = "Sorcery"
    Planeswalker = "Planeswalker"

class Rarity(Enum):
    Common = "Common"
    Uncommon = "Uncommon"
    Rare = "Rare"
    Mythic = "Mythic"

class Supertype(Enum):
    Legendary = "Legendary"
    Snow = "Snow"
