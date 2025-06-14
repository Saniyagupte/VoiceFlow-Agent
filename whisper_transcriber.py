#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sounddevice as sd
from scipy.io.wavfile import write
import whisper
import time

def record_audio(filename="input.wav", duration=5, fs=44100):
    print(" Recording for", duration, "seconds...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(filename, fs, audio)
    print(" Recording saved to", filename)

def transcribe_audio(filename="input.wav", model_size="base"):
    print(" Loading Whisper model...")
    model = whisper.load_model(model_size)
    print(" Transcribing...")
    result = model.transcribe(filename)
    print(" Transcription:", result["text"])
    return result["text"]

def get_speech_to_text():
    timestamp = int(time.time())
    filename = f"audio_{timestamp}.wav"
    record_audio(filename)
    return transcribe_audio(filename)


# In[ ]:




# In[ ]:



