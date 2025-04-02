#!/user/bin/env python3
import rclpy
from rclpy.node import Node

class TurtleControllerNode(Node):

    def __init__(self):
        super().__init__ ("urtrle_controller")
        self.get_logger().info("Turtle controller has been started")


def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
