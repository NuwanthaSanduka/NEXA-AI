import subprocess
import webbrowser


def execute_command(command):
    command = command.lower().strip()

    chrome_commands = [
        "open chrome",
        "chrome open",
        "launch chrome",
        "start chrome",
        "open google chrome"
    ]

    notepad_commands = [
        "open notepad",
        "notepad open",
        "launch notepad",
        "start notepad"
    ]

    calculator_commands = [
        "open calculator",
        "calculator open",
        "launch calculator",
        "start calculator",
        "open calc"
    ]

    youtube_commands = [
        "open youtube",
        "youtube open",
        "launch youtube",
        "start youtube"
    ]

    if any(phrase in command for phrase in chrome_commands):
        print("Opening Chrome...")
        subprocess.Popen("start chrome", shell=True)
        return "Opening Chrome"

    elif any(phrase in command for phrase in notepad_commands):
        print("Opening Notepad...")
        subprocess.Popen("notepad.exe")
        return "Opening Notepad"

    elif any(phrase in command for phrase in calculator_commands):
        print("Opening Calculator...")
        subprocess.Popen("calc.exe")
        return "Opening Calculator"

    elif any(phrase in command for phrase in youtube_commands):
        print("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    else:
        return "Sorry, I don't know that command yet."