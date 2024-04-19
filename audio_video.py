from moviepy.editor import VideoFileClip
from datetime import datetime

def extract_audio(video_input):
    #video_path = "video/video.mp4"
    video = VideoFileClip(video_input)
    audio = video.audio

    #audio_path = "audios/audio_seguridad.mp3"
    ahora = datetime.now()
    nombre_archivo = f'audio_{ahora.strftime("%Y-%m-%d_%H-%M-%S")}.mp3'
    audio.write_audiofile(nombre_archivo)

    audio.close()
    video.close()


    return nombre_archivo
