#!usr/bin/env python3
import rclpy

from rclpy.node import Node
from rclpy.logging import LoggingSeverity

from std_msgs.msg import String

class TopicNode(Node):
    def __init__(self):
        super().__init__("topic_node")
        self.publisher_ = self.create_publisher(String, "topic_news", 10)
        
        self.create_timer(1, self.publish_news)
        self.get_logger().log("Publisher in Action", LoggingSeverity.INFO)


    def publish_news(self):
        msg = String()
        msg.data = "Hello, this is a topic"

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TopicNode()
    rclpy.spin(node)
    rclpy.shutdown()

