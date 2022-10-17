#!/usr/bin/env python
import rospy
from std_msgs.msg import String
def fax_handle(data):
    rospy.loginfo("I heard "+str(data.data))
def printer():
    rospy.init_node('Printer',anonymous= True)
    rospy.Subscriber('fax_line',String, fax_handle)
    rospy.spin()

if __name__ == "__main__":
    printer()
