import api_gen_properties
import openai

openai.api_key = api_gen_properties.API_KEY

def generate(prompt):
    request = build_request(prompt)
    response = send_request(request)
    output_file_path = "output.txt"
    with open(output_file_path, "w") as output_file:
        output_file.write(response.choices[0].text)
    print(f"Response saved to {output_file_path}")


def build_request(prompt, model="text-davinci-002", max_tokens=1024, temperature=0.5):
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