import sys
import rospy

from geometry_msgs.msg import Twist
rospy.init_node("cmd_node")
my_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=10)

def send_cmd(v,w):
    twist = Twist()
    twist.linear.x = v
    twist.angular.z = w
    my_publisher.publish(twist)

send_cmd(0.1,0.0)

rospy.spin()