import os
import webbrowser

from core.app_scanner import find_app


def execute_command(command):
    command = command.lower().strip()

    open_words = ["open", "launch", "start"]

    if any(word in command for word in open_words):

        if "youtube" in command:
            print("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")
            return "Opening YouTube"

        app_name = command

        for word in open_words:
            app_name = app_name.replace(word, "")

        app_name = app_name.strip()

        app_path = find_app(app_name)

        if app_path:
            print("Opening", app_name)
            os.startfile(app_path)
            return "Opening " + app_name

        return "I could not find " + app_name

    return "Sorry, I don't know that command yet."