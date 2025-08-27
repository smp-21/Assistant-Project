import speech_recognition as sr
import pyaudio
import webbrowser
import pyttsx3
import json

with open("./music.json") as f:
    music_library = json.load(f)


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()
    
    if "open" in c:
        try:
            site = c.split("open ")[1].strip()
            url = f"https://{site}.com"
            speak(f"Opening {site}")
            webbrowser.open(url)
        except:
            speak("Sorry, I couldn't open that site.")
    
    elif "play" in c:
        parts = c.split(" ")
        if len(parts) > 1:
            song = parts[1]
            if song in music_library:
                link = music_library[song]
                speak(f"Playing {song}")
                webbrowser.open(link)
            else:
                speak("Sorry, that song is not in my library.")
        else:
            speak("Please say the song name after 'play'.")

    else:
        speak("Sorry, I don't understand that command.")

if __name__ == "__main__":
    speak("Initializing Assistant....")
    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
                word = recognizer.recognize_google(audio)

                if "siri" in word.lower():
                    speak("Yes?")
                    print("Wake word detected. Awaiting command. ..")

                    with sr.Microphone() as source:
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        print(f"You said: {command}")
                        processCommand(command)

        except sr.WaitTimeoutError:
            pass  
        except Exception as e:
            print(f"Error: {e}")