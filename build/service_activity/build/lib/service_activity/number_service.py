#!/usr/bin/env python3
import rclpy

from rclpy.node import Node
from rclpy.logging import LoggingSeverity

from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class NumberService(Node):
    def __init__(self):
        super().__init__("number_server")

        self.publisher_ = self.create_publisher(Int64, "number", 10)
        self.create_subscription(Int64, "number", self.number_callback, 10)
        self.create_service(SetBool, "reset_count", self.reset_callback)

        self.get_logger().log("Server in Action", LoggingSeverity.INFO)

    def number_callback(self, msg : Int64):
        if hasattr(self, "num"):
            if self.num == msg.data:
                return
        
        self.num = msg.data
        self.get_logger().log(str(msg.data), LoggingSeverity.INFO)

    def reset_callback(self, request, response):
        if not request.data:
            response.success = False
            response.message = "Counter reset failed"
            
            return response

        msg = Int64()
        msg.data = 0
        self.publisher_.publish(msg)

        response.success = True
        response.message = "Counter reset successfully"

        self.get_logger().log(response.message, LoggingSeverity.INFO)
        return response

def main(args=None):
    rclpy.init(args=args)
    node = NumberService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()