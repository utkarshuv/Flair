import pyttsx3
import google.generativeai as genai
import speech_recognition as sr
from AppOpener import open, close

wait_commands = ['bye', 'nothing as of now', 'nothing']

def running():
    while True:
        speak('Yes Mr Verma, What can I do for you?')
        print('main loop')
        command = listen()
        print('main loop command: ', end='')
        print(command)
        if command == 'sleep':
            speak('Turning off, please start me if you need anything else.')
            break
        elif ('how are you' in command) or ('how r u' in command):
            speak('I am good, thank you for asking, what can I do for you?')
        elif command == 'open notepad':
            speak('Opening Notepad')
            open('notepad')
        elif command == 'open browser':
            speak('Opening Brave')
            open("brave")
        elif command in wait_commands:
            wait()
        else:
            print('else block')

def wait():
    while True:
        print('waiting loop')
        command = listen()
        if command == 'flair':
            break

def start_up():
    global engine
    engine = pyttsx3.init()
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[1].id)
    # rate = engine.getProperty('rate')
    # engine.setProperty('rate', rate-10)
    speak('Starting up...')

def listen():
    r = sr.Recognizer()
    r.dynamic_energy_threshold = True
    r.dynamic_energy_adjustment_ratio = 1.5
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source, timeout=30, phrase_time_limit=10)
        # audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(query)
        # If system is unable to understand what was said the query is None and the same is returned which causes
        # issue in the speak() function
        if query == None:
            raise Exception('Unable to understand what was said...')
        print(f"user Said : {query}\n")
        return query.lower()

    except Exception as e:
        print(e)
        speak("Say that again please")
        return listen()

def speak(text):
    print(f'Flair: {text}\n')
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    start_up()
    running()

