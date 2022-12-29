import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
print(engine)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()
    
    
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'wizzy' in command:
                command = command.replace('wizzy', '')
                print(command)
        return command
    except:
        pass
 
    
    
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + time)
        print(time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'tell me joke' in command:
        talk(pyjokes.get_joke())
    elif 'hello' in command:
        talk('Hi! I am wizzy Rohits talk assistant how may I help you')
    elif 'how are you doing' in command:
        talk('I am doing good! Thanks for asking!')
    elif 'bitch' in command:
        talk('Hey! please talk good to me I am not your whore!')
    elif 'honey' in command:
        talk('Love you too honey muuuuuuuhaaaaaaah! Thanks for love!')
    elif 'bye' in command:
        quit
    else:
        talk('Please say the command again.')
        

while True:
    run_alexa()