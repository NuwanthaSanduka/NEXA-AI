import difflib
import re
import pygetwindow as gw


def match_window(app_name):
    app_name = app_name.lower().strip()

    windows = gw.getAllWindows()

    best_window_title = None
    best_score = 0.0

    for window in windows:
        title = window.title.strip()

        if not title:
            continue

        lower_title = title.lower()

        # 1. Direct / partial match
        if app_name in lower_title:
            print(
                "Direct window match:",
                app_name,
                "->",
                title,
                "| confidence: 1.0"
            )

            return title, 1.0

        # Split title:
        # "Untitled - Figma" -> ["untitled", "figma"]
        title_parts = re.split(r"[-|–—:]", lower_title)

        for part in title_parts:
            part = part.strip()

            if not part:
                continue

            score = difflib.SequenceMatcher(
                None,
                app_name,
                part
            ).ratio()

            if score > best_score:
                best_score = score
                best_window_title = title

    # Return best fuzzy match
    if best_window_title:
        print(
            "Fuzzy window match:",
            app_name,
            "->",
            best_window_title,
            "| confidence:",
            round(best_score, 2)
        )

        return best_window_title, best_score

    return None


def close_window(window_title):
    windows = gw.getAllWindows()

    for window in windows:
        if window.title == window_title:

            print("Closing:", window.title)

            try:
                window.close()
                return True

            except Exception as error:
                print("Could not close window:", error)
                return False

    return False