import pyfirmata
import time

board = pyfirmata.Arduino('COM5')  # Adjust the port as necessary

it = pyfirmata.util.Iterator(board)
it.start()

board.digital[10].mode = pyfirmata.INPUT  # Set pin 10 as input

while True:
    sw = board.digital[10].read()  # Read the state of the switch
    if sw is True:
        board.digital[13].write(1) 
    else:
        board.digital[13].write(0)
    time.sleep(0.1) # Turn on the LED