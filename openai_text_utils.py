import api_gen_properties
import openai

openai.api_key = api_gen_properties.API_KEY

prompt = """Create a newly generated Magic the Gathering card with the name """
json_format = """\nCreate a valid json with the following fields: Name, Rarity, Types, Manacost, Supertype, subtypes, Colors, Power/toughness, loyalty, ability text with new line breaks, flavor-text"""

output_file_path = "output.txt"
output_file = open(output_file_path, "w")

def generateWithArguments(cardarguments):
    input = prompt + cardarguments.createStringArgument() + json_format
    print(input)
    conversation=[{"role": "user", "content": input}]
    request = build_request(conversation)
    response = send_request(request)
    output_file.write(response['choices'][0]['message']['content'] + "\n")
    print(f"Response saved to {output_file_path}")


def build_request(messages, model="gpt-3.5-turbo", max_tokens=1024, temperature=0.5):
    request = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    return request


def send_request(request):
    response = openai.ChatCompletion.create(**request)
    return response

