from openai import OpenAI

# Replace with your OpenAI API key
api_key = 'Nuh uh'
client = OpenAI(api_key=api_key)

# Replace with your fine-tuned model ID
model_id = 'Nuh uh x 2'

# Generate a completion using the fine-tuned model
response = client.completions.create(
  model=model_id,
  prompt="What does impact admission do?",
  max_tokens=100
)
print(response['choices'][0]['text'])