import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests
import os
from openai import OpenAI

# ===================== CONFIG =====================
WAKE_WORD = "pragya"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"        # move to env later
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"    # move to env later

# ===================== INIT =======================
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# ---- Female voice setup ----
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)   # usually female on Windows
engine.setProperty("rate", 175)
engine.setProperty("volume", 1.0)

# ===================== SPEAK ======================
def speak(text):
    engine.say(text)
    engine.runAndWait()

# ===================== AI =========================
def aiProcess(command):
    client = OpenAI(api_key=OPENAI_API_KEY)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are Pragya, a smart Indian virtual assistant. Keep replies short and clear."
            },
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

# ===================== COMMANDS ===================
def processCommand(command):
    command = command.lower()

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")

    elif command.startswith("play"):
        song = command.split(" ", 1)[1]
        link = music_library.music.get(song)
        if link:
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak("Sorry, I could not find that song")

    elif "news" in command:
        speak("Here are the latest headlines")
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
        )
        if r.status_code == 200:
            articles = r.json().get("articles", [])
            for article in articles[:5]:
                speak(article["title"])
        else:
            speak("Unable to fetch news right now")

    else:
        response = aiProcess(command)
        speak(response)

# ===================== MAIN LOOP ==================
if __name__ == "__main__":
    speak("Initializing Pragya")

    while True:
        try:
            print("Listening for wake word...")

            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

            word = recognizer.recognize_google(audio)
            print("Heard:", word)

            if "pragya" in word.lower():
                speak("Yes")   # ✅ mic is CLOSED now
                print("Pragya active")

                with sr.Microphone() as source:
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)

                command = recognizer.recognize_google(audio)
                print("Command:", command)
                processCommand(command)

        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            print("Could not understand")
        except Exception as e:
            print("Error:", e)