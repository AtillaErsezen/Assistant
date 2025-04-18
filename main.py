import speech_recognition as sr
import pyttsx3
from classifier import IntentClassifier
from actions import perform_action

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen_for_wake_word(wake_word="hey assistant"):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("👂 Waiting for wake word...")

    while True:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        try:
            transcript = recognizer.recognize_google(audio).lower()
            print("Heard:", transcript)
            if wake_word in transcript:
                print("✅ Wake word detected!")
                speak("Yes?")
                return  # Exit to main loop
        except sr.UnknownValueError:
            continue
        except sr.RequestError:
            print("⚠️ Speech recognition error.")
            continue

def listen_command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio).lower()
    except:
        return ""

def main():
    clf = IntentClassifier()
    try:
        clf.load()
    except:
        clf.train()
        clf.save()

    speak("Voice assistant is ready.")

    while True:
        listen_for_wake_word()

        print("🎤 Listening for command...")
        user_input = listen_command()
        if not user_input:
            speak("Sorry, I didn't catch that.")
            continue

        if "exit" in user_input:
            speak("Goodbye!")
            break

        intent = clf.predict(user_input)
        response = perform_action(intent)
        print("🤖", response)
        speak(response)

if __name__ == "__main__":
    main()
