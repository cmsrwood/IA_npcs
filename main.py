from Transcriber import Transcriber
from Npc_generator import NPCGenerator
from multiprocessing import freeze_support

# Crear instancias de las clases
transcriber = Transcriber()
npc_generator = NPCGenerator( "John", 25)

if __name__ == "__main__":
    freeze_support()
    print("Iniciando la aplicación...")
    audio_text = transcriber.transcribe_audio()