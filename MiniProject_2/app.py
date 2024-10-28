import os
from getpass4 import getpass
from openai import OpenAI
from dotenv import load_dotenv

# Funaction to call ChatGPT Api with query
def llm_call(context, client):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=context
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
            text = llm_call([{"role": "user", "content": query}], client)
            # Print Generated Hello World Message
            print(text)
            # Return client if llm_call successful
            return client
        except:
            # If API Key set is not valid, as if user wants to continue
            print('OpenAI API Key Set is not valid.')
            if 'n' == input('Do you want to try again (Default: Yes)? [y/n]\n'):
                print('Exitting Application')
                exit()
            else:
                # Get new API Key
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
    print('Enter your question for ChatGPT\nRemember you can only ask 10 questions at a time\nType exit to close Application')
    query = input("Enter: ")
    
    # System prompt
    context = [{"role": "system", "content": "You are a sarcastic assistant."}]
    
    # While in range keep getting new responses till the time user enters exit
    for i in range(10):
        if query != 'exit':
            # Add query as user context
            context.append({"role": "user", "content": query})
            # Make llm call
            text = llm_call(context, client)
            # Add llm response to context
            context.append({"role": "assistant", "content": text})
            # Output llm response
            print(text)
            # Get new prompt
            query = input("Prompt: ")
        else:
            break
    
    if i == 9:
        print('Oops, it looks like you have exhausted context window\nRun app again to try new prompts')
    print('Exitting Application')