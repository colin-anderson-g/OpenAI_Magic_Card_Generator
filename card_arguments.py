import card_enums

class CardArguments:
    def __init__(self, input):
        self.colors = []
        self.types = []
        self.subtypes = []
        self.keywords = []
        self.Name = ""
        self.rarity = ""
        self.supertype = ""
        self.cmc = ""
        string_arguments = input.split(",")
        self.Name = string_arguments[0]
        if len(string_arguments) > 1:
            for string in string_arguments[1:]:
                string = string.strip()
                if checkIsEnum(string, card_enums.Colors):
                    self.colors.append(string)
                elif checkIsEnum(string, card_enums.Types):
                    self.types.append(string)
                elif checkIsEnum(string, card_enums.Rarity):
                    self.rarity = string
                elif checkIsEnum(string, card_enums.Supertype):
                    self.supertype = string
                elif string.isnumeric():
                    self.cmc = string
                elif "(ST)" in string.upper():
                    self.subtypes.append(string[:-4])
                elif "(KW)" in string.upper():
                    self.keywords.append(string[:-4])

    def createStringArgument(self):
        output = self.Name
        if self.colors:
            output += "\n" + self.Name + " has the colors: "
            for color in self.colors:
                output += color + " "
        if self.types:
            output += "\n" + self.Name + " has the types: "
            for type in self.types:
                output += type + " "
                if type == "Land":
                    output += "with abilities"
        if self.subtypes:
            output += "\n" + self.Name + " has the subtypes: "
            for subtypes in self.subtypes:
                output += subtypes + " "
        if self.keywords:
            output += "\n" + self.Name + " has the keywords: "
            for keyword in self.keywords:
                output += keyword + " "
        if self.rarity:
            output += "\n" + self.Name + " has the rarity: " + self.rarity
        if self.supertype:
            output += "\n" + self.Name + " has the supertype: " + self.supertype
        if self.cmc:
            output += "\n" + self.Name + " has the converted mana cost: " + self.cmc
        return output

def checkIsEnum(string, enum):
    enumValues = [member.value for member in enum]
    return string in enumValues

