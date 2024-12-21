import whisper
import pyaudio
import numpy as np

class Transcriber:
    def __init__(self, model_size="base"):
        # Cargar el modelo de Whisper
        self.model = whisper.load_model(model_size)
        self.fs = 16000  # Frecuencia de muestreo
        self.duration = 5  # Duración de la grabación en segundos
        self.p = pyaudio.PyAudio()  # Instancia de PyAudio

    def record_audio(self):
        stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=self.fs,
        input=True, frames_per_buffer=1024)
        print("Escuchando...")
        frames = []
        for _ in range(0, int(self.fs / 1024 * self.duration)):  # Graba 5 segundos
            data = stream.read(1024)
            frames.append(data)
        print("Grabación terminada")
        stream.stop_stream()
        stream.close()
        
        # Convertir el audio grabado a un arreglo de numpy y luego a float32
        audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)
        audio_data = audio_data.astype(np.float32)  # Convertir a float32
        audio_data /= 32768.0  # Normalizar a rango [-1, 1] para Whisper
        return audio_data

    def transcribe_audio(self, audio_data):
        print("Transcribiendo...")
        result = self.model.transcribe(audio_data)
        print(f"Texto transcrito: {result['text']}")
        return result["text"]
