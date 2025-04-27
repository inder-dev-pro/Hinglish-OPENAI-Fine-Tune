import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

fine_tuned_model = "ft:gpt-3.5-turbo-XXX"

prompts = [
    "Mujhe ek chai pilao.",
    "Kal ka weather batao.",
    "Kya tum cricket dekhte ho?"
]

for prompt in prompts:
    response = openai.ChatCompletion.create(
        model=fine_tuned_model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    print(f"Prompt: {prompt}")
    print(f"Reply: {response['choices'][0]['message']['content']}")
    print("------")