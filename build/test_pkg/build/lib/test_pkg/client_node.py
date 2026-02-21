#!usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.logging import LoggingSeverity

from example_interfaces.srv import AddTwoInts

class ClientNode(Node):
    def __init__(self):
        super().__init__('client_node')
        self.client_ = self.create_client(AddTwoInts, 'add_two_ints')
        self.client_.wait_for_service()

    def add_int(self, a, b):
        self.request = AddTwoInts.Request()
        self.request.a = a
        self.request.b = b

        self.future = self.client_.call_async(self.request)
        self.future.add_done_callback(self.response_callback)

    def response_callback(self, future):
        self.get_logger().info(f'Response: {future.result().sum}')
    

def main(args=None):
    rclpy.init(args=args)
    node = ClientNode()
    node.add_int(2, 3)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
