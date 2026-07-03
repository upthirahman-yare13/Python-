from openai import OpenAI

client = OpenAI(api_key="Halkan-soo-geli-furahaaga")

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": "Hello! Sidee tahay?"}]
)

print(response.choices[0].message.content)
