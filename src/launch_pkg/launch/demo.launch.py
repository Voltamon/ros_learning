#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pub_node = Node(
        package="data_interface_bridge",
        executable="pub",
        name="data_publisher",
        output='screen',
        parameters=[{
            "timer_period" : 2.0
        }]
    )

    sub_node = Node(
        package="data_interface_bridge",
        executable="sub",
        name="data_subscriber",
        output='screen'
    )

    return LaunchDescription([
        pub_node,
        sub_node
    ])