import subprocess
import webbrowser


def execute_command(command):
    command = command.lower().strip()

    if "open chrome" in command:
        print("Opening Chrome...")
        subprocess.Popen("start chrome", shell=True)
        return "Opening Chrome"

    elif "open notepad" in command:
        print("Opening Notepad...")
        subprocess.Popen("notepad.exe")
        return "Opening Notepad"

    elif "open calculator" in command:
        print("Opening Calculator...")
        subprocess.Popen("calc.exe")
        return "Opening Calculator"

    elif "open youtube" in command:
        print("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    else:
        return "Sorry, I don't know that command yet."