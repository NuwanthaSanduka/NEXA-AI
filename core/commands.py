import os
import webbrowser
import string

from core.process_manager import close_app
from core.speech_corrector import correct_speech
from core.app_matcher import match_app


def execute_command(command):
    command = command.lower().strip()

    # Correct common speech recognition mistakes
    command = correct_speech(command)

    # Remove punctuation from speech transcription
    command = command.translate(
        str.maketrans("", "", string.punctuation)
    )

    open_words = ["open", "launch", "start"]
    close_words = ["close", "exit", "quit"]

    filler_words = [
        "please",
        "can you",
        "could you",
        "would you",
        "for me"
    ]

    # Remove unnecessary natural-language words
    cleaned_command = command

    for phrase in filler_words:
        cleaned_command = cleaned_command.replace(phrase, "")

    cleaned_command = cleaned_command.strip()

    # =========================
    # OPEN APP
    # =========================
    if any(word in cleaned_command for word in open_words):

        if "youtube" in cleaned_command:
            print("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")
            return "Opening YouTube"

        app_name = cleaned_command

        for word in open_words:
            app_name = app_name.replace(word, "")

        app_name = app_name.strip()

        # Dynamic app matching
        match = match_app(app_name)

        if match:
            matched_name, app_path, confidence = match

            # High confidence
            if confidence >= 0.65:
                print("Opening", matched_name)
                os.startfile(app_path)
                return "Opening " + matched_name

            # Low confidence
            print(
                "Low confidence match:",
                 app_name,
                 "->",
                matched_name
            )

            return {
                "type": "confirmation",
                "message": "Did you mean " + matched_name + "?",
                "app_name": matched_name,
                "app_path": app_path
            }

            return "Did you mean " + matched_name + "?"

        return "I could not find " + app_name

    # =========================
    # CLOSE APP
    # =========================
    if any(word in cleaned_command for word in close_words):

        app_name = cleaned_command

        for word in close_words:
            app_name = app_name.replace(word, "")

        app_name = app_name.strip()

        if close_app(app_name):
            print("Closing", app_name)
            return "Closing " + app_name

        return "I could not find an open window for " + app_name

    return "Sorry, I don't know that command yet."