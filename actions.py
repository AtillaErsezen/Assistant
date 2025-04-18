import os

def perform_action(intent):
    if intent == 'open_notepad':
        os.system('notepad')  # Or any other command on Linux/Mac
        return "Opening Notepad..."
    elif intent == 'greet':
        return "Hello! How can I help you?"
    elif intent == 'goodbye':
        return "Goodbye! Have a great day!"
    elif intent == 'open_outlook':
        os.system('start brave "https://outlook.office.com/mail/20d326cc.8dd3.4dfb.8921.48f2b0c00eff@vunl.mail.onmicrosoft.com/"')
        return "Opening school email"
    elif intent == 'open_gmail':
        os.system('start brave "https://mail.google.com/mail/u/0/#inbox"')
        return "Opening Gmail"
    elif intent == 'open_notion':
        os.system(r'start "" "C:\Users\ersez\AppData\Local\Programs\Notion\Notion.exe"')
        return "Opening Notion"
    elif intent == 'open_spotify':
        os.system('start brave "https://open.spotify.com/"')
        return "Opening Spotify"
    elif intent == 'open_chatgpt':
        os.system('start brave "https://chat.openai.com/"')
        return "Opening ChatGPT"
    #Doesn't work
    elif intent == 'open_whatsapp':
        os.system(r'start "" "C:\Users\ersez\AppData\Local\WhatsApp\WhatsApp.exe"')
        return "Opening WhatsApp"
    else:
        return "Sorry, I don't understand that yet."
