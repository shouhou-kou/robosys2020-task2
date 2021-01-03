#!/usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node('count')
pub = rospy.Publisher('count_up', String, queue_size=10)
rate = rospy.Rate(10)
n = 500
plus= True
while not rospy.is_shutdown():
    msg = str(n)
    pub.publish(msg)
    rate.sleep()
    if plus:
        n+=100
    else:
        n-=100
    if n==2500:
        plus = False

    if n==500:
        plus = True
