import openai_text_utils
import openai_image_utils
import card_arguments

# openai_text_utils.generateWithArguments(card_arguments.CardArguments("True Near")) 
# it can still be called like this using just the name of the card

image_prompt = """Create art for a Magic the Gathering card named TrueNear"""

openai_image_utils.generate(image_prompt)

with open("input.txt", "r") as input_file:
    num_lines = sum(1 for line in open('input.txt'))
    i = 1
    for line in input_file:
        arguments = card_arguments.CardArguments(line)
        openai_text_utils.generateWithArguments(arguments)
        print("finsihed with " + str(i) + "/" + str(num_lines) + "\n")
        i += 1

