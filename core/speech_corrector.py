def correct_speech(text):
    text = text.lower().strip()

    corrections = {
        "vigma": "figma",
        "fire fox": "firefox",
        "visual studio coat": "visual studio code",
        "note pad": "notepad"
    }

    for wrong_word, correct_word in corrections.items():
        if wrong_word in text:
            print("Speech correction:", wrong_word, "->", correct_word)

            text = text.replace(
                wrong_word,
                correct_word
            )

    return text