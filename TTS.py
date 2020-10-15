from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

def createSpeech():
    convotext = open("./texts/tts.txt","r")
    convostring = convotext.read()
    language = "en"
    speech = gTTS (text = convostring, lang = language, slow=False)
    speech.save("./speeches/tts.wav")
    os.system('ffplay ./speeches/tts.wav')
    # sound = AudioSegment.from_wav('./speeches/tts.wav')
    # play(sound)

