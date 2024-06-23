from openai import OpenAI
client = OpenAI(api_key="nuh uh, i wont show you tokens")

print(client.files.create(
  file=open("teach.jsonl", "rb"),
  purpose="fine-tune"
))