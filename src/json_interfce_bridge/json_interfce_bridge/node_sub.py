#!/usr/bin/env python3

import json
import rclpy

from rclpy.node import Node
from rclpy.logging import LoggingSeverity

from std_msgs.msg import String

class Sub(Node):
    def __init__(self):
        super().__init__("node_sub", allow_undeclared_parameters=True)

        self.create_subscription(String, "json_bridge", self.sub_callback, 10)
        self.get_logger().log("Subscriber in Action", LoggingSeverity.INFO) 

    def sub_callback(self, msg):
        data = json.loads(msg.data)
        self.get_logger().log(f'{data}', LoggingSeverity.INFO)

def main(args=None):
    rclpy.init(args=args)
    node = Sub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()