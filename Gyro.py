from imu import MPU6050
from time import sleep
from machine import Pin, I2C

LED = machine.Pin("LED", machine.Pin.OUT)
LED.on()

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(i2c)

while True:
    ax=round(imu.accel.x,2)
    ay=round(imu.accel.y,2)
    az=round(imu.accel.z,2)
    gx=round(imu.gyro.x) +3.235445
    gy=round(imu.gyro.y) +2.162849
    gz=round(imu.gyro.z) +1.120858
    tem=round(imu.temperature,2)
    print("ax",ax,"\n","ay",ay,"\n","az",az,"\n","gx",gx,"\n","gy",gy,"\n","gz",gz,"\n","Temperature",tem,"        ",end="\r")
    sleep(0.2) 