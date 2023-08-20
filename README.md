# IoT-worksheet-3

Raspberry Pi and micro:bit IoT Setup

Description: A simple IoT setup using Raspberry Pi and micro:bit. The Raspberry Pi sends commands (LED_ON or LED_OFF) to the micro:bit.

Architecture: The Raspberry Pi acts as the server, and the micro:bit acts as the client. The Raspberry Pi sends a signal via USB-serial connection to the micro:bit to control the LED display.

Setup:

Flash microbit_code.py onto the micro:bit using the MicroPython editor.
SSH into the Raspberry Pi and navigate to the project directory.
Run the raspberry_code.py script.

Usage:

After starting the raspberry_code.py script, you'll be prompted to enter a command.
Enter "LED_ON" to display a happy face on the micro:bit.
Enter "LED_OFF" to clear the display.

Contributors:

Ahmed Ali
S2201026
