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

drive_motor = Motor(Port.B)

left_motor = Motor(Port.D)
right_motor = Motor(Port.C)

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


def left(turn_speed, angle):
  left_motor.run_target(turn_speed, angle)


def right(turn_speed, angle):
  right_motor.run_target(turn_speed, angle)


def turn(turn_speed, angle):
  t1 = Thread(target=left, args=(turn_speed, angle,))
  t2 = Thread(target=right, args=(turn_speed, angle,))

  t1.start()
  t2.start()


def steering(turn_speed, angle):
  turn(turn_speed, angle)


def clamp(num, min_val, max_val):
  return max(min(num, min_val), max_val)

def turn_calc(dist, offset, multiplier):
  return clamp((dist - offset) * multiplier, -30, 30)

def forwardMovement(speed):
  while(front_ultra.distance() >= 160):
    drive_motor.run(speed)

  if(front_ultra.distance() <= 152  and right_ultra.distance() >= 45):
    while(front_ultra.distance()>= 130 and front_ultra.distance< right_ultra.distance()):
      steering(5000, 45)
      drive_motor.run(speed)
      if(right_ultra.distance() <60):
        while(right_ultra.distance() <60):
          steering(360, -20)
      
      

  elif(front_ultra.distance() <120 & right_ultra.distance() ):
    drive_motor.stop()




align()

forwardMovement(5000)

