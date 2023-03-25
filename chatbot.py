import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
from  pyfiglet import Figlet
import creds 
import openai
import speedtest



openai.api_key = creds.openai_api_key

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)
webbrowser.register('chrome' , None , webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))



figlet = Figlet()
fonts = figlet.getFonts()
figlet.setFont(font='big')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def greet():
    hour = int(datetime.datetime.now().hour)
    if morning(hour):
        speak('Good Morning')
    elif afternoon(hour):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
        
    speak("I am Echo , Your Personal Intelligent Assistant")    
    speak("How may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language='en-in' , show_all=True )
        query = query['alternative']
        query = query[0]
        query = query['transcript']
        
        print(f"User said : {query}\n")
    
    except Exception as e:
        #print(e)
        print("Say that again Please")
        return "None"

    
    return query

def valid_search(search):
    if search:
        return True
    else:
        return False
    
def morning(hour):
    if 0 <= hour < 12:
        return True
    else:
        return False

def afternoon(hour):
    if 12 <= hour < 18:
        return True
    
    else:
        return False



if __name__ == "__main__":
    print(figlet.renderText("Echo AI"))
    greet()
    while True:
    
        query = takeCommand().lower()
    
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia" , "")
            search = wikipedia.search(query , results = 1 , suggestion = False)
            results = wikipedia.summary(search , sentences = 2 , auto_suggest = False , redirect = True)
            speak("According to Wikipedia , ")
            print(f"According to Wikipedia : {results}")
            speak(results)
            
        elif 'open' in query:
            if 'google' in query:
                webbrowser.get('chrome').open("google.com")
            
                
            elif 'stack overflow' in query:
                webbrowser.get('chrome').open("stackoverflow.com")
            
            elif 'code' in query or 'vs code' in query:
                codePath = "C:\\Users\\Com\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            
            elif 'sublime' in query or 'sublime text' in query:
                codePath ="C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
                os.startfile(codePath)
                
            else:
                query = query.replace("open" , "")
                speak("Do you want me to open it in Web Browser")
                new_query = takeCommand()
                
                if "yes" in new_query:
                    webbrowser.get('chrome').open("google.com/search?q=" + query)
                
                else:
                    speak("I cant perform that task as of now , I am Sorry")
                    
            
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f" Sir, the time is {strTime}")
            
        elif 'youtube' in query:
            query = query.replace("youtube" , "")
            #speak("what should i search for")
            #search=takeCommand()
            if valid_search(query):
                pywhatkit.playonyt(query)
            else:
                speak("Invalid Search")
            
                
        elif 'chat gpt' in query or 'chat' in query:
            speak("What should i look up")
            prompt = takeCommand()
            if prompt == 'exit':
                break
            else:
                response=openai.Completion.create(engine='text-davinci-003' , prompt=prompt , max_tokens=200) 
                result = response['choices'][0]["text"]
                print(f"Result: {result}")
                
        elif 'internet' in query or 'speed' in query:
            
            st = speedtest.Speedtest()
            d1 = st.download()
            d1 = d1*0.000000125
            u1 = st.upload()
            u1 = u1*0.000000125
            print(f"Sir , your download speed is {d1:.2f} mega bytes per second and your upload speed is {u1:.2f} mega bytes per second ")
            speak(f"Sir , your download speed is {d1:.2f} mega bytes per second and your upload speed is {u1:.2f} mega bytes per second ")
                
                
        elif 'exit' in query or 'quit' in query:
            speak(" Thank You ")
            break
            
        
            
        
