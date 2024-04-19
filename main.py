from audio_video import extract_audio
from transcript import transcript
from prompt import prompt_summarize

def main():

    video_input = "video/video.mp4"

    # Extract audio from video
    print("Extracting audio from video...")
    audio_input = extract_audio(video_input)

    # Transcribe audio 
    print("Transcribing audio...")
    transcript_output = transcript(audio_input)

    # Summarize transcription
    print("Summarizing transcription...")
    summ = prompt_summarize(transcript_output)

    print(f'Summary: {summ}')

if __name__ == "__main__":
    main()
