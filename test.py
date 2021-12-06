import platform

string = platform.platform()

match string:
    case string if "macOS" in string:
        print("This system is macOS")
    case string if "Windows" in string:
        print("This system is Windows")
    case _:
        print("This is a linux system")
