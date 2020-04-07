# Sign reader sample

This project is designed to be a sample Azure project using [Computer Vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/). You can use this to see how Computer Vision works, or as a starter for a project you're creating.

## Requirements

### Git

To clone the repository, you will use [Git](https://git-scm.com/).

### Python

In order to run the site you will need [Python](https://python.org) installed locally. You can install Python by visiting the [Python downloads](https://www.python.org/downloads/) page.

### Azure Cognitive Services

To use Computer Vision you will need a key for Azure Cognitive Services. We will create this by using the [Azure Portal](https://portal.azure.com).

1. Navigate to the [Azure Portal](https://portal.azure.com) and authenticate with your account.
2. Click **Create a Resource**
3. In the **Search the Marketplace** box, type **Cognitive Services**
4. Click on **Cognitive Services** in the dropdown window
5. Click **Create**
6. Complete the form
    - Enter a unique name
    - Choose the subscription
    - Choose a location near you
    - Set the [pricing tier](https://azure.microsoft.com/pricing/details/cognitive-services/) to S0
    - Click **Create New** for Resource Group and provide a name
    - If you agree to the terms, click confirm, and then **Create**
7. When the completion screen appears, click **Go to resource**
8. Make a note of the **Key** and **Endpoint** values; you'll be using those in just a few moments.

## Local setup

1. Open a command or terminal window. Clone the sample repository.

``` console
git clone https://github.com/geektrainer/computer-vision-demo
```

2. Navigate to the folder using a terminal or command window.

``` console
cd computer-vision-demo
```

3. Create a virtual environment using Python and install the libraries listed in [requirements.txt](./requirements.txt)

``` console
# Windows
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt

# macOS or Linux
python3 -m venv env
. ./env/bin/activate
pip3 install -r requirements.txt
```

4. Open the folder in the code editor of your choice. If you are using [Visual Studio Code](https://code.visualstudio.com/) you can use the command below.

``` console
code .
```

5. Add a new file named **.env**, which is used by [dotenv](https://github.com/theskumar/python-dotenv), which simulates environment variables. Add the text below, and then update the placeholders with the values you created in the earlier step.

> **NOTE**: The leading **.** is required on the file name.

``` text
COGSVCS_CLIENTURL=<your endpoint>
COGSVCS_KEY=<your key>
```
