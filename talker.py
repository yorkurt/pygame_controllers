#!/usr/bin/env python

import rospy
from std_msgs.msg import String#, Float64MultiArray
from controller.msg import FloatList, IntList
#import main

def talker():
    #float64[4] axes = [main.leftX,main.leftY,main.rightX,main.rightY]
    pub_axes = rospy.Publisher('controls', FloatList, queue_size=10)
    pub_buttons = rospy.Publisher('buttons', IntList, queue_size=10)
    rospy.init_node('controller_base', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    axes = FloatList()
    buttons = IntList()
    while not rospy.is_shutdown():
        #axes.data = [main.leftX,main.leftY,main.rightX,main.rightY]
	axes.data = [1,-1,0,1]
	#buttons.data = main.buttonArr1
	buttons.data = [1,0,1,0,1]
        rospy.loginfo(axes)
        pub_axes.publish(axes)
	rospy.loginfo(buttons)
        pub_buttons.publish(buttons)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
