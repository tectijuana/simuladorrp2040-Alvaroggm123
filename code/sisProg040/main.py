from machine import Pin, SPI
import utime as time
from imu import MPU6050
from fusion import Fusion
#from ulab import numpy as np # Doesn't work in the Wokwi firmware
import sdcard
import uos

# Initialise IMU
sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=20000)
imu = MPU6050(i2c)
fuse = Fusion()


# Initialise SD Card
sd_spi = SPI(1, sck=Pin(10, Pin.OUT), mosi=Pin(11, Pin.OUT), miso=Pin(12, Pin.OUT))
sd = sdcard.SDCard(sd_spi, Pin(9, Pin.OUT))

print('Finished init of SD card')
print("Size: {} MB".format(sd.sectors/2048))
print(uos.listdir("/"))

#uos.mount(sd, "/sd") # DEBUGGING THIS STEP NOW


# Create a file and write something to it
with open("/test01.txt", "w") as file:
    file.write("Hello, SD World!\r\n")
    file.write("This is a test\r\n")

# Open the file we just created and read from it
with open("/test01.txt", "r") as file:
    data = file.read()
    print(data)

# Experimental position calculation section
'''
def calc_position(pos_init, acc, quat, rate):
    # From https://github.com/thomas-haslwanter/scikit-kinematics/blob/master/src/skinematics/imus.py
    # Calculate the position, assuming that the orientation is already known.

    initialPosition = pos_init
    # Acceleration, velocity, and position ----------------------------
    # From q and the measured acceleration, get the \frac{d^2x}{dt^2}
    g = 9.80665
    g_v = np.r_[0, 0, g] 
    accReSensor = acc - vector.rotate_vector(g_v, quat.q_inv(quat))
    accReSpace = vector.rotate_vector(accReSensor, quat)

    # Position and Velocity through integration, assuming 0-velocity at t=0
    vel = np.nan*np.ones_like(accReSpace)
    pos = np.nan*np.ones_like(accReSpace)

    for ii in range(accReSpace.shape[1]):
        # Swap out scipy.cumtrapz for https://numpy.org/doc/stable/reference/generated/numpy.trapz.html?
        vel[:,ii] = cumtrapz(accReSpace[:,ii],
                                dx=1./np.float(rate), initial=0)
        pos[:,ii] = cumtrapz(vel[:,ii],
                    dx=1./np.float(rate), initial=initialPosition[ii])

    return { "vel": vel, "pos": pos }
'''

# Choose test to run
Timing = True

if Timing:
    accel = imu.accel.xyz
    gyro = imu.gyro.xyz
    start = time.ticks_us()  # Measure computation time only
    fuse.update_nomag(accel, gyro) # 979μs on Pyboard
    t = time.ticks_diff(time.ticks_us(), start)
    print("Update time (uS):", t)

count = 0
while True:
    fuse.update_nomag(imu.accel.xyz, imu.gyro.xyz)
    print(str(fuse.q).replace("(","").replace(")",""))
    '''
    if count % 50 == 0:
        print("Heading, Pitch, Roll: {:7.3f} {:7.3f} {:7.3f}".format(fuse.heading, fuse.pitch, fuse.roll))
        print("Quarternion: " + str(fuse.q))
        print()
    '''
    time.sleep_ms(2) # Maximum 500 hZ cycle rate
    count += 1
    