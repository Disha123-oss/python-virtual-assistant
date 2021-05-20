import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import time
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def jarvisvoice(audioinput):
    engine.say(audioinput)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        jarvisvoice("i am listening to you!...")
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print("Query : ",query)
    except Exception  as e:
        jarvisvoice("could you say that again please... I did'nt hear you")
        r.pause_threshold=1
        takecommand()
        print(e)
        return "None"
    return query

def wish():
    h=int(datetime.datetime.now().hour)
    if h>=1 and h<12:
        jarvisvoice("Good Morning swagata")
        jarvisvoice("what u want me to do?")
    elif h>=12 and h<18:
        jarvisvoice("Good Afternoon swagata")
    else:
        jarvisvoice("Good Evening swagata")

wish()

def youtubesearch(term):
    result="https://www.youtube.com/results?search_query=" + term
    pywhatkit.playonyt(result)
    jarvisvoice("okay! this is what i got for u maam!")

while True:
    query=takecommand().lower()
    if "music please" in query:
        songs_dir="D:\\music"
        songs=os.listdir(songs_dir)
        os.startfile(os.path.join(songs_dir,songs[1]))
    elif "exit" in query:
        exit()
    elif "what is" in query or "who is" in query:
        jarvisvoice("searching in wikipedia... please wait...")
        query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        jarvisvoice("according to wikipedia...")
        print(results)
        jarvisvoice(results)
    elif "i want a movie review" in query:
        jarvisvoice("which movie review do you want?")
        mov = takecommand()
        res = "https://www.google.com/search?q="+mov+"+movie+review"
        webbrowser.open_new_tab(res)
    elif "say hello to" in query:
        jarvisvoice("hello! nice to know you...")
    elif "open google" in query:
        webbrowser.open_new_tab("google.com")
    elif "open gmail" in query:
        webbrowser.open_new_tab("gmail.com")
    elif "open youtube" in query:
        webbrowser.open_new_tab("youtube.com")
    elif "open facebook" in query:
        webbrowser.open_new_tab("facebook.com")
    elif "don't listen" in query or "stop listening" in query:
            jarvisvoice("for how much time you want to stop jarvis from listening commands")
            a = int(takecommand())
            time.sleep(a)
            jarvisvoice("okay! i am ready to listen to you!...")

    elif "play " in query:
        youtubesearch(query)
    else:
        jarvisvoice("searching in wikipedia... please wait...")
        query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        jarvisvoice("according to wikipedia...")
        print(results)
        jarvisvoice(results)
