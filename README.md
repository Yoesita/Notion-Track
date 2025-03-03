# Transcriptor de Videoconferencias del Lobohackaton 2024

> Propuesta de solución al desafio API Notion.

## Integrantes

- Felipe Marcial
- Juan Pablo Cielo
- Miguel Hernández
- Hozai Marquez
- Keisi Pérez
## Descripción

Se propone desarrollar un sistema que, a partir de un video/audio de una conferencia (Webinar o Presencial) transcriba su contenido a Notion.

## Objetivos

Resumir lo sus puntos clave de cualquier conferencia y enviar la información (utilizando la API de Notion) a un workspace colaborativo para su posterior analisis/evaluación.

## Funcionalidades

- Automatizar la tarea de tomar notas durante una conferencia (online/presencial).
- Resumir el contenido de la conferencia en sus puntos clave para un posterior análisis.
- Colaborar eficientemente en grupos de trabajo (desde programadores hasta creadores de contenido) que requieran las ideas clave de una conferencia.

## Tecnologias

- Python
- Flask

## Integraciones

- WhisperAI: Transcripción de audio a texto.
- ChatGPT: Resumen y obtención de palabras clave.
- ffmpeg: Renderización de video.
- Flask: Interfaz amigable con el usuario.
