import pyaudio
import wave
from pydub import AudioSegment
from pydub.playback import play
import requests
import subprocess
import os

def recAudio():
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 44100
    seconds = 5
    filename = "./speeches/stt.wav"

    p = pyaudio.PyAudio()

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    sound = AudioSegment.from_file('./speeches/stt.wav', format='wav')
    sound.export('./speeches/stt.flac', format='flac')

def getText():
    API_ENDPOINT = "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/4defdcc5-8735-4626-8d6b-8188ceb5c809/v1/recognize" 
    API_KEY = "apikey:HZvhBrtA4EGIxYnKJJv8GQOBPeNaJlTXkXPeIIKEVE7V"
    PATH = "@/home/pi/COLLEGE-PROJECT/illiterate-blind/speeches/sample.flac"
    HEADER = "Content-Type: audio/flac"

    api_call_open = 'curl -X POST -u "{}"  --header "{}"  --data-binary {}  "{}"'
    api_call = api_call_open.format(API_KEY,HEADER,PATH,API_ENDPOINT);

    output = os.system(api_call)
    print(output)

recAudio()
getText()
