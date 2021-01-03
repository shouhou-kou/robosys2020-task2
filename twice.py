#!/usr/bin/env python
import rospy
import pigpio
from std_msgs.msg import String
SERVO_PIN =25
pi=pigpio.pi()


def cb(message):
    rospy.loginfo(message.data)
    p_width =int(message.data)
    pi.set_servo_pulsewidth(SERVO_PIN,p_width)

if __name__ == '__main__': 
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', String, cb) 
    rospy.spin()
