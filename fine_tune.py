import openai
import os
from dotenv import load_dotenv

load_dotenv(r"config\.env")
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

upload_response = client.files.create(
    file=open("your_file.jsonl", "rb"),
    purpose="fine-tune"
)

file_id = upload_response["id"]
print(f"Uploaded File ID: {file_id}")

# 2. Fine-tune the model
fine_tune_response = openai.FineTune.create(
    training_file=file_id,
    model="gpt-3.5-turbo",
    n_epochs=2
)
print(f"Fine-tune started: {fine_tune_response}")
