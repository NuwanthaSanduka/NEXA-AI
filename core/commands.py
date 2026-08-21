import os
import webbrowser
import string

from core.app_scanner import find_app
from core.process_manager import close_app


def execute_command(command):
    command = command.lower().strip()

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

    # OPEN APP
    if any(word in cleaned_command for word in open_words):

        if "youtube" in cleaned_command:
            print("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")
            return "Opening YouTube"

        app_name = cleaned_command

        for word in open_words:
            app_name = app_name.replace(word, "")

        app_name = app_name.strip()

        app_path = find_app(app_name)

        if app_path:
            print("Opening", app_name)
            os.startfile(app_path)
            return "Opening " + app_name

        return "I could not find " + app_name

    # CLOSE APP
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