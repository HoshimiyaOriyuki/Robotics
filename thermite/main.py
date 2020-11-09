#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from threading import Thread
import sys

# Config

drive_motor = Motor(Port.A)

left_motor = Motor(Port.C)
right_motor = Motor(Port.B)

front_ultra = UltrasonicSensor(Port.S1)
right_ultra = UltrasonicSensor(Port.S3)


# Main

def align():
  left_motor.run_until_stalled(-5000)
  left_motor.reset_angle(0)
  left_motor.run_target(5000, 143)
  left_motor.reset_angle(0)

  right_motor.run_until_stalled(5000)
  right_motor.reset_angle(0)
  right_motor.run_target(5000, -143)
  right_motor.reset_angle(0)


def turn(turn_speed, angle):
  t1 = Thread(target=left_motor.run_target(turn_speed, angle))
  t2 = Thread(target=right_motor.run_target(turn_speed, angle))

  t1.start()
  t2.start()

def steering(turn_speed, angle, forward_speed):
  turn(turn_speed, angle)

  drive_motor.run(forward_speed)


align()

while True:
  steering(5000, 35, 0)
  break