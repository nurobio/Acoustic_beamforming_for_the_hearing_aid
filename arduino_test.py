import serial
import time
import matplotlib.pyplot as plt
import numpy as np
import wavio


ser = serial.Serial('/dev/cu.usbmodem14201',115200)
time.sleep(2)

# Read and record the data
data =[]    
                   # empty list to store the data
t_end = time.time() + 3

while time.time() < t_end:
    try:
        b = ser.readline()         # read a byte string
        string = b.decode()  # decode byte string into Unicode  
        string = string.strip()
        flt = float(string)        # convert string to float
    
        data.append(flt) 
             # add to the end of data list
    except UnicodeDecodeError: # catch error and ignore it
        data.append(0)
    except ValueError: # catch error and ignore it
        data.append(0)

ser.close()

plt.plot(data)
plt.xlabel('Time')
plt.ylabel('Mic output')
plt.title('Mic output vs. Time')
plt.show()

print(len(data))

arr = np.array(data)
arr_norm = arr / 5

wavio.write("out.wav", arr_norm, 2231, sampwidth=3)
