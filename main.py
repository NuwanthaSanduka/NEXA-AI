import os
import difflib

from core.voice import speak
from core.recorder import record_audio
from core.transcriber import transcribe_audio
from core.commands import execute_command
from core.process_manager import close_window


# =========================
# CONFIRMATION HANDLER
# =========================
def get_confirmation(response):
    message = response["message"]

    print("Nexa:", message)
    speak(message)

    record_audio()

    confirmation_text = transcribe_audio("recording.wav")
    confirmation_text = confirmation_text.lower().strip()

    print("You said:", confirmation_text)

    yes_words = [
        "yes",
        "yeah",
        "yep",
        "correct",
        "sure",
        "confirm"
    ]

    no_words = [
        "no",
        "nope",
        "cancel"
    ]

    if any(word in confirmation_text for word in yes_words):
        return True

    if any(word in confirmation_text for word in no_words):
        return False

    return None


# =========================
# EXIT COMMAND DETECTION
# =========================
def is_exit_command(text):
    text = text.lower().strip()

    exit_phrases = [
        "stop assistant",
        "exit assistant",
        "close assistant",
        "quit assistant",
        "stop nexa",
        "exit nexa",
        "close nexa",
        "quit nexa"
    ]

    # Exact / partial match
    for phrase in exit_phrases:
        if phrase in text:
            print("Exit command detected:", text)
            return True

    # Fuzzy full-sentence match
    for phrase in exit_phrases:
        similarity = difflib.SequenceMatcher(
            None,
            text,
            phrase
        ).ratio()

        if similarity >= 0.65:
            print(
                "Exit command detected:",
                text,
                "| matched:",
                phrase,
                "| confidence:",
                round(similarity, 2)
            )
            return True

    # Fuzzy Nexa name detection
    words = text.split()

    action_words = [
        "exit",
        "stop",
        "quit",
        "close"
    ]

    has_exit_action = any(
        action in words
        for action in action_words
    )

    if has_exit_action:

        for word in words:

            similarity = difflib.SequenceMatcher(
                None,
                word,
                "nexa"
            ).ratio()

            if similarity >= 0.55:

                print(
                    "Exit command detected:",
                    text,
                    "| Nexa word:",
                    word,
                    "| confidence:",
                    round(similarity, 2)
                )

                return True

    return False


# =========================
# STARTUP
# =========================
print("====================================")
print("       Welcome to NEXA AI")
print("====================================")

print("System Starting...")
print("Developer : Nuwantha Sanduka")

speak(
    "Hello Nuwantha. "
    "I am Nexa. "
    "How can I help you today?"
)


# =========================
# CONTINUOUS LISTENING LOOP
# =========================
while True:

    record_audio()

    text = transcribe_audio("recording.wav")
    text = text.strip()

    print("You said:", text)

    # No speech detected
    if not text:
        print("Nexa: I could not hear anything.")
        continue

    lower_text = text.lower()


    # =========================
    # EXIT NEXA
    # =========================
    if is_exit_command(lower_text):

        final_response = "Okay. Goodbye."

        print("Nexa:", final_response)
        speak(final_response)

        break


    # =========================
    # EXECUTE COMMAND
    # =========================
    response = execute_command(text)


    # =========================
    # OPEN CONFIRMATION
    # =========================
    if (
        isinstance(response, dict)
        and response.get("type") == "confirmation"
    ):

        confirmation = get_confirmation(response)

        if confirmation is True:

            os.startfile(
                response["app_path"]
            )

            final_response = (
                "Opening "
                + response["app_name"]
            )

        elif confirmation is False:

            final_response = "Okay, cancelled"

        else:

            final_response = (
                "Sorry, I could not understand your answer"
            )

        print("Nexa:", final_response)
        speak(final_response)


    # =========================
    # CLOSE CONFIRMATION
    # =========================
    elif (
        isinstance(response, dict)
        and response.get("type") == "close_confirmation"
    ):

        confirmation = get_confirmation(response)

        if confirmation is True:

            success = close_window(
                response["window_title"]
            )

            if success:

                final_response = (
                    "Closing "
                    + response["window_title"]
                )

            else:

                final_response = (
                    "Sorry, I could not close that window"
                )

        elif confirmation is False:

            final_response = "Okay, cancelled"

        else:

            final_response = (
                "Sorry, I could not understand your answer"
            )

        print("Nexa:", final_response)
        speak(final_response)


    # =========================
    # NORMAL RESPONSE
    # =========================
    else:

        print("Nexa:", response)
        speak(response)