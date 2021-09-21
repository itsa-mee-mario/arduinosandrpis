import pyfirmata
print('loading')
board = pyfirmata.Arduino('/dev/ttyACM0')
print('connected to board')
pin = board.get_pin("d:13:o")
pin.write(1)
