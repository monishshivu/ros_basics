#!/usr/bin/env python

import rospy
from std_msgs.msg import String

novel_number = 0


def kindler():

   rospy.init_node('Durjoy_datta')

   pub = rospy.Publisher('novel', String, queue_size=10)

   rate = rospy.Rate(10)

   while not rospy.is_shutdown():

      global novel_number

      novel_title = "novel_number  "+str(novel_number)

      pub.publish(novel_title)

      print(novel_title)

      novel_number = novel_number+1

      rate.sleep()



if __name__ == '__main__' :

   try:
      kindler()

   except rospy.ROSInterruptException:
      pass   
