import difflib
import re
import pygetwindow as gw


def close_app(app_name):
    app_name = app_name.lower().strip()

    windows = gw.getAllWindows()

    # 1. Direct match
    for window in windows:
        title = window.title.lower().strip()

        if title and app_name in title:
            print("Closing:", window.title)

            try:
                window.close()
                return True

            except Exception as error:
                print("Could not close window:", error)
                return False

    # 2. Fuzzy match
    for window in windows:
        title = window.title.lower().strip()

        if not title:
            continue

        # Example:
        # "Untitled - Figma" -> ["untitled", "figma"]
        title_parts = re.split(r"[-|–—:]", title)

        for part in title_parts:
            part = part.strip()

            similarity = difflib.SequenceMatcher(
                None,
                app_name,
                part
            ).ratio()

            if similarity >= 0.6:
                print("Matched:", app_name, "->", part)
                print("Closing:", window.title)

                try:
                    window.close()
                    return True

                except Exception as error:
                    print("Could not close window:", error)
                    return False

    return False