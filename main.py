from Transcriber import Transcriber
from Npc_generator import NPCGenerator
from pynput import keyboard

# Crear instancias de las clases
transcriber = Transcriber()
npc_generator = NPCGenerator()

# Función para cuando se presiona una tecla
def on_press(key):
    try:
        # Si se presiona la barra espaciadora, empezar a grabar
        if key == keyboard.Key.space:  # Cambia esto si prefieres otra tecla
            print("Iniciando grabación...")
            audio_data = transcriber.record_audio()  # Graba el audio
            audio_text = transcriber.transcribe_audio(audio_data)  # Transcribe el audio
            npc_generator.respuesta(audio_text)  # Llama a la respuesta del NPC

        # Si se presiona 'esc' salir del programa
        if key == keyboard.Key.esc:
            print("Saliendo...")
            return False  # Detiene el listener

    except Exception as e:
        print(f"Error: {e}")

# Configura el listener del teclado
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
