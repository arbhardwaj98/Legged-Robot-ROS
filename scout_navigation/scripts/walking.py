#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def talker():
	pub1 = rospy.Publisher('/scout/joint1_position_controller/command', Float64, queue_size=10)
	pub2 = rospy.Publisher('/scout/joint2_position_controller/command', Float64, queue_size=10)
	pub3 = rospy.Publisher('/scout/joint3_position_controller/command', Float64, queue_size=10)
	pub4 = rospy.Publisher('/scout/joint4_position_controller/command', Float64, queue_size=10)
	rospy.init_node('walking_scout', anonymous=False)
	rate = rospy.Rate(1) # 10hz
	rate2 = rospy.Rate(1)
	leg_count = 0
	timeStamp = rospy.get_rostime()
	pub1.publish(0)
	pub2.publish(0)
	pub3.publish(0)
	pub4.publish(0)
	while not rospy.is_shutdown():
		if leg_count == 0:			
			pub1.publish(2)
			rate2.sleep()
			rate2.sleep()
			pub2.publish(-1)
			pub3.publish(-1)
			pub4.publish(-1)
			rate2.sleep()
			rate2.sleep()
		else:
			pub1.publish(0)
			pub2.publish(0)
			pub3.publish(0)
			pub4.publish(0)
			rate2.sleep()
			rate2.sleep()
		leg_count = (leg_count+1)%2
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
