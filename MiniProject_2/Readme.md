# HCI Mini Project 2 Documntation

* The API Used in this application is the OpenAI API
* The Model used is gpt-3.5-turbo


### API Integration Steps

* Login to website [OpenAI Developer API Keys](https://platform.openai.com/api-keys)
* Select the green button "Create new secret key" from the top right corner of the screen if you don't already have an api key
* Follow the instructions o screen to generate an API Key
* Make sure to copy and save the API Key someplace secure before closing the popup
* Now you have the API Key and you can use it in the application.

### Setting API Key

* In your terminal cd into the directory containing the file **app.py**
* Execute the following shell commands in your terminal
```bash
# Create .env file
touch .env

# Set API Key
echo OPENAI_API_KEY=<API-KEY> > .env
```
* Alternatively, you can skip this step and directly enter the API key after running **app.py**

### Running the Application

* Run the following commands to run the application in the terminal
* Make sure to cd into the **MiniProject_2** directory
```bash
# Create virtual environment
python -m venv ./venv 

# Activate Virtual Environemt
source venv/bin/activate

# Install Requirements
pip install -r requirements.txt 

# Run App
python app.py
```