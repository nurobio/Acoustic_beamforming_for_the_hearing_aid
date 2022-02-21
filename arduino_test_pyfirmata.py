
from pyfirmata import Arduino, util
import time
import matplotlib.pyplot as plt

board = Arduino("/dev/cu.usbmodem14201")

pin = board.get_pin('a:0:i')

it = util.Iterator(board)
it.start()
data =[] 

t_end = time.time() + 3

while time.time() < t_end:
    value = pin.read()
    data.append(value)

plt.plot(data)
plt.xlabel('Time')
plt.ylabel('Analog input')
plt.title('Analog pin reading')
plt.show()

