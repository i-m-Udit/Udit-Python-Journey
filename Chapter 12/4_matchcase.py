force=input("Enter:")
match force:
    case "Start":
        print("Machine is starting")
    case "Stop":
        print("Stopping the machine")
    case "Pause":
        print("Pausing the machine")
    case _:
        print("Unknown force")