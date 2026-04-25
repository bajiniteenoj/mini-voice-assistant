import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

# Initialize voice engine
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen_or_type():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening... (or type if mic fails)")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(source, timeout=5)

            command = recognizer.recognize_google(audio)
            print("You said:", command)

            return command.lower()

    except:
        # If microphone fails, switch to typing
        command = input("Type command: ")
        return command.lower()

# Start assistant
speak("Hello Teenoj, I am your assistant.")

while True:
    command = listen_or_type()

    if "hello" in command:
        speak("Hello Teenoj")

    elif "time" in command:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + time_now)

    elif "date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + today)

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "exit" in command or "stop" in command:
        speak("Goodbye Teenoj")
        break
