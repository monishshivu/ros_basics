#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def read(data):

   read = "I have read durjoy,s novel - "+str(data.data)

   print(read)

def subscriber():

   rospy.init_node('Ananth_pai')

   rospy.Subscriber('novel',String, read)

   pub = rospy.Publisher('comics', String, queue_size=10)

   rate = rospy.Rate(10)

   while not rospy.is_shutdown():

      pub.publish('comic_title')

      rate.sleep()

   rospy.spin()


if __name__ == '__main__' :
   try:
      subscriber()

   except rospy.ROSInterruptException:
      pass   
