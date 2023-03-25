import card_enums

class CardArguments:
    Name = ""
    rarity = ""
    supertype = ""
    keyword = ""
    colors = []
    types = []

    def __init__(self, input):
        self.colors = []
        self.types = []
        self.Name = ""
        self.rarity = ""
        self.supertype = ""
        self.keyword = ""
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
                else:
                    self.keyword = string

    def createStringArgument(self):
        output = self.Name
        if self.colors:
            output += "\nThe card has the colors: "
            for color in self.colors:
                output += color + " "
        if self.types:
            output += "\nThe card has the types: "
            for type in self.types:
                output += type + " "
        if self.rarity:
            output += "\nThe card has the rarity: " + self.rarity
        if self.supertype:
            output += "\nThe card has the supertype: " + self.supertype
        if self.keyword:
            output += "\nThe card has a brand new keyword: " + self.keyword
        return output

def checkIsEnum(string, enum):
    enumValues = [member.value for member in enum]
    return string in enumValues

