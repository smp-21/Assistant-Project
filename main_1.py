import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musicLibrary
import requests
import json

# pip install pocketsphinx
# pip install pygame

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.2)

# Here goes your personal api key
newsapi = "d093053d72bc40248998159804e0e67d"
    
def processCommand(c):
    # print(c)
    # pass
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            # Extract the articles
            articles = data.get('articles', [])
            # Print the headlines
            for article in articles:
                print(article[ 'title'])
            
    
if __name__=="__main__":
    speak("Initializing Jarvis...........")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        # recognize speech using Sphinx or google
        print("recognizing...")
        try:
            # word = r.recognize_sphinx(audio)
            with sr.Microphone() as source:
                print("Listening...")
                # audio = r.listen(source, timeout=2, phrase_time_limit=5)
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            print(word)
            if(word.lower() == "jarvis"):
                speak("Yes?")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
            
                    processCommand(command)
            
        except Exception as e:
            print("Error : {0}".format(e))
            
        # except sr.UnknownValueError:
        #     print("Sphinx could not understand audio")
        # except sr.RequestError as e:ˀˀ
        #     print("Sphinx error: {0}".format(e))