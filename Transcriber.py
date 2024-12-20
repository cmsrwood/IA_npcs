import whisper
import os

class Transcriber:
    def __init__(self, file_path="player_audio.m4a"):
        self.file_path = file_path

    def transcribe_audio(self):
        
        file_path = self.file_path
        model = whisper.load_model("base")
        print ("Transcribiendo audio...")
        # Transcribir el audio
        result = model.transcribe(file_path)
        print ("Texto del audio:", result["text"])
        return result["text"]