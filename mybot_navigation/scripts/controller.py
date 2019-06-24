#! /usr/bin/python

import rospy
from tf.transformations import euler_from_quaternion
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Twist
from math import atan2

x = 0.0
y = 0.0
theta = 0.0

def moveRobot(x, y):
	goal = Point()
	goal.x = x
	goal.y = y
	return goal


def newOdom (msg):
	global x
	global y
	global theta

	x = msg.pose.pose.position.x
	y = msg.pose.pose.position.y

	rot_q = msg.pose.pose.orientation
	
	(roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
	

rospy.init_node("speed_controller")

sub = rospy.Subscriber("odom", Odometry, newOdom)
pub = rospy.Publisher("cmd_vel", Twist, queue_size = 1)


r = rospy.Rate(4)

speed = Twist()

goal = moveRobot(-1,1)

while not rospy.is_shutdown():
	inc_x = goal.x - x
	inc_y = goal.y - y

	angle_to_goal = atan2(inc_y, inc_x)

	print angle_to_goal

	if abs(angle_to_goal - theta) > 0.1:
		speed.linear.x = 0.0
		speed.angular.z = 0.2
	else:
		speed.linear.x = 0.1
		speed.angular.z = 0.0

	if x - goal.x < inc_x and y - goal.y < inc_y:
		speed.linear.x = 0.0
		speed.angular.z = 0.0		

	pub.publish(speed)
	r.sleep()
