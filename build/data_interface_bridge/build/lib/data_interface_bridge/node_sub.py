#!/usr/bin/env python3

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import json
import rclpy

from rclpy.node import Node
from rclpy.logging import LoggingSeverity

from std_msgs.msg import String
from interfaces.identity import Identity

class Sub(Node):
    def __init__(self):
        super().__init__("node_sub", allow_undeclared_parameters=True)

        self.create_subscription(String, "data_bridge", self.sub_callback, 10)
        self.get_logger().log("Subscriber in Action", LoggingSeverity.INFO) 

    def sub_callback(self, msg):
        fields = Identity.__annotations__.keys()
        data = {k : v for k, v in json.loads(msg.data).items() if k in fields}

        identity = Identity(**data)
        self.get_logger().log(f'{identity}', LoggingSeverity.INFO)

def main(args=None):
    rclpy.init(args=args)
    node = Sub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()