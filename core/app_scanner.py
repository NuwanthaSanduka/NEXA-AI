import os
import difflib


BLOCKED_WORDS = [
    "uninstall",
    "help",
    "manual",
    "documentation",
    "release notes",
    "language preferences",
    "upload center"
]


def scan_apps():
    apps = {}

    start_menu_paths = [
        os.path.join(
            os.environ.get("APPDATA", ""),
            "Microsoft",
            "Windows",
            "Start Menu",
            "Programs"
        ),
        os.path.join(
            os.environ.get("PROGRAMDATA", ""),
            "Microsoft",
            "Windows",
            "Start Menu",
            "Programs"
        )
    ]

    for start_menu in start_menu_paths:

        if not os.path.exists(start_menu):
            continue

        for root, folders, files in os.walk(start_menu):

            for file in files:

                if not file.lower().endswith(".lnk"):
                    continue

                app_name = os.path.splitext(file)[0].lower().strip()

                if any(word in app_name for word in BLOCKED_WORDS):
                    continue

                app_path = os.path.join(root, file)

                apps[app_name] = app_path

    return apps


def find_app(app_name):
    apps = scan_apps()

    app_name = app_name.lower().strip()

    # Exact match
    if app_name in apps:
        return apps[app_name]

    # Partial match
    for installed_name, path in apps.items():
        if app_name in installed_name:
            return path

    # Fuzzy match
    app_names = list(apps.keys())

    matches = difflib.get_close_matches(
        app_name,
        app_names,
        n=1,
        cutoff=0.6
    )

    if matches:
        matched_app = matches[0]

        print("Matched:", app_name, "->", matched_app)

        return apps[matched_app]

    return None