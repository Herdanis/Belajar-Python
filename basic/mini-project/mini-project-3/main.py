command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car Already started!")
        else:
            started = True
            print("Car Started...")
    elif command == "stop":
        if not started:
            print("Car Already stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print(
            """
start - to start
stop - to stop
quit - to quit
              """
        )
    elif command == "quit":
        break
    else:
        print("Sorry, I dont understand")
