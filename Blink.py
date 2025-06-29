import pyfirmata
import time

board = pyfirmata.Arduino('COM5')

while True:
    board.digital[13].write(1)  # Turn on the LED
    time.sleep(1)                # Wait for 1 second
    board.digital[13].write(0)  # Turn off the LED
    time.sleep(1)                # Wait for 1 second