import openai
import os

animal = input('What animal would you like to learn about?')

openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = os.environ['OPENAI_API_KEY']

for chunk in openai.Completion.create(
    model="text-davinci-003",
    prompt=f"make a joke about {animal}",
    max_tokens=30,
    temperature=0,
    stream=True
):
    print(chunk['choices'][0]['text'])
