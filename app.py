from openai import OpenAI  # pip install openai
from api_key import api_data  # Importing the api key from api_key.py file
import os # To interact with the operating system # pip install os-system
import speech_recognition as sr # Converts my voice commands to text 
import pyttsx3 # Read out text output to voice. # pip install pyttsx3
import webbrowser # To open web browser # pip install pyttsx3
# from googlesearch import search # To search on google # pip install google
Model = "gpt-4o" # Model used
# Model = "gpt-3.5-turbo" # Model used
client = OpenAI(api_key=api_data) # Passing the api key to the client

def Reply(question): # Function to get the response from the model
    completion = client.chat.completions.create(
        model=Model,
        messages=[
            {'role':"system","content":'You are a helful assistant'},
            {'role':'user','content':question}
        ], 
        max_tokens=200 # Limiting the response length to 200 tokens
    )
    answer = completion.choices[0].message.content # Extracting the response
    return answer # Returning the response
#example usage
# question = "What is the weather like today?"
# answ = Reply(question)
# print(answ)
engine = pyttsx3.init('sapi5') # Using the sapi5 voice engine
# print(engine.getProperty('voices')) # To get the available voices
voices = engine.getProperty('voices') # Getting the available voices
# print(voices
engine.setProperty('voice', voices[0].id) # Setting the voice to the first voice in the list
engine.setProperty('rate', 150) # Setting the speech rate

def speak(text): # Function to convert text to speech
    engine.say(text) # Passing the text to be spoken
    engine.runAndWait() # Running the speech engine
    
speak("Hello shanmukha sri vyshnav what can i do for you today?") # Greeting message

def takeCommand(): # Function to take voice commands from the user
    
    r = sr.Recognizer() # Initializing the recognizer
    with sr.Microphone() as source:  # Using the microphone as source
        print('Listening .......') # Indicating that the assistant is listening
        r.pause_threshold = 1 # Wait for 1 sec before considering the end of a phrase
        audio = r.listen(source) # Listening to the source
    try: 
        print('Recogninzing ....') # Indicating that the assistant is recognizing the voice
        query = r.recognize_google(audio, language = 'en-in') # Using google to recognize the voice
        print("User Said: {} \n".format(query)) # Printing what the user said
    except Exception as e: # If the voice is not recognized
        # print(e) # Printing the error
        print("Say that again .....") # Asking the user to say again
        return "None" # Returning none if the voice is not recognized
    return query # Returning the recognized voice as text

if __name__ == '__main__': # Main function
    while True:  # Infinite loop to keep the assistant running
        query = takeCommand().lower() # Taking the command and converting it to lower case
        if query == 'none': # If the command is none
            continue # Continue to the next iteration
        # Logic for executing tasks based on query
        
        ans = Reply(query) # Getting the response from the model
        print(ans) # Printing the response
        speak(ans) # Speaking the response
        
        # Specific Browser Related Tasks 
        if "Open youtube" in query:    
            webbrowser.open('www.youtube.com')
        if "Open Google" in query: 
            webbrowser.open('www.google.com')
        if "bye" in query:
            speak("Goodbye shanmukha sri vyshnav, have a great day!")
        #continue to add more commands here want to add browser related tasks
            break 