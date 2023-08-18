key = "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"



# Importing the libraries
import openai as oi

#Move This later
oi.api_key = key
#print(oi.Model.list())

prompt = "Who wrote the book 'The Fault in Our Stars'?"
response = oi.Completion.create(engine="davinci", prompt=prompt, max_tokens=5)
print(response)
# print(response['choices'][0]['text'])


