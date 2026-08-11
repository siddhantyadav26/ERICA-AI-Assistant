
# E.R.I.C.A. – Enhanced Responsive Intelligent Computing Assistant

import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia as wk

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 550
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
        return query.lower()  

    except Exception as e:
        print("Say that again Please...")
        return "none"

if __name__ == "__main__":
    print("ERICA")
    speak("     Hello I amm  EERICA  an Artificial Intelligence devloped by Sir  Sidddhhaant  Yaadav")
    while True:
        query = takecommand()
        
        happy_jj = ["very good", "nice", "well done", "good", "great", "excellent", "wonderful", "perfect", "amazing"]
        nice_jj = False
        
        for jj in happy_jj:
            if jj in query:
                nice_jj = True
                break
        
        if nice_jj:
            speak("Thank you, sir.")
        
        question_keywords = ["what", "who", "where","about" ,"when", "why", "how", "can you tell me about", "tell me more about"]
        found_keyword = False
        
        for keyword in question_keywords:
            if keyword in query:
                found_keyword = True
                break
                
        if found_keyword:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', "")
            results = wk.summary(query, sentences=1)
            speak("According to Wikipedia")
            print("According to Wikipedia")
            print(results)
            speak(results) 
            
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
             
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        
        elif 'open chatgpt' in query:
            webbrowser.open("https://www.chatgpt.com/")    
             
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")    
             
        elif 'open amazon' in query:
            webbrowser.open("https://www.amazon.in/?tag=topca0b-21&ascsubtag=3477124x105530760")
             
        elif 'open spotify' in query:
            webbrowser.open("https://open.spotify.com/download")
             
        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com/")
        
        elif 'open wikipedia' in query:
            webbrowser.open("https://www.wikipedia.org/")
        