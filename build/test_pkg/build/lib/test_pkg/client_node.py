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
        self.request = AddTwoInts.Request()

    def send_request(self, a, b):
        self.request.a = a
        self.request.b = b
        self.future = self.client_.call_async(self.request)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main(args=None):
    rclpy.init(args=args)
    node = ClientNode()
    response = node.send_request(2, 3)
    node.get_logger().info(f'Response: {response.sum}')
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
