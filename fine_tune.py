import openai
import os
from dotenv import load_dotenv
load_dotenv(r"config\.env")

openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Step 1: Upload the file
file = openai_client.files.create(
    file=open(r"data/dataset.jsonl", "rb"),
    purpose="fine-tune"
)
print(f"Uploaded File ID: {file.id}")

# Step 2: Start fine-tuning
fine_tune_job = openai_client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-4o-mini-2024-07-18",
    hyperparameters={
        "n_epochs": 2}
)

print("Fine-tuning started!")
print(f"Fine-tune Job ID: {fine_tune_job.id}")
