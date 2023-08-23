import openai
import os

# Constants
openai.api_key = os.getenv("OPENAI_API_KEY")
engine = "davinci"
defualt_tokens = 10


def animal_fact_generator():
    # Prompt the user for an animal to generate a fact from
    animal = input("What animal would you like to learn about? ")

    # This is a placeholder and is impossible to reach right now
    if not animal_validator(animal):
        animal = input("Please enter a valid animal")
        # animal_fact_generator()
        return

    # Generate a fact about the valid animal
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


def animal_validator():
    animal_valid = input("Please enter a valid animal: ")

    for response in openai.Completion.create(
        model="text-davinci-003",
        prompt=f"is {animal_valid} a valid animal? Respond 'yes' or 'no'",
        max_tokens=30,
        temperature=0,
        stream=True
    ):
        validated = response['choices'][0]['text']
        # print(validated)
        if 'Yes' in validated or 'yes' in validated:
            print(f'Great job, "{animal_valid}" is considered a valid animal!')
            return True

        print('Not an animal (or mythical creature). Please try again!')
        return False


animal_validator()
