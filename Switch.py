import pyfirmata
import time

board = pyfirmata.Arduino('COM5')  # Adjust the port as necessary

it = pyfirmata.util.Iterator(board)
it.start()

"""
board.digital[10].mode = pyfirmata.INPUT  # Set pin 10 as input

while True:
    sw = board.digital[gfhfth10].read()  # Read the state of the switch
    if sw is True:
        board.digital[13].write(1) 
    else:
        board.digital[13].write(0)
    time.sleep(0.1) ### Turn on the LED
"""
digital_pin = board.get_pin('d:10:i')  # Set pin 10 as input
led_pin = board.get_pin('d:13:o')  # Set pin 13 as output

while True:
    sw = digital_pin.read()  # Read the state of the switch
    if sw is True:
        led_pin.write(1)
    else:
        led_pin.write(0)
    time.sleep(0.1)  # Wait for 100 milliseconds