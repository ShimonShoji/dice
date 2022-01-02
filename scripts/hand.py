#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0
dice[]=[0,0,0,0,0]

def cb(message):
	global n
	n = message.data

rospy.init_node('hand')
sub = rospy.Subscriber('roll', Int32, cb)

while not rospy.is_shutdown():
	dice[0]=n
	rospy.loginfo(dice[0]*100)
	rate.sleep

rospy.spin()
