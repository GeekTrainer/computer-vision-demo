import os
from dotenv import load_dotenv
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

# Load the .env file
load_dotenv()

# Read the values
key = os.getenv('COGSVCS_KEY')
endpoint = os.getenv('COGSVCS_CLIENTURL')

# Create the credentials
credentials = CognitiveServicesCredentials(key)

# Create the client
client = ComputerVisionClient(endpoint, credentials)

with open('sample.jpg', 'rb') as image:
    description = client.describe_image_in_stream(image)
    for tag in description.tags:
        print(f'- {tag}')
    image.seek(0)
    text_results = client.recognize_printed_text_in_stream(image)
    messages = []
    for region in text_results.regions:
        for line in region.lines:
            messages.append(' '.join(word.text for word in line.words))
            # for word in line.words:
            #     print(word.text)
    print(messages)