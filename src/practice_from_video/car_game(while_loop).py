user_input = ""
started = False


while True:
    user_input = input("> ").lower()
    if user_input.lower() == "help":
        print('''
start = start the car
stop = stop the car
quit = quit game  ''')

    elif user_input.lower() == "start":
        if started:
            print("Car already started!")
        else:
            print(" Car started...Ready to go!")
            started = True

    elif user_input.lower() == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            print(" Car stopped.")
            started = False

    elif user_input.lower() == "quit":
        break
    else:
        print("I don't understand that!")
