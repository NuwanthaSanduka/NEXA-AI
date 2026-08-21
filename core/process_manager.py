import difflib
import re
import pygetwindow as gw


def match_window(app_name):
    app_name = app_name.lower().strip()

    # Very short names are too risky for direct matching
    if len(app_name) < 3:
        print(
            "Window match rejected:",
            app_name,
            "| reason: command too short"
        )
        return None

    windows = gw.getAllWindows()

    best_window_title = None
    best_score = 0.0

    for window in windows:
        title = window.title.strip()

        if not title:
            continue

        lower_title = title.lower()

        # Split title into meaningful parts
        # Example:
        # "Untitled - Figma" -> ["untitled", "figma"]
        title_parts = re.split(
            r"[-|–—:]",
            lower_title
        )

        title_parts = [
            part.strip()
            for part in title_parts
            if part.strip()
        ]

        # =========================
        # 1. EXACT PART MATCH
        # =========================
        for part in title_parts:

            if app_name == part:

                print(
                    "Exact window match:",
                    app_name,
                    "->",
                    title,
                    "| confidence: 1.0"
                )

                return title, 1.0


        # =========================
        # 2. SAFE PARTIAL MATCH
        # =========================
        if len(app_name) >= 4:

            for part in title_parts:

                # Example:
                # "photoshop" inside
                # "adobe photoshop 2023"
                if app_name in part:

                    score = difflib.SequenceMatcher(
                        None,
                        app_name,
                        part
                    ).ratio()

                    # Partial matches are not automatically 1.0
                    score = max(score, 0.75)

                    if score > best_score:
                        best_score = score
                        best_window_title = title


        # =========================
        # 3. FUZZY MATCH
        # =========================
        for part in title_parts:

            score = difflib.SequenceMatcher(
                None,
                app_name,
                part
            ).ratio()

            if score > best_score:
                best_score = score
                best_window_title = title


    # =========================
    # RETURN BEST MATCH
    # =========================
    if best_window_title:

        print(
            "Best window match:",
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
                print(
                    "Could not close window:",
                    error
                )
                return False

    return False