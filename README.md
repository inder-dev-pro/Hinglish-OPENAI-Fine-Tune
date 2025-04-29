# 🧠 Hinglish Voice-AI Fine-Tuning (Mini Project)

We fine-tuned OpenAI’s `gpt-3.5-turbo` model on a small conversational Hinglish dataset to make it more effective in responding to code-switched inputs involving Hindi + English (Hinglish) – a common pattern in Indian speech and casual conversations.

## 📁 Project Structure

```
hinglish-voice-ai-finetune/
│
├── nb/
    dataset.jsonl          # Hinglish prompt-completion training pairs
├── fine_tune.py           # Script to upload + fine-tune model using OpenAI API
├── inference.py           # Test fine-tuned model on new prompts
├── requirements.txt       # Required Python dependencies
└── README.md              # Project documentation
```

## ⚙️ Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set your OpenAI API Key

Make sure to set your API key as an environment variable:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

### 3. Upload Dataset & Start Fine-Tuning

```bash
python fine_tune.py
```

### 4. Run Inference on New Prompts

```bash
python inference.py
```

## 💡 Why This Dataset?

We manually curated 15 prompt-completion examples that represent natural, informal Hinglish dialogue including everyday tasks and casual tone.

## 🤖 Model Choice

- **Model**: `gpt-3.5-turbo`
- **Why?**: Chat-ready, affordable, and supports fine-tuning.

## 🔧 Hyperparameters

- **Epochs**: 2 — balanced to avoid overfitting a small dataset.

## 💬 Prompt Format

Structured as `User: ...` and `Assistant: ...` to match chat role clarity.

## 🌡️ Inference Settings

- `temperature=0.7` for balanced creativity and relevance.

## 🧪 Sample Outputs

| Prompt | Response |
|--------|----------|
| Mujhe ek chai pilao. | Zaroor! Ek garma-garam chai tayyar hai. |
| Kal ka weather batao. | Kal halka baarish ho sakti hai aur thoda cloudy rahega. |

## ✅ Evaluation Plan

Human review and feedback from Hinglish speakers for fluency and tone.
