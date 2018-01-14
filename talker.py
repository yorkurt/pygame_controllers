#!/usr/bin/env python

import rospy
from std_msgs.msg import String#, Float64MultiArray
from controller.msg import FloatList
#import main

def talker():
    #float64[4] axes = [main.leftX,main.leftY,main.rightX,main.rightY]
    pub = rospy.Publisher('controls', FloatList, queue_size=10)
    rospy.init_node('controller_base', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    axes = FloatList()
    while not rospy.is_shutdown():
        #axes.data = [main.leftX,main.leftY,main.rightX,main.rightY]
	axes.data = [1,-1,0,1]
        rospy.loginfo(axes)
        pub.publish(axes)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
