#!/usr/bin/env python

import sys
import rospy
import actionlib

from geometry_msgs.msg import Twist
from tf.transformations import quaternion_from_euler
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


rospy.init_node("straight_node")
my_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=10)
client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

print(client.wait_for_server())

def update_init_pose(self, x, y, theta):
    init_pose = PoseWithCovarianeStamped()
    init_pose.header.frame_id = "map"
    init_pose.header.stamp = rospy.Time.now()
    init_pose.pose.pose.position.x = 0.0
    init_pose.pose.pose.position.y = 0.0
    init_pose.pose.pose.position.orientation.w = 0.0
    q = quaternion_from_euler(0.0, 0.0, theta)
    init_pose.pose.pose.orientation.x = q[0]
    init_pose.pose.pose.orientation.y = q[1]
    init_pose.pose.pose.orientation.z = q[2]
    init_pose.pose.pose.orientation.w = q[3]


def send_goal(x, y, theta):
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    q = quaterntion_from_equler(0.0, 0.0, theta)
    goal.target_pose.pose.orientation.x = q[0]
    goal.target_pose.pose.orientation.y = q[1]
    goal.target_pose.pose.orientation.z = q[2]
    goal.target_pose.pose.orientation.w = q[3]
    client.send_goal(goal)

update_init_pose(0.2,0.3,0.0)
send_goal(1.0,0.3,0.0)

def main(self):
    rospy.spin()
