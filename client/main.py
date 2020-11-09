#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from pybricks.messaging import BluetoothMailboxClient, TextMailbox

# Config

pivot_motor = Motor(Port.A)

pivot_ultra = UltrasonicSensor(Port.S4)
left_light = ColorSensor(Port.S1)
right_light = ColorSensor(Port.S2)


# This is the name of the remote EV3 or PC we are connecting to.
SERVER = 'serotonin'

client = BluetoothMailboxClient()
mbox = TextMailbox('main', client)

print('establishing connection...')
client.connect(SERVER)
print('connected!')


mbox.send('ready')
mbox.wait()

pivot_motor.run_target(200, 90)
pivot_motor.run_target(200, 0)

while True:
  mbox.send(left_light.ambient() - right_light.ambient())
  mbox.wait()