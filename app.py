# app.py
import os, base64, json, requests
from flask import Flask, render_template, request

# Load system variables with dotenv
from dotenv import load_dotenv
load_dotenv()

# Load keys
endpoint = os.environ["COGSVCS_CLIENTURL"]
key = os.environ["COGSVCS_KEY"]

# Create vision_client
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient

vision_credentials = CognitiveServicesCredentials(key)
vision_client = ComputerVisionClient(endpoint, vision_credentials)

# Create the application
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # If it"s a GET, just return the form
    if request.method == "GET":
        # Display default page
        return render_template("index.html", image_uri="/static/placeholder.png", alt_text="Placeholder")

    # Read the file from the form
    image = request.files["file"]

    # Create a uri to display image on form
    image_uri = "data:;base64," + base64.b64encode(image.read()).decode("utf-8")

    # Reset stream back to the beginning
    image.seek(0)

    # Retrieve text from picture
    messages = extract_text_from_image(image, vision_client)

    # Reset the stream
    image.seek(0)

    # Get the caption as alt text
    alt_text = generate_caption(image, vision_client)

    # Display result
    return render_template("index.html", image_uri=image_uri, messages=messages, alt_text=alt_text)
