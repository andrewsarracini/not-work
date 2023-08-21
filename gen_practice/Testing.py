import openai
key = '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'

animal = input('What animal would you like to learn about?')

openai.api_key = key
for chunk in openai.Completion.create(
    model="text-davinci-003",
    prompt=f"2 facts about {animal}?",
    max_tokens=30,
    temperature=0,
    stream=True
):
    print(chunk['choices'][0]['text'])
