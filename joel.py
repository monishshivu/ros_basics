#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def read_durjoy(data):

   read = "I have read durjoy's novel with title - "+str(data.data)

   print(read)

def read_ananth(data):

   read = "I have read ananth's comics with title - "+str(data.data)

   print(read)  

def subscriber():   

   rospy.init_node('Joel')

   rospy.Subscriber('novel', String, read_durjoy)

   rospy.Subscriber('comics', String, read_ananth)

   rospy.spin()  

if __name__ == '__main__' :

   try:

      subscriber()

   except rospy.ROSInterruptException:
      pass   
