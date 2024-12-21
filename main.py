from Transcriber import Transcriber
from Npc_generator import NPCGenerator
from multiprocessing import freeze_support

# Crear instancias de las clases
transcriber = Transcriber()
npc_generator = NPCGenerator()

if __name__ == "__main__":
    freeze_support()
    print("Iniciando la aplicación...")
    audio_text = transcriber.transcribe_audio()
    npc_generator.respuesta(audio_text)