import subprocess


def execute_command(command):
    command = command.lower()

    if "open chrome" in command:
        print("Opening Chrome...")
        subprocess.Popen("start chrome", shell=True)
        return "Opening Chrome"

    else:
        return "Sorry, I don't know that command yet."