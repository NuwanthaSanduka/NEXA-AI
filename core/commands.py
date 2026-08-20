import subprocess
import webbrowser


def execute_command(command):
    command = command.lower().strip()

    open_words = ["open", "launch", "start"]

    if any(word in command for word in open_words):

        if "chrome" in command:
            print("Opening Chrome...")
            subprocess.Popen("start chrome", shell=True)
            return "Opening Chrome"

        elif "notepad" in command:
            print("Opening Notepad...")
            subprocess.Popen("notepad.exe")
            return "Opening Notepad"

        elif "calculator" in command or "calc" in command:
            print("Opening Calculator...")
            subprocess.Popen("calc.exe")
            return "Opening Calculator"

        elif "youtube" in command:
            print("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")
            return "Opening YouTube"

    return "Sorry, I don't know that command yet."