import pyttsx3 #pip install pyttsx3==2.71
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon Sir!")
    elif hour>=16 and hour<22:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    
    speak("I am Friday alpha one")
    strtime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {strtime}")
    speak("Please tell me how may i help you??")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said :{query}\n")
    except Exception as e:
        #print(e)

        print("Say that again please....")
        speak("Say that again please")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ruturajpatil782@gmail.com', 'bbkamaqbara')
    server.sendmail('ruturajpatil782@gmail.com', to, content)
    server.close()
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=10)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open hackerrank' in query:
            webbrowser.open("hackerrank.com")

        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[1]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open PYCharm' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3.3\\bin\\pycharm64.exe"
            os.startfile(codePath)
        elif 'open Chrome' in query:
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
        elif 'email' in query:
            try:
                speak("what shoud i say??")
                content = takeCommand()
                to = "ruturajpatil782@gmail.com"
                sendEmail(to, content)
                speak("email has been sent")
            except Exception as e:
                speak("sorry sir I am not able to sent email")
        elif 'exit' in query:
            speak("Have a nice day sir!!")
            exit()
#pip install pipwin
#pipwin install payAudio 
        