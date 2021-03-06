#!/usr/bin/env python
import rospy
from clever_flight_routines import get_telemetry, takeoff, reach_point, land

rospy.init_node('clever_flight_example')

# copter parameters

speed = 1
z = 1
frame = 'map'
x0 = get_telemetry(frame_id = frame).x
y0 = get_telemetry(frame_id = frame).y

# flight program

takeoff(z)                                                  # takeoff
reach_point(x=x0, y=y0+1, z=z, speed=speed, frame_id=frame) # flight 1m toward
land()
