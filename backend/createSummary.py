import openai
import os
import io
from google.cloud import vision
from dotenv import load_dotenv

load_dotenv('.env') 
print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])

def createSummary(img):

    client = vision.ImageAnnotatorClient()
    with io.open("uploaded_images/"+img, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    response = client.text_detection(image=image)

    texts = response.text_annotations

    print("~~~~~~要約前~~~~~~")
    output_text = ""
    for text in texts:
        output_text += text.description

    output_text = output_text.replace(" ", "").replace("\n", "")
    print(output_text)

    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="この文章を小学生にもわかりやすく要約してください。また、幼児に語りかけるような口調で説明してください。:\n\n" + output_text,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print("~~~~~~要約後~~~~~~")
    print(response.choices[0].text.strip())

    return response.choices[0].text.strip()