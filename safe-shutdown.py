from gpiozero import Button #import button from the Pi GPIO library
import time # import time functions
import os #imports OS library for Shutdown control

stopButton = Button(3) # defines the button as an object and chooses GPIO 3

# This script will run every 10 seconds. If the button is pressed, 
# it will shutdown the Raspberry Pi and put it into a low power state.
# Because the script only runs every 10 seconds, you need to keep 
# hold of the button for up to 10 seconds to initiate a shutdown.

while True: #infinite loop
    if stopButton.is_pressed: # Check to see if button is pressed
        os.system("halt") # shut down the Pi
    time.sleep(10) # wait to loop again so we don't use the processor too much.