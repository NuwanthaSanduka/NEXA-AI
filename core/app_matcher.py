import difflib

from core.app_scanner import scan_apps


def match_app(spoken_name):
    spoken_name = spoken_name.lower().strip()

    apps = scan_apps()

    if not apps:
        return None

    app_names = list(apps.keys())

    # 1. Exact match
    if spoken_name in apps:
        print("Exact app match:", spoken_name)
        return spoken_name, apps[spoken_name], 1.0

    # 2. Partial match
    partial_matches = []

    for app_name in app_names:
        if spoken_name in app_name or app_name in spoken_name:
            partial_matches.append(app_name)

    if partial_matches:
        best_match = min(partial_matches, key=len)

        score = difflib.SequenceMatcher(
            None,
            spoken_name,
            best_match
        ).ratio()

        print(
            "Partial app match:",
            spoken_name,
            "->",
            best_match,
            "| confidence:",
            round(score, 2)
        )

        return best_match, apps[best_match], score

    # 3. Fuzzy match
    best_match = None
    best_score = 0.0

    for app_name in app_names:
        score = difflib.SequenceMatcher(
            None,
            spoken_name,
            app_name
        ).ratio()

        if score > best_score:
            best_score = score
            best_match = app_name

    if best_match:
        print(
            "Fuzzy app match:",
            spoken_name,
            "->",
            best_match,
            "| confidence:",
            round(best_score, 2)
        )

        return best_match, apps[best_match], best_score

    return None