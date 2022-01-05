#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import Int32
from std_msgs.msg import String

rospy.init_node('roll')
pub = rospy.Publisher('roll', Int32, queue_size=1)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    press_key = input('\npress "e" to exit\npress number-key(1~6) to send the number\npress "r" to roll a dice: ')

    if press_key == "r":
        pub.publish(random.randint(1,6))

    elif press_key == "1":
        pub.publish(1)

    elif press_key == "2":
        pub.publish(2)

    elif press_key == "3":
        pub.publish(3)

    elif press_key == "4":
        pub.publish(4)

    elif press_key == "5":
        pub.publish(5)

    elif press_key == "6":
        pub.publish(6)

    elif press_key == "e":
        break

    rate.sleep()
