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
        return spoken_name, apps[spoken_name]

    # 2. Partial match
    partial_matches = []

    for app_name in app_names:
        if spoken_name in app_name or app_name in spoken_name:
            partial_matches.append(app_name)

    if partial_matches:
        # Prefer the shortest matching name
        best_match = min(partial_matches, key=len)

        print("Partial app match:", spoken_name, "->", best_match)

        return best_match, apps[best_match]

    # 3. Fuzzy match
    matches = difflib.get_close_matches(
        spoken_name,
        app_names,
        n=1,
        cutoff=0.5
    )

    if matches:
        best_match = matches[0]

        print("Fuzzy app match:", spoken_name, "->", best_match)

        return best_match, apps[best_match]

    return None