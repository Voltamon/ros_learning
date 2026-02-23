#!/usr/bin/env python3

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import json
import rclpy

from rclpy.node import Node
from rclpy.logging import LoggingSeverity

from std_msgs.msg import String
from dataclasses import asdict
from interfaces.identity import Identity

class Pub(Node):
    def __init__(self):
        super().__init__("node_pub", allow_undeclared_parameters=True)
        self.declare_parameter("timer_period", 1.0)

        self.publisher_ = self.create_publisher(String, "data_bridge", 10)
        self.create_timer(self.get_parameter("timer_period").value, self.pub_callback)

        self.get_logger().log("Publisher in Action", LoggingSeverity.INFO)

    def pub_callback(self):
        data = Identity(id=48, name="voltamon")

        msg = String()
        msg.data = json.dumps(asdict(data))
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = Pub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()