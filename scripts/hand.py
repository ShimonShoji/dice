#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0
dice = [0,0,0,0,0,0,100]

def cb(message):
    global n
    n = message.data
    if dice[4] != 0:
        dice[5] = n
        rospy.loginfo(dice[5]*100000)

        #ソート
        #判定

    elif dice[3] != 0:
        dice[4] = n
        rospy.loginfo(dice[4]*10000)

    elif dice[2] != 0:
        dice[3] = n
        rospy.loginfo(dice[3]*1000)

    elif dice[1] != 0:
        dice[2] = n
        rospy.loginfo(dice[2]*100)

    else:
        dice[1] = n
        rospy.loginfo(dice[1]*10)

rospy.init_node('hand')
sub = rospy.Subscriber('roll', Int32, cb)

"""
if dice[4] != 0:
    dice[5] = n
    rospy.loginfo(dice[5]*100)

elif dice[3] != 0:
    dice[4] = n
    rospy.loginfo(dice[4]*100)

elif dice[2] != 0:
    dice[3] = n
    rospy.loginfo(dice[3]*100)

elif dice[1] != 0:
    dice[2] = n
    rospy.loginfo(dice[2]*100)

else:
    dice[1] = n

    rospy.loginfo(dice[0]*100)
    rospy.loginfo(dice[1]*100)
    rospy.loginfo(dice[2]*100)
    rospy.loginfo(dice[3]*100)
    rospy.loginfo(dice[4]*100)
    rospy.loginfo(dice[5]*100)
    rospy.loginfo(dice[6]*100)
"""
rospy.spin()

