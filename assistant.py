import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening")

        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()

        except:
            print("Sorry, I didn't understand.")
            speak("Sorry, I didn't understand.")
            return ""

# Main assistant loop
speak("Hello, I am your voice assistant.")

while True:
    command = listen()

    if "hello" in command:
        speak("Hello Teenoj")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "exit" in command:
        speak("Goodbye")
        break