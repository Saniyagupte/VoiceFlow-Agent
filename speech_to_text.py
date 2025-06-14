#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import speech_recognition as sr

def get_speech_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Speak now...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"📝 You said: {text}")
        return text
    except sr.UnknownValueError:
        print(" Could not understand.")
        return None
    except sr.RequestError:
        print(" API error.")
        return None

# In[ ]:




# In[ ]:



