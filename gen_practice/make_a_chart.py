
# from key import key1
import openai
import os


# Importing the libraries

# Constants
openai.api_key = os.getenv("OPENAI_API_KEY")
engine = "davinci"
defualt_tokens = 10


def animal_fact_generator():
    # Prompt the user for an animal to generate a fact from
    animal = input("What animal would you like to learn about? ")

    # Validate the animal
    # This is ia placeholder and is impossible to reach right now
    if not animal_validator(animal):
        print("Please enter a valid animal")
        animal_fact_generator()
        return  

    # Prompt the user for a fact about the animal
    for response in openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Lifespan of {animal}",
        max_tokens=30,
        temperature=0,
        stream=True
    ):
        print(response['choices'][0]['text'])



    print(response)
    # print(response['choices'][0]['text'])
    return


def chart_generator():
    return


def animal_validator(response):
    return True


animal_fact_generator()
