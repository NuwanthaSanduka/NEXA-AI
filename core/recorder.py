import os
import sounddevice as sd 
from scipy.io.wavfile import write

SAMPLE_RATE = 16000
DURATION = 5

def record_audio():

    filename = "recording.wav"
    folder = "assets/rec"
    print("Recording... Speak now!")

    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write(filename, SAMPLE_RATE, audio)

    print("Recording saved as", filename)