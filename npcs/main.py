from Transcriber import Transcriber
from Npc_generator import NPCGenerator
import keyboard

if __name__ == "__main__":
    
    transcriber = Transcriber()
    npc = NPCGenerator("Camilo")  # Crear un NPC

    print("Mantén presionada la barra espaciadora para grabar audio. Presiona 'esc' para salir.")
    
    while True:
        try:
            # Detectar si la barra espaciadora está presionada
            if keyboard.is_pressed("space"):
                print("Iniciando grabación...")
                audio_data = transcriber.record_audio()  # Grabar audio mientras se mantenga presionada
                audio_text = transcriber.transcribe_audio(audio_data)  # Transcribir el audio
                print(f"Texto transcrito: {audio_text}")
                npc.respuesta(audio_text) # Obtener la respuesta del NPC
            
            # Salir del programa si se presiona 'esc'
            if keyboard.is_pressed("esc"):
                print("Saliendo...")
                break

        except Exception as e:
            print(f"Error: {e}")
