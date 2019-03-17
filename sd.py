#! Python3

# Simple script to calculate your top of descent.

# Get the necessary values

while True:
    try:
        start = int(input("Starting Altitude: "))
        target = int(input("Target Altitude: "))
        rate = int(input("Descent Rate: "))
    except ValueError:
        print("That's not a valid number. Try again.")
    else:
        # Math stuff
        diff = start - target
        time = int(diff / rate)
        dist = (diff * 3) / 1000
        # Print the answers!
        print("Start descent", time , "minutes prior to target location")
        print("Start descent" , dist , "miles from target location")
