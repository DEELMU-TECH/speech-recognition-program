# -*- coding: utf-8 -*-
"""
Created on Sat May  1 17:25:32 2021

@author: deelmutech technologies
"""
import speech_recognition as sr
 
r = sr.Recognizer()

with sr.Microphone() as source:
    print('speak anything: ')
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print('you said: {}'.format(text))
    except:
        print('sorry we couldnt recognize your voice')

