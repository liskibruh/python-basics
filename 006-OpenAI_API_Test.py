#pip install openai
import openai

openai.api_key = "<enter your api key>"
response = openai.Completion.create(model="text-davinci-003", prompt="Write me a paragraph on the role of statistics in data sciences", temperature=0, max_tokens=1000)


print(response['choices'][0]['text'])