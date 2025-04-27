'''from gtts import gTTS
from playsound import playsound
import tempfile
import os

def speak(text):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tts = gTTS(text)
        tts.save(tmp.name)
        tmp_path = tmp.name

    playsound(tmp_path)
    os.remove(tmp_path)'''''

from gtts import gTTS
from playsound import playsound
import tempfile
import os

def speak(text, lang='en'):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tts = gTTS(text=text, lang=lang)
        tts.save(tmp.name)
        tmp_path = tmp.name

    playsound(tmp_path)
    os.remove(tmp_path)



     