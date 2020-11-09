#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase


# Config Code

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

right_ultra = UltrasonicSensor(Port.S4)
front_ultra = UltrasonicSensor(Port.S3)

watch = StopWatch()

gyro = GyroSensor(Port.S2)

color = ColorSensor(Port.S1)
# robot = DriveBase(left_motor, right_motor, wheel_diameter=80.3, axle_track=117.5)

# TODO: Create github repo for Fall Robotics


def steering(speed, turn_rate):
  left_motor.run(speed + turn_rate)
  right_motor.run(speed - turn_rate)

def hold_motors():
  left_motor.hold()
  right_motor.hold()

def turn_rate_calc(dist_to_target, multiplier):
  return clamp(((right_ultra.distance() - dist_to_target) * multiplier), 80, -80)

def clamp(input, max_value, min_value):
  return max(min(input, max_value), min_value)

def turn_left():
  left_motor.hold()
  right_motor.hold()
  gyro.reset_angle(0)
  while True:
    steering(150,-150)
    if gyro.angle() <= -80:
      break


def turn_right():
  left_motor.hold()
  right_motor.hold()
  gyro.reset_angle(0)
  while True:
    steering(150,150)
    if gyro.angle() >= 80:
      break

attempts = 0

turn = 0
while True:
  steering(300, turn_rate_calc(120, .6))

  if front_ultra.distance() <= 180:
    turn_left()
    turn = turn + 1
    print("Turn: " + str(turn))

  if turn == 9:
    turn = -1
    temp = 0
    while True:
      print('9th turn')
      steering(300, turn_rate_calc(120, .6))
      
      dist = front_ultra.distance()

      if dist <= 960:
        temp += 1
        if temp > 20:
          turn_left()
          break
      else:
        temp = 0

    while True:
      print('Into room')
      steering(300, 0)
      if front_ultra.distance() <= 200:
        break

    while True:
      print('Inside Room')
      steering(300, turn_rate_calc(120, .6))
      if front_ultra.distance() <= 200:
        turn_left()
      if color.reflection() >= 15:
        break

    while True:
      print('Out of room')
      steering(300,0)
      if front_ultra.distance() <= 200:
        turn_left()
        attempts += 1
        print('Attempt: ' + str(attempts))
        break




