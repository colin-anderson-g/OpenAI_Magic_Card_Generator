import api_gen_properties
import openai
import card_arguments

openai.api_key = api_gen_properties.API_KEY

prompt = """Create a new randomly generated Magic the Gathering card with the name """
json_format = """\nCreate a valid json object for the card into the following format:
{
    "Name": "Card Name",
    "Rarity": "Rarity of Card",
    "Type": "The card Types in an array",
    "Manacost": "The manacost of the card with colors",
    "CMC": The converted manacost of the card,
    "Supertype": "The supertype of the card",
    "Subtype": "The subtypes of the card in an array",
    "Colors": "The colors of the card in an array",
    "Power": "The power of the card",
    "Toughness": "The toughness of the card",
    "Loyalty": "The starting loyalty of the card",
    "Art-Description": "The description of the art of the card",
    "Abilities": "The abilities of the card in an array",
    "Flavor-Text": "The flavor text of the card",
}"""

output_file_path = "output.txt"
output_file = open(output_file_path, "w")

def generateWithArguments(cardarguments):
    print(cardarguments.createStringArgument())
    input = prompt + cardarguments.createStringArgument() + json_format
    request = build_request(input)
    response = send_request(request)
    output_file.write(response.choices[0].text)
    print(f"Response saved to {output_file_path}")


def build_request(prompt, model="text-davinci-003", max_tokens=1024, temperature=0.5):
    request = {
        "model": model,
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    return request


def send_request(request):
    response = openai.Completion.create(**request)
    return response

