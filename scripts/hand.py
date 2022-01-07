#!/usr/bin/env python3

# SPDX-License-Identifier: BSD-2.0
"""
* Copyright (C) 2022 Ueda Ryuichi.  All rights reserved.
"""
import rospy
from std_msgs.msg import Int32

n = 0
dice = [0,0,0,0,0,0,100,200,300,400,500]

def cb(message):
    global n
    n = message.data

    if dice[4] != 0:
        dice[5] = n
        rospy.loginfo("5th: %d", dice[5])

        #hand
        hand = sorted(dice)
        dice[1] = 0
        dice[2] = 0
        dice[3] = 0
        dice[4] = 0
        dice[5] = 0
        rospy.loginfo("hand: %d, %d, %d, %d, %d", hand[1], hand[2], hand[3], hand[4], hand[5])
        
        #five-card
        if hand[1] == hand[2] == hand[3] == hand[4] == hand[5]:
            rospy.loginfo("FIVE OF A KIND, %d", hand[5])
        
        #full-house
        elif hand[1] == hand[2] != hand[3] == hand[4] == hand[5] or hand[1] == hand[2] == hand[3] != hand[4] == hand[5]:
            rospy.loginfo("FULL HOUSE, %d", hand[5])
        
        #straight
        elif hand[1]+1 == hand[2] and hand[2]+1 == hand[3] and hand[3]+1 == hand[4] and hand[4]+1 == hand[5]:
            rospy.loginfo("%d high STRAIGHT", hand[5])

        #BUST
        elif hand[1] != hand[2] != hand[3] != hand[4] != hand[5]:
            rospy.loginfo("%d high", hand[5])

        #pairs or else
        else:
            for i in range(1,5):
                #four-card
                if hand[i-1] != hand[i] == hand[i+1] == hand[i+2] == hand[i+3] != hand[i+4]:
                    rospy.loginfo("FOUR OF A KIND, %d", hand[i])
                    break
                #three-card
                elif hand[i-1] != hand[i] == hand[i+1] == hand[i+2] != hand[i+3]:
                    rospy.loginfo("THREE OF A KIND, %d", hand[i])
                    break
                #one-pair
                elif hand[i-1] != hand[i] == hand[i+1] != hand[i+2]:
                    #two-pair
                    if hand[i+2] == hand[i+3] != hand[i+4] or hand[i+2] != hand[i+3] == hand[i+4]:
                        rospy.loginfo("TWO-PAIR, %d", hand[i+3])
                    else:
                        rospy.loginfo("ONE-PAIR, %d", hand[i])
                    break
        rospy.loginfo(" ")

    elif dice[3] != 0:
        dice[4] = n
        rospy.loginfo("4th: %d", dice[4])

    elif dice[2] != 0:
        dice[3] = n
        rospy.loginfo("3rd: %d", dice[3])

    elif dice[1] != 0:
        dice[2] = n
        rospy.loginfo("2nd: %d", dice[2])

    else:
        dice[1] = n
        rospy.loginfo("1st: %d", dice[1])

rospy.init_node('hand')
sub = rospy.Subscriber('roll', Int32, cb)

rospy.spin()

