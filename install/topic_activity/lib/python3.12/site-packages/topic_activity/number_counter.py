#!/usr/bin/env python3
import rclpy
import time

from rclpy.node import Node
from rclpy.logging import LoggingSeverity

from std_msgs.msg import Int64

class NumberCounter(Node):
    def __init__(self):
        super().__init__("number_counter")

        self.publisher_ = self.create_publisher(Int64, "number", 10)
        self.create_subscription(Int64, "number", self.counter_callback, 10)
        
        self.create_timer(1.0, self.timer_callback)

        self.get_logger().log("Counter in Action", LoggingSeverity.INFO)

    def counter_callback(self, msg : Int64):
        if hasattr(self, "count"):
            if self.count == msg.data:
                return

        self.count = msg.data
        self.get_logger().log(str(msg.data), LoggingSeverity.INFO)

    def timer_callback(self):
        if not hasattr(self, "count"):
            self.count = 0

        msg = Int64()
        msg.data = self.count + 1
        self.publisher_.publish(msg)
        
def main(args=None):
    rclpy.init(args=args)

    node = NumberCounter()
    rclpy.spin(node)
    node.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()
