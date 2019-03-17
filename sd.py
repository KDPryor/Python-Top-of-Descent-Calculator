#! Python3

# Simple script to calculate your top of descent.

# Get the necessary values

try:
    start = int(input("Starting Altitude: "))
except ValueError:
    print("That's not a valid number. Try again.")

try:
    target = int(input("Target Altitude: "))
except ValueError:
    print("That's not a valid number. Try again.")

try:
    rate = int(input("Descent Rate: "))

except ValueError:
    print("That's not a valid number. Try again.")

# Math stuff
diff = start - target
time = int(diff / rate)
dist = (diff * 3) / 1000

# Print the answers!
print("Start descent", time , "minutes prior to target location")
print("Start descent" , dist , "miles from target location")
