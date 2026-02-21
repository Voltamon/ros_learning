#!/usr/bin
import rclpy

from rclpy.node import Node
from rclpy.logging import LoggingSeverity

from example_interfaces.msg import Int64

class NumberPublisher(Node):
    def __init__(self):
        super().__init__('number_publisher')
        self.publisher_ = self.create_publisher(Int64, 'number', 10)
        self.create_timer(1.0, self.timer_callback)
        self.i = 1

        self.get_logger().log('Number Publisher in Action', LoggingSeverity.INFO)

    def timer_callback(self):
        msg = Int64()
        msg.data = self.i
        self.publisher_.publish(msg)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    number_publisher = NumberPublisher()
    rclpy.spin(number_publisher)
    number_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
