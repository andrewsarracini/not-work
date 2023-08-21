
# from key import key1
import openai as oi
key1 = ''


# Importing the libraries

# Constants
oi.api_key = key1
engine = "davinci"
defualt_tokens = 10


def animal_fact_generator():
    # Prompt the user for an animal to generate a fact from
    animal = input("What animal would you like to learn about? ")

    # validate the input is a valid animal
    animal_validation_string = "is " + animal + \
        " a valid animal? respond with either 'yes' or 'no'"
    check = oi.Completion.create(
        engine=engine, prompt=animal_validation_string, max_tokens=1)

    # if it's not a valid animal, return
    if check['choices'][0]['text'] == "no":
        print("Sorry, that's not a valid animal")
        return

    # Prompt the user for a fact about the animal
    prompt = "Generate a random fun fact about" + \
        animal + "which is in the form of a statistic'?"
    response = oi.Completion.create(
        engine=engine, prompt=prompt, max_tokens=defualt_tokens, temperature=0.2)
    print(response)
    # print(response['choices'][0]['text'])
    return


def chart_generator():

    return


animal_fact_generator()
