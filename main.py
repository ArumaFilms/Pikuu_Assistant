import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")
    elif hour>=12 and hour<18:
        talk("Good Afternoon!")
    else:
        talk("Good Evening!")

    talk("I am PIKU. Please tell me how may I help you!")

def take_command():
    with sr.Microphone() as source:
        print('listening...')
        listener.pause_threshold = 1
        voice = listener.listen(source)
    try:
        print("Recognizing...")
        command = listener.recognize_google(voice, language='en-in')
        command = command.lower()
        if 'piku' in command:
            command = command.replace('piku','')
        print(command)
    except Exception as e:
        print("Please say again..")
        return "None"
    return command


def run_piku():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        print('playing ' + song)
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'who created you' in command:
        talk('I am created by Ritish jain')
    elif 'about you' in command:
        talk('I am Artificial Assistant piku bulid by Ritish Jain.')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date with me' in command:
        talk('Yeah!! Sure.')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        j=pyjokes.get_joke()
        print(j)
        talk(j)
    elif 'open youtube' in command:
        talk("opening youtube!")
        webbrowser.open("youtube.com")
    elif 'open google' in command:
        talk("opening google")
        webbrowser.open("google.com")
    elif 'write a note' in command:
        file = open("speech.txt", 'w')
        talk("what do you want to write!")
        print("what do you want to write!")
        file.writelines(take_command())
        file.close()
    elif 'wikipedia' in command:
            talk('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            talk("According to Wikipedia")
            print(results)
            talk(results)
    else:
        talk('I dont understand, please repeat it again')

if __name__ == '__main__':
    wishMe()
    while True:
    # if 1:   #for one time
        run_piku()
