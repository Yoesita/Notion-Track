from openai import OpenAI
from datetime import datetime
from dotenv import load_dotenv
import os

def prompt_summarize(summ_path: str):

    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    client = OpenAI(api_key=api_key)

    with open(summ_path, 'r') as file:
        mi_texto = file.read()

    message = f"""
    Te pasaré un texto que es la transcripción de una conferencia. Quiero que extraigas de ahi lo siguiente:

    - Nombre de la conferencia
    - Resumen de la conferencia
    - Keynotes y temas relevantes

    Hazlo con el siguiente formato:

    [Nombre de la conferencia]

    Resumen;
    [Resumen de la conferencia]

    Keynotes:
    [Keynotes y temas relevantes]

    {mi_texto}
    """

    response = client.chat.completions.create(
      model="gpt-4-turbo-preview",
      #response_format={ "type": "json_object" },
      messages=[
        {"role": "system", "content": "Eres un asistente muy util que resume conferencias a las que no puedo asistir y no pierdes ningun detalle"},
        {"role": "user", "content": message}
      ]
    )

    print(response.choices[0].message.content)

    result = f"{response.choices[0].message.content}"
    print(result)

    ahora = datetime.now()
    nombre_archivo = f'summ_{ahora.strftime("%Y-%m-%d_%H-%M-%S")}.txt'

    with open(nombre_archivo, "w") as archivo:
        archivo.write(result)

    return nombre_archivo
