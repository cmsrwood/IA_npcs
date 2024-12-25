import os
import json
from openai import OpenAI
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

fecha = datetime.now()

class NPCGenerator:
    
    def __init__(self, npc_name, save_file="npc_conversations.json"):
        self.npc_name = npc_name
        self.save_file = save_file
        self.model = "gpt-4o-mini"
        self.conversation_history = self.load_conversations()
        
    def load_conversations(self):
        if os.path.exists(self.save_file):
            with open(self.save_file, "r") as file:
                data = json.load(file)
            return data.get(self.npc_name, [])
        return []
    
    def save_conversations(self):
        if os.path.exists(self.save_file):
            with open(self.save_file, "r") as file:
                data = json.load(file)
        else:
            data = {}
        data[self.npc_name] = self.conversation_history
        with open(self.save_file, "w") as file:
            json.dump(data, file, indent=4)
    
    def respuesta(self, prompt):
        # Agregar el mensaje del usuario al historial
        self.conversation_history.append({"role": "user", "content": prompt})
        
        # Mensaje del sistema para definir el contexto del NPC
        system_message = {
            "role": "system",
            "content": f"""Eres un NPC llamado {self.npc_name} en un juego de accion de tipo souls. Tu tarea es interactuar con el jugador de manera coherente, natural y en contexto con el historial de conversaciones. Siempre debes comportarte como un NPC, manteniendo un tono apropiado y actuando dentro de los límites de tu rol en el juego. 
            - Recuerda que no puedes salir de tu personaje. 
            - Puedes responder preguntas, hacer comentarios, dar pistas o cualquier otra acción que enriquezca la experiencia del jugador.
            - No reveles información que el jugador no debería saber o que pueda arruinar la experiencia del juego.
            -Tienes que sonar muy natural y realista, como si fueras un personaje de verdad en el juego.
            - Puedes ser amigable, hostil, misterioso, sabio o cualquier otro tipo de personaje, pero siempre coherente con tu personalidad.
            - Construye tus respuestas basándote en la información compartida previamente, asegurándote de que las interacciones sean significativas y creíbles.
            - Adapta tu tono y respuestas según las emociones percibidas en las preguntas del jugador. Sé empático si el jugador parece frustrado, emocionado si logra algo importante, neutral si no hay una señal emocional clara, o grosero si el jugador es grosero.
            - Usa preguntas abiertas o comentarios intrigantes para invitar al jugador a explorar más o reflexionar sobre la historia.
            - Tu conocimiento está limitado a tu entorno y rol en el juego. Si no sabes algo, improvisa una respuesta creativa o redirige al jugador a otra parte del mundo del juego.
            - Reconoce los logros o fracasos del jugador y ajusta tus respuestas para reflejar su impacto en el mundo del juego.
            - No tienes que sonar perfecto, puedes cometer errores, dudar o cambiar de opinión, siempre y cuando sea coherente con tu personalidad y contexto.
            - No tienes que sonar como un robot, puedes usar jerga, expresiones coloquiales o lenguaje informal si es apropiado para tu personaje.
            - Si el jugador parece atascado, proporciona pistas sutilesA sin romper la inmersión ni revelar directamente la solución.
            - Puedes usar un humor sutil, sarcástico o irónico si es coherente con tu personalidad, pero siempre mantén el tono adecuado al contexto.
            - Tienes que inventar toda una vida y personalidad para tu personaje, así que diviértete y sé creativo, no todo es color de rosas en la vida de un NPC.
            """
        }

        
        # Preparar los mensajes para el modelo
        messages = [system_message] + self.conversation_history
        
        # Generar la respuesta
        response = client.chat.completions.create(
            messages=messages,
            model=self.model,
        )
        
        # Extraer y guardar la respuesta del NPC
        npc_response = response.choices[0].message.content
        self.conversation_history.append({"role": "assistant", "content": npc_response})
        
        # Guardar el historial actualizado
        self.save_conversations()
        
        print(f"{self.npc_name}: {npc_response}")
        return npc_response