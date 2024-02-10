from openai import OpenAI

# use ur own api
api_key = "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"

client = OpenAI(api_key=api_key)


def chat_with_bot():
    while True:
        prompt = input("You: ")

        if prompt.lower() == 'exit':
            print("Chat ended.")
            break

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )

        response = chat_completion.choices[0].message.content
        print("Bot:", response)

# Start the chat
chat_with_bot()
