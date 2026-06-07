from openai import OpenAI
from dotenv import load_dotenv
from scraper import fetch_website_contents
import os

load_dotenv(override= True)

model = 'llama-3.1-8b-instant'
api = os.getenv('groq_api_key')

if not api:
    print("API Key not found")

groq = OpenAI(api_key= api, base_url='https://api.groq.com/openai/v1')

def create_brochure(content):
    system_prompt = 'You are a seasoned content writer with crisp and inpormed delivery. Create a website Brochure using the content provided. Reply in Markdown with only Brochure, no other content'
    user_prompt = f'''Here's the website content- {content} '''
    message = [
        {"role" : 'system',
        "content" : system_prompt 
        },
        {
            "role" : 'user',
            "content" : user_prompt
        }
    ]
    response = groq.chat.completions.create(messages= message, model= model)
    return response.choices[0].message.content






def main():
    url = input("Enter a valid url")
    print("Getting url content")
    content = fetch_website_contents(url)
    brochure = create_brochure(content)
    print(brochure)



if(__name__ == "__main__"):
    main()