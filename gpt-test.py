from openai import OpenAI
import openai
import json
import os

PATH = os.path.dirname(os.path.realpath(__file__))
with open(PATH + "/config.json") as f:
    config = json.load(f)

client = OpenAI(api_key=config["token"])

msgs = [
        {"role": "system", "content": "You are a tsundere girl."}
        ]


while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break

    msgs.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=msgs
    )
    bot_output = response.choices[0].message.content
    msgs.append({"role": "assistant", "content": bot_output})

    print("Bot:", bot_output)
