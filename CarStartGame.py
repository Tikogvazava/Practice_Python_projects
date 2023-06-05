typing_here=""
started=False

while True:
    typing_here=input("> ")
    if typing_here.lower()=="start":
        if started:
            print("Car is already started!")
        else:
            started=True
            print("Car started...")
    elif typing_here== "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started=False
            print("Car stopped.")
    elif typing_here=="help":
        print("""
start-to start the car
stop-to stop the car
quit-to quit the car
""")
    elif typing_here=="quit":
        break
    else:
        print("Sorry, I do not understand that")
        
        
