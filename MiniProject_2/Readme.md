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

### Reflections

* Developing a basic application to generate a creative “Hello World message was a good starting to using generative AI in a simple application
* One of the initial challenges was understanding how to create a good prompt to both do the expected Hello World task while also running in the flow of the application to let the user  know that the client is live and can be used for more prompts.
* Understanding the process of adding context to the llm was also a bit challenging. Making the llm aware of the previous conversation history was tricky, you need to keep in mind the context window size and the fact that it doesn't grow too big too avoid using too many tokens which will cost money.
* I have used an arbitrary limit of 10 prompts before the system automatically exits to conserve API Credits.
* I also learned how to setup system prompts. Though they can be long, I have intentionally used a shorter prompt to conserve tokens.
* Through this process, I learned how small prompt adjustments can significantly impact the results, highlighting the importance of prompt engineering. I tried two differnt prompts
* Prompt - You are a helpful assistant.
```text
python app.py
Greetings from the API Client! 🌎✨ Just dropping by to say "Hello, World!" and let you know that I am up and running smoothly. Let's make some magic happen together through the power of API integration. Have a fantastic day! 👋🔥 #APIClient #HelloWorld
Enter your question for ChatGPT
Remember you can only ask 10 questions at a time
Type exit to close Application
Enter: sugegst a food recipe
Oh, I would be thrilled to help you with that. Here's a groundbreaking recipe for making cereal: Step 1: Open box. Step 2: Pour cereal into bowl. Step 3: Add milk. Bon appétit!
Prompt: exit
Oops, it looks like you have exhausted context window
Run app again to try new prompts
Exitting Application
```
* Prompt - You are a helpful assistant.
```text
python app.py
"Hello world! The API Client is fired up and ready to rock n' roll. Let's fetch, fetch, fetch those data and make some magic happen! 🚀🌍 #APIClientPower"
Enter your question for ChatGPT
Remember you can only ask 10 questions at a time
Type exit to close Application
Enter: sugegst a food recipe
How about trying a simple and delicious chicken stir-fry recipe? Here's a basic recipe you can follow:

Ingredients:
- 1 lb boneless, skinless chicken breasts, sliced into thin strips
- 2 tablespoons soy sauce
- 1 tablespoon sesame oil
- 1 tablespoon vegetable oil
- 2 cloves garlic, minced
- 1 onion, thinly sliced
- 1 bell pepper, thinly sliced
- 1 cup broccoli florets
- Salt and pepper to taste
- Cooked rice or noodles for serving

Instructions:
1. In a bowl, marinate the sliced chicken with soy sauce and sesame oil. Let it sit for about 15-30 minutes.
2. Heat the vegetable oil in a large skillet or wok over medium-high heat. Add the garlic and stir-fry for about 30 seconds until fragrant.
3. Add the marinated chicken to the skillet and stir-fry until cooked through, about 5-7 minutes.
4. Add the onion, bell pepper, and broccoli to the skillet and continue stir-frying for another 3-5 minutes until the vegetables are crisp-tender.
5. Season with salt and pepper to taste.
6. Serve the chicken stir-fry over cooked rice or noodles.

Enjoy your homemade chicken stir-fry! Let me know if you need more details or other recipe suggestions.
Prompt: exit
Oops, it looks like you have exhausted context window
Run app again to try new prompts
```
* We can see that just changing the system prompt can drastically change the llm response even if the user prompt is the same.
* This exercise helped me see how generative AI can be applied to add personality and variability to even the simplest tasks, enriching user interaction.
* In future projects, I plan to leverage this experience to test more diverse apis such as image to text, or text to image, or speech to text models which can be used in creative ways for generating educational content personalised to each users needs.

### References

* The following code was referenced from the website [OpenAI Developer Platform](https://platform.openai.com/)
```python
from openai import OpenAI
client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)
```