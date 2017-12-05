import rospy
from std_msgs.msg import String, Float64MultiArray
import main

def talker():
    float64[] axes = [main.leftX,main.leftY,main.rightX,main.rightY]
    pub = rospy.Publisher('controls', Float64MultiArray, queue_size=10)
    rospy.init_node('controller_base', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        axes = [main.leftX,main.leftY,main.rightX,main.rightY]
        rospy.loginfo(axes)
        pub.publish(axes)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
