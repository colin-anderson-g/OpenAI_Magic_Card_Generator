import api_gen_properties
import openai
import requests

openai.api_key = api_gen_properties.API_KEY

def generate(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url =  response['data'][0]['url']

    # Download the JPEG image
    image_data_jpg = requests.get(image_url).content
    with open('image.jpg', 'wb') as f:
        f.write(image_data_jpg)
    
    # Download the PNG image
    image_url_png = image_url.replace(".jpg", ".png")
    image_data_png = requests.get(image_url_png).content
    with open('image.png', 'wb') as f:
        f.write(image_data_png)