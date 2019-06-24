#!/usr/bin/env python


import rospy
from std_msgs.msg import String

from geometry_msgs.msg import Twist
from time import sleep 



speed=5


rospy.init_node('rotate')


def callback(data):

    hi=data.data
   
    msg=Twist()
    global speed
    if hi=="q":

    	speed=speed*2
    	print(speed)
    	



    if hi =="i":
    
        
       
      

        msg.linear.x = speed; msg.linear.y = 0.0; msg.linear.z = 0
        msg.angular.x = 0; msg.angular.y = 0; msg.angular.z = 0
        publisher.publish(msg)
    

        

    if hi == "j" :

        msg.linear.x = 0.0; msg.linear.y = 0; msg.linear.z = 0
        msg.angular.x = 0; msg.angular.y = 0; msg.angular.z = 0.5
        publisher.publish(msg)
    
    if hi == "o":

        msg.linear.x = 0.0; msg.linear.y = 0; msg.linear.z = 0
        msg.angular.x = 0; msg.angular.y = 0; msg.angular.z = 0.0
        publisher.publish(msg)

        


publisher=rospy.Publisher('/cmd_vel',Twist,queue_size=1)


rotate_right = True 

if __name__ == '__main__':


    rospy.Subscriber("chatter", String, callback)
    

    



    rospy.spin()
