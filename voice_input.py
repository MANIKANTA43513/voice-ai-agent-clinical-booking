import os
import whisper
import sounddevice as sd
import numpy as np
import requests

# FFmpeg path fix (important for Windows)
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg-8.0.1-essentials_build\ffmpeg-8.0.1-essentials_build\bin"

# Load Whisper model
model = whisper.load_model("base")

# Record audio
def record_audio(duration=5, samplerate=16000):
    print("Speak now...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    return audio.flatten(), samplerate

# Convert speech to text
def speech_to_text():
    audio, samplerate = record_audio()

    # Save temp audio file
    audio_file = "temp_audio.wav"
    import soundfile as sf
    sf.write(audio_file, audio, samplerate)

    result = model.transcribe(audio_file)
    text = result["text"]

    print("Detected text:", text)
    return text

# Send text to AI agent backend
def send_to_agent(text):
    url = "http://127.0.0.1:8000/process"

    data = {
        "message": text
    }

    try:
        response = requests.post(url, json=data)
        print("AI Agent Response:", response.json())
    except Exception as e:
        print("Server error:", e)

# Main
if __name__ == "__main__":
    text = speech_to_text()
    send_to_agent(text)