import sys
import pyttsx3

def init_engine():
    engine = pyttsx3.init()
    return engine

def say(s):
    engine.say(s)
    engine.runAndWait()
    # return 1

engine = init_engine()
engine.setProperty('rate', 160)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)

say(str(sys.argv[1]))