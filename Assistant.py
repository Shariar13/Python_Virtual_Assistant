import pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty("rate", 172)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak('Hey. Who are you?')

       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

wishMe()
while True:
    speak('Please tell me your security code.')
    query = takeCommand().lower()
    if '99' not in query:
        speak('Sorry I dont know you.')
        
    else:
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning sir. Welcome Back. I am Tina your personal assistant. How may i help you?")      

        elif hour>=12 and hour<18:
            speak("Good Afternoon sir. Welcome Back. I am Tina your personal assistant. How may i help you?")   

        else:
            speak("Good Evening sir. Welcome Back. I am Tina your personal assistant. How may i help you?") 
        

        def sendEmail(to, content):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('shariarkabir13@gmail.com', '01986292330sk')
            server.sendmail('shariarkabir13@gmail.com', to, content)
            server.close()

        if __name__ == "__main__":
            while True:
            # if 1:
                query = takeCommand().lower()

                # Logic for executing tasks based on query
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'youtube' in query:
                    speak('Here is your youtube sir.')
                    webbrowser.open("https://youtube.com")

                elif 'name' in query:
                    speak('My name is Tina.')

                elif 'creator' in query:
                    speak('My boss Shariar Kabir.')

                elif 'song' in query:
                    speak('Sorry sir at this moment i cant sing song without my boss permisson.')

                elif 'love' in query:
                    speak('In the world i love only one person & that is my boss Shariar Kabir.')

                elif 'type' in query:
                    speak('Okay sir. Here is your note pad. ')
                    codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
                    os.startfile(codePath)

                elif 'note' in query:
                    speak('Okay sir. Here is your note pad. ')
                    codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
                    os.startfile(codePath)

                elif 'stop' in query:
                    os.system('taskkill /im firefox.exe /f')

                elif 'video' in query:
                    speak('Which video should i play sir?')
                    query = takeCommand().lower()
                    webbrowser.open("https://www.youtube.com/results?search_query=" + query)

                elif 'google' in query:
                    speak('Here is your google sir.')
                    webbrowser.open("https://google.com")

                elif 'bye' in query:
                    speak('Bye sir. I am always ready for your service.')
                    sys.exit()


                elif 'search' in query:
                    speak('What thing i search for?')
                    query = takeCommand().lower()
                    try:
                        from googlesearch import search
                    except ImportError:
                        print("No module named 'google' found") 
                    for j in search(query, tld="co.in", num=2, stop=2, pause=2):
                        webbrowser.open(j)

                elif 'stack overflow' in query:
                    speak('Here is your stack overflow sir.')
                    webbrowser.open("https://stackoverflow.com") 
                

                elif 'music' in query:
                    music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                    songs = os.listdir(music_dir)
                    print(songs)    
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif 'time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")

                elif 'compiler' in query:
                    speak('Here is your favorite & most use compiler vs code sir.')
                    codePath = "C:\\Users\\shari\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)

                elif 'email' in query:
                    try:
                        speak("sir What should I say?")
                        content = takeCommand()
                        speak("okay sir Who is the receiver?")
                        to =  input()   
                        sendEmail(to, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("Sorry sir I am not able to sent this email.")    

                else:
                    speak('Sorry sir. Can you please tell me again?')
