import serial
import time
import matplotlib.pyplot as plt
import numpy as np
import wavio


ser = serial.Serial('/dev/cu.usbmodem14201',9600)
time.sleep(2)


data =[]    
                   
t_end = time.time() + 3

while time.time() < t_end:
    
    b = ser.readline()         
    string = b.decode()  
    string = string.strip()
    flt = float(string)       
    
    data.append(flt) 
             

ser.close()

plt.plot(data)
plt.xlabel('Time')
plt.ylabel('Mic output')
plt.title('Mic output vs. Time')
plt.show()

print(len(data))

arr = np.array(data)
arr_norm = arr / 5

wavio.write("out3.wav", arr_norm, 2231, sampwidth=3)
