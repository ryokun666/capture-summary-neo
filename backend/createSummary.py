import openai
import os
import io
from google.cloud import vision

def createSummary(img):

    client = vision.ImageAnnotatorClient()
    with io.open("uploaded_images/"+img, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    response = client.text_detection(image=image)

    texts = response.text_annotations

    output_text = ""
    for text in texts:
        output_text += text.description

    print(output_text)
    output_text = output_text.replace(" ", "").replace("\n", "")

    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=output_text,
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=1
    )

    return response.choices[0].text.strip()