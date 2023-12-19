import pyttsx3
import pyperclip, re

text = pyperclip.paste()

text_cleaned  = re.sub("[\s\n\.\/]+"," ", text)
word_count = len(text_cleaned.split())
text_to_speak = f"{word_count} words"


engine = pyttsx3.init()

engine.setProperty('rate', 200) 
engine.setProperty('volume', 0.8) 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[11].id)

engine.say(text_to_speak)

engine.runAndWait()