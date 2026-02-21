#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.logging import LoggingSeverity

class MyNode(Node):
    def __init__(self):
        super().__init__("node_name")
        self.get_logger().log("This is a template for ROS node", LoggingSeverity.INFO)

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.shutdown()

if __name__ == "__main__":
    main()