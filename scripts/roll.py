#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import Int32
from std_msgs.msg import String

rospy.init_node('roll')
pub = rospy.Publisher('roll', Int32, queue_size=1)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    press_key = input('press "e" to exit\npress "r" to roll a dice: ')

    if press_key == "r":
        pub.publish(random.randint(1,6))

    if press_key == "e":
        break

    rate.sleep()
