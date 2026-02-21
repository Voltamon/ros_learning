#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.logging import LoggingSeverity

class TestNode(Node):
    def __init__(self):
        super().__init__("test")
        self.create_timer(1.0, self.timer_callback)
    
    def timer_callback(self):
        self.get_logger().log("Hello, this is a test", LoggingSeverity.INFO)

def main(args=None):
    rclpy.init(args=None)
    node = TestNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()