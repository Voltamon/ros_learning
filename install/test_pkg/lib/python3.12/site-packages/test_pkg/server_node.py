#!usr/bin/env python3
import rclpy

from rclpy.node import Node
from rclpy.logging import LoggingSeverity

from example_interfaces.srv import AddTwoInts

class ServerNode(Node):
    def __init__(self):
        super().__init__('server_node')
        self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)
        self.get_logger().log('Server in Action', LoggingSeverity.INFO)

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().log(f'Request: {request.a} + {request.b} = {response.sum}', LoggingSeverity.INFO)
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ServerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
