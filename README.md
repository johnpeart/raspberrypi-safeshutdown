# raspberrypi-safeshutdown

A script for initiating a safe shutdown on a Raspberry Pi when a button, attached to GPIO pins, is pressed.

## Installing the script

1. Get the git repository:\
`git clone https://github.com/johnpeart/raspberrypi-safeshutdown`
2. Change the permissions as the super-user such that you can execute the files:\
`sudo chmod 777 /home/pi/raspberrypi-safeshutdown`
3. Open `rc.local` in the text editor as the super-user:\
`sudo nano /etc/rc.local`
4. Add the following command _**before**_ the `exit 0` at the end of `rc.local`:\
`sudo python /home/pi/raspberrypi-safeshutdown/safe-shutdown.py &`
5. Reboot the Raspberry Pi:\
`sudo reboot`

> **NOTE**: It is _very_ important that you add the code in step 4 _before_ the `exit 0`. If you don't, you'll cause terminal havoc.

## Adding the hardware button

You will need an "Normally Open" ("NO") switch and some wire. You should:

1. attach a wire to each of the terminals on the button
2. attach the other ends of the wire to GPIO 3 and a GND pin (e.g. physical pins 5 and 6)

The benefit of using GPIO 3 is that it will also power *on* the Raspberry Pi when shorted to a GND pin.

## Acknowledgments

Based on tutorial from [Core Electronics](https://core-electronics.com.au/tutorials/how-to-make-a-safe-shutdown-button-for-raspberry-pi.html)