import pygetwindow as gw


def close_app(app_name):
    app_name = app_name.lower().strip()

    windows = gw.getAllWindows()

    for window in windows:
        title = window.title.lower().strip()

        if app_name in title and title:
            print("Closing:", window.title)

            try:
                window.close()
                return True

            except Exception as error:
                print("Could not close window:", error)
                return False

    return False