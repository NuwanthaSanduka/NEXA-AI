from core.voice import speak
from core.recorder import record_audio
from core.transcriber import transcribe_audio

print("====================================")
print("       Welcome to NEXA AI")
print("====================================")

print("System Starting...")
print("Developer : Nuwantha Sanduka")

speak("Hello Nuwantha. I am Nexa. How can I help you today?")

record_audio()

text = transcribe_audio("recording.wav")

print("You said:", text)

speak("I heard " + text)