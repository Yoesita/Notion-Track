# Transcriptor de Videoconferencias del Lobohackaton 2024

> Propuesta de solución al desafio API Notion.

## Descripción

Se propone desarrollar un sistema que, a partir de un video/audio de una conferencia (Webinar o Presencial) transcriba su contenido y lo resuma en sus puntos clave para posteriormente utilizar la API de Notion y para enviar los punto clave a un workspace colaborativo.

## Funcionalidades

- Automatizar la tarea de tomar notas durante una conferencia (online/presencial).
- Resumir el contenido de la conferencia en sus puntos clave para un posterior análisis.
- Colaborar eficientemente en grupos de trabajo (desde programadores hasta creadores de contenido) que requieran las ideas clave de una conferencia.

## Integraciones

- WhisperAI: Transcripción de audio a texto.
- ChatGPT: Resumen y obtención de palabras clave.
- ffmpeg: Renderización de video.
- Flask: Interfaz amigable con el usuario.
