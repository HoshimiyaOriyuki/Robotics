#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Config
ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

right_ultra = UltrasonicSensor(Port.S4)
front_ultra = UltrasonicSensor(Port.S3)

gyro = GyroSensor(Port.S2)

data = []

gyro.reset_angle(0)

count = 0
while gyro.angle() < 320:
  left_motor.run(200)
  right_motor.run(-200)
  print(front_ultra.distance())
  data.append(front_ultra.distance())
  
print(data)