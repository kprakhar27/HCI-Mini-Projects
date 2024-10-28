import os
from getpass4 import getpass
from openai import OpenAI
from dotenv import load_dotenv

# Funaction to call ChatGPT Api with query
def llm_call(query, client):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{"role":"user","content":query}]
    )
            
    return(response.choices[0].message.content)

def get_client():
    while True:
        # Set API Client
        client = OpenAI()
            
        # Test Hello World Query
        query = "Generate a creative hello world message telling API Client is working"
        
        try:
            # Get llm_call response
            text = llm_call(query, client)
            
            # Print Generated Hello World Message
            print(text)
            
            # Return client if llm_call successful
            return client
        except:
            print('OpenAI API Key Set is not valid.')
            if 'n' == input('Do you want to try again (Default: Yes)? [y/n]\n'):
                print('Entered Invalid API Key 3 Times\nExitting Application')
                exit()
            else:
                os.environ['OPENAI_API_KEY'] = getpass("Enter new OpenAI API key: \n")
    
    


    
if __name__ == '__main__':
    # Load Open AI API Key from .env if present
    load_dotenv()
    
    try:
        # Check if API key is set
        os.environ['OPENAI_API_KEY']
    except KeyError:
        print('OpenAI API Key not set as environment variable.')
        # Get API Key as input if not already set
        os.environ['OPENAI_API_KEY'] = getpass("Enter OpenAI API key: \n")
    
    # Set API Client
    client = get_client()
    
    # Run ChatGPT
    print('Enter your question for ChatGPT\nType exit to close Application')
    query = input("Enter: ")
    while query != 'exit':
        text = llm_call(query, client)
        print(text)
        query = input("Prompt: ")
    
    print('Exitting Application')