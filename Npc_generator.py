import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

class NPCGenerator:
    def __init__(self):
        self.model = "gpt-4o-mini"
        
    def respuesta(self, prompt):
        response = client.chat.completions.create(
            messages=[
            {
                "role": "user",
                "content": prompt,
            },
            {
                "role": "system",
                "content" : "Eres un NPC en un juego de aventuras"
            }
            ],
            model=self.model,  
        )
        print('Respuesta: ', response.choices[0].message.content)
        return response