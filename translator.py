from speak_module import speak
from datetime import datetime

# Start with English language by default
current_lang = 'en'

# Language map for English, Hindi, and Marathi
lang_map = {
    "english": "en",
    "hindi": "hi",
    "marathi": "mr"
}

# Main assistant loop
def translateNow():
    while True:
        user_input = input("You: ").lower()

        # Language switch command
        if "set language to" in user_input:
            for lang_name in lang_map:
                if lang_name in user_input:
                    current_lang = lang_map[lang_name]
                    speak(f"Language set to {lang_name}", lang=current_lang)
                    break
            else:
                speak("Sorry, I only support English, Hindi, and Marathi.", lang=current_lang)

        # Time response command
        elif "time" in user_input:
            now = datetime.now()
            time_str = now.strftime('%I:%M %p')

            # Provide the time in the selected language
            if current_lang == 'hi':
                speak(f"वर्तमान समय {time_str} है", lang='hi')  # Hindi
            elif current_lang == 'mr':
                speak(f"आत्ता वेळ {time_str} आहे", lang='mr')  # Marathi
            else:
                speak(f"The current time is {time_str}", lang='en')  # English

        # Exit command
        elif user_input in ["exit", "quit"]:
            speak("Goodbye!", lang=current_lang)
            break

        else:
            speak("Sorry, I didn't understand that.", lang=current_lang)

