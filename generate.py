import openai_text_utils
import openai_image_utils

text_prompt = """Create a new randomly generated Magic the Gathering card name TrueNear. Format as a json."""

openai_text_utils.generate(text_prompt)

image_prompt = """Create art for a Magic the Gathering card named TrueNear"""

openai_image_utils.generate(image_prompt)

