from openai import OpenAI

# use ur own api key
api_key = "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"

client = OpenAI(api_key=api_key)

class OpenAIBot:
    def __init__(self, engine):

        self.conversation = [{"role": "system", "content": "You are a helpful assistant."}]
        self.engine = engine

    def add_message(self, role, content):

        self.conversation.append({"role": role, "content": content})

    def generate_response(self, prompt):

        self.add_message("user", prompt)
        try:

            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="gpt-3.5-turbo",
            )

            assistant_response = response['choices'][0]['message']['content'].strip()

            self.add_message("assistant", assistant_response)

            return assistant_response
        except:
            print('Error Generating Response!')
