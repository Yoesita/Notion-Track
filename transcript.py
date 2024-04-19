from openai import OpenAI
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
import os

def transcript(audio_input: str):

    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    client = OpenAI(api_key=api_key)

    speech_file_path = Path(__file__).parent / audio_input

    transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=speech_file_path,
        )

    print(transcription.text)

    ahora = datetime.now()
    nombre_archivo = f'transcription_{ahora.strftime("%Y-%m-%d_%H-%M-%S")}.txt'

    with open(nombre_archivo, "w") as archivo:
        archivo.write(transcription.text)

    return nombre_archivo
