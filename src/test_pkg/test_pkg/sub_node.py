#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.logging import LoggingSeverity

from example_interfaces.msg import String

class SubscriberNode(Node):
    def __init__(self):
        super().__init__("sub_node")
        self.subscription_ = self.create_subscription(String, "topic_news", self.fetch_news, 10)
        self.get_logger().log("Subscriber in Action", LoggingSeverity.INFO)

    def fetch_news(self, msg: String):
        self.get_logger().log(msg.data, LoggingSeverity.INFO)


def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()