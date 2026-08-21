import os

from core.voice import speak
from core.recorder import record_audio
from core.transcriber import transcribe_audio
from core.commands import execute_command
from core.process_manager import close_window


print("====================================")
print("       Welcome to NEXA AI")
print("====================================")

print("System Starting...")
print("Developer : Nuwantha Sanduka")

speak("Hello Nuwantha. I am Nexa. How can I help you today?")

record_audio()

text = transcribe_audio("recording.wav")

print("You said:", text)

response = execute_command(text)


# =========================
# OPEN CONFIRMATION
# =========================
if isinstance(response, dict) and response.get("type") == "confirmation":

    message = response["message"]

    print("Nexa:", message)
    speak(message)

    record_audio()

    confirmation_text = transcribe_audio("recording.wav")
    confirmation_text = confirmation_text.lower().strip()

    print("You said:", confirmation_text)

    yes_words = ["yes", "yeah", "yep", "correct", "sure"]
    no_words = ["no", "nope", "cancel"]

    if any(word in confirmation_text for word in yes_words):

        os.startfile(response["app_path"])

        final_response = "Opening " + response["app_name"]

        print("Nexa:", final_response)
        speak(final_response)

    elif any(word in confirmation_text for word in no_words):

        final_response = "Okay, cancelled"

        print("Nexa:", final_response)
        speak(final_response)

    else:

        final_response = "Sorry, I could not understand your answer"

        print("Nexa:", final_response)
        speak(final_response)


# =========================
# CLOSE CONFIRMATION
# =========================
elif isinstance(response, dict) and response.get("type") == "close_confirmation":

    message = response["message"]

    print("Nexa:", message)
    speak(message)

    record_audio()

    confirmation_text = transcribe_audio("recording.wav")
    confirmation_text = confirmation_text.lower().strip()

    print("You said:", confirmation_text)

    yes_words = ["yes", "yeah", "yep", "correct", "sure"]
    no_words = ["no", "nope", "cancel"]

    if any(word in confirmation_text for word in yes_words):

        if close_window(response["window_title"]):

            final_response = "Closing " + response["window_title"]

        else:
            final_response = "Sorry, I could not close that window"

        print("Nexa:", final_response)
        speak(final_response)

    elif any(word in confirmation_text for word in no_words):

        final_response = "Okay, cancelled"

        print("Nexa:", final_response)
        speak(final_response)

    else:

        final_response = "Sorry, I could not understand your answer"

        print("Nexa:", final_response)
        speak(final_response)


# =========================
# NORMAL RESPONSE
# =========================
else:
    print("Nexa:", response)
    speak(response)