import speech_recognition as sr
import pyttsx3 as p
import webbrowser
import datetime

engine = p.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)

def say(text):
    engine.say(text)
    engine.runAndWait()

def recognize_language(language_code):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language=language_code)
        print(f"User said: {query}")
        return query
    except Exception as e:
        print(f"Error: {str(e)}")
        return "कुछ गड़बड़ हो गई है, कृपया फिर से भाषा चुनें"

if __name__ == '__main__':
    print("\n******************************************")
    print(" Bajrangi the assistant, Welcomes you !!! ")
    
    print("******************************************")
    say("Hello Everyone, Bajrangi this Side. How may I help you?")
    print("Choose the language in which you want to take Services")
    say("Choose the language in which you want to take Services")
    
    while True:
        print("Listening...")
        print("English, Hindi, Punjabi, Tamil or Gujarati")
        say("English, Hindi, Punjabi, Tamil or Gujarati")
        
        query = recognize_language("en-IN")
        say(query)
        
        if "stop" in query.lower():
            say("Goodbye!")
            break
        
        if "english" in query.lower():
            print("Bajrangi is Listening you please speak loud....")
            query = recognize_language("en-IN")
            say(query)
            if "stop" in query.lower():
                say("Goodbye!")
                break
            say("You can also ask me to open sites like YouTube, Google, Wikipedia, tell the time, or search on YouTube or Google")
            print("In English, you can also ask me to open sites like YouTube, Google, Wikipedia, tell the time, or search on YouTube or Google")
            
            sites = {
                "youtube": "https://www.youtube.com",
                "wikipedia": "https://www.wikipedia.com",
                "google": "https://www.google.com",
                "github": "https://github.com/ShauryaBhardwaj112",
                "leetcode": "https://leetcode.com/problemset/all/"
            }
            
            if "search on youtube" in query.lower():
                say("What do you want to search for on YouTube?")
                search_query = recognize_language("en-IN")
                if "stop" in search_query.lower():
                    say("Goodbye!")
                    break
                say(f"Searching for {search_query} on YouTube")
                webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
            elif "search on google" in query.lower():
                say("What do you want to search for on Google?")
                search_query = recognize_language("en-IN")
                if "stop" in search_query.lower():
                    say("Goodbye!")
                    break
                say(f"Searching for {search_query} on Google")
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
            else:
                for site, url in sites.items():
                    if f"open {site}".lower() in query.lower():
                        say(f"Opening {site} sir...")
                        webbrowser.open(url)
                        break  # Break to avoid multiple openings
                
                if "tell the time" in query.lower():
                    current_time = datetime.datetime.now().strftime("%H:%M:%S")
                    say(f"Sir, the time is {current_time}")
        
        elif "hindi" in query.lower():
            print("Bajrangi आपकी मदद करने के लिए तैयार है, कृपया बोलें...")
            say("आप मुझसे यूट्यूब, गूगल, विकिपीडिया खोलने, समय बताने, या यूट्यूब पर कुछ खोजने के लिए कह सकते हैं")
            print("आप मुझसे यूट्यूब, गूगल, विकिपीडिया खोलने, समय बताने, या यूट्यूब पर कुछ खोजने के लिए कह सकते हैं")
            
            query = recognize_language("hi-IN")
            say(query)
            if "बंद करो" in query:
                say("अलविदा!")
                break
            
            sites = {
                "youtube": "https://www.youtube.com",
                "wikipedia": "https://www.wikipedia.com",
                "google": "https://www.google.com",
                "github": "https://github.com/ShauryaBhardwaj112",
                "leetcode": "https://leetcode.com/problemset/all/"
            }
            
            if "यूट्यूब पर खोजें" in query:
                say("यूट्यूब पर क्या खोजना चाहते हैं?")
                search_query = recognize_language("hi-IN")
                if "बंद करो" in search_query:
                    say("अलविदा!")
                    break
                say(f"यूट्यूब पर {search_query} खोज रहे हैं")
                webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
            elif "गूगल पर खोजें" in query:
                say("गूगल पर क्या खोजना चाहते हैं?")
                search_query = recognize_language("hi-IN")
                if "बंद करो" in search_query:
                    say("अलविदा!")
                    break
                say(f"गूगल पर {search_query} खोज रहे हैं")
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
            else:
                for site, url in sites.items():
                    if f"{site} खोलो" in query:
                        say(f"{site} खोल रहा हूँ...")
                        webbrowser.open(url)
                        break  # Break to avoid multiple openings
                
                if "समय बताओ" in query:
                    current_time = datetime.datetime.now().strftime("%H:%M:%S")
                    say(f"सर, समय है {current_time}")
        
        elif any(lang in query.lower() for lang in ["punjabi", "tamil", "gujarati"]):
            language_dict = {
                "punjabi": "pa-IN",
                "tamil": "ta-IN",
                "gujarati": "gu-IN"
            }
            
            for lang, lang_code in language_dict.items():
                if lang in query.lower():
                    print(f"Listening in {lang.capitalize()}...")
                    query = recognize_language(lang_code)
                    if "stop" in query.lower():
                        say("Goodbye!")
                        
                        break
                    
                    say(query) 
                    print("Goodbye!!!!!")
                    break
