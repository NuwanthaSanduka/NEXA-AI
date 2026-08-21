import os


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

    if app_name in apps:
        return apps[app_name]

    for installed_name, path in apps.items():
        if app_name in installed_name:
            return path

    return None