#!/usr/bin/env python



import rospy
from std_msgs.msg import String
def faxer():  
       
    rospy.init_node('faxer',anonymous = True) #initialize node
    pub = rospy.Publisher('fax_line', String, queue_size = 10)#initial node name, Type message  
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        message = str(input("Enter your message"))
        rospy.loginfo(message)
        pub.publish(message)
        rate.sleep() 
 
if __name__ == "__main__":
    try:
        faxer()
    except rospy.ROSInterruptException:
        pass
