#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from pybricks.messaging import BluetoothMailboxServer, TextMailbox

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

server = BluetoothMailboxServer()
mbox = TextMailbox('main', server)

# The server must be started before the client!
print('waiting for connection...')
server.wait_for_connection()
print('connected!')

# In this program, the server waits for the client to send the first message
# and then sends a reply.
mbox.wait()
mbox.send(True)

def steering(speed, turn_rate):
  left_motor.run(speed + turn_rate)
  right_motor.run(speed - turn_rate)

def clamp(input, max_value, min_value):
  return max(min(input, max_value), min_value)

def turn_rate_calc(dist, dist_to_target, multiplier):
  return clamp(((dist - dist_to_target) * multiplier), 80, -80)

# while True:
#   mbox.wait()
#   dist = mbox.read()
#   print(dist)
#   steering(200, turn_rate_calc(int(dist), 120, -1.5))
#   mbox.send('recv')

while True:
  mbox.wait()
  dif = mbox.read()
  print(dif)
  steering(0, dif * 2)
  mbox.send('recv')