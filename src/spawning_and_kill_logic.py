#!/usr/bin/env Python3
import rclpy
import random
from rclpy.node import Node
from turtlesim.msg import Pose
from turtlesim.srv import Spawn
from turtlesim.srv import Kill

class SpawnAndKillNode(Node): 

    def __init__(self):
        super().__init__("spawn_and_kill_node")

        self.my_x = 0.0
        self.my_y = 0.0

        self.subscription = self.create_subscription(
            Pose, 
            "/turtle1/pose", 
            self.turtle1_pose_callback,
            10)

        self.turtles = {}
        self.timer_ = self.create_timer(2, self.main_logic)

        self.spawn_client = self.create_client(Spawn, "/spawn")
        self.kill_client = self.create_client(Kill, "/kill")


    def turtle1_pose_callback(self, msg: Pose):
        self.my_x = msg.x
        self.my_y = msg.y


    def main_logic(self):

        request = Spawn.Request()

        request.x = random.uniform(1.0, 10.0)
        request.y = random.uniform(1.0, 10.0)
        request.theta = random.uniform(0.0, 6.28)

        future = self.spawn_client.call_async(request)

        future.add_done_callback(
            lambda future: self.spawn_callback(future, request)
        )

        for turtle_name, position in self.turtles.items():

            distance = (
                (self.my_x - position[0]) ** 2
                + (self.my_y - position[1]) ** 2
            ) ** 0.5

            if distance < 0.5:

                self.get_logger().info(
                    f"Catching {turtle_name}, distance = {distance}"
                )

                kill_request = Kill.Request()
                kill_request.name = turtle_name

                future = self.kill_client.call_async(kill_request)

                future.add_done_callback(
                    lambda future, name=turtle_name: self.kill_callback(future, name)
                )

    def spawn_callback(self, future, request):
        response = future.result()
        self.turtles[response.name] = [request.x, request.y]

    def kill_callback(self, future, turtle_name):

        try:
            future.result()
            self.get_logger().info(f"{turtle_name} killed!")
            del self.turtles[turtle_name]

        except Exception as e:
            self.get_logger().error(f"Failed to kill {turtle_name}: {e}")


def main(args=None):
    rclpy.init(args=args)
    node = SpawnAndKillNode() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

