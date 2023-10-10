#!/usr/bin/env python3
import numpy as np
import rclpy
from asl_tb3_lib.control import BaseHeadingController
from asl_tb3_lib.math_utils import wrap_angle
from asl_tb3_msgs.msg import TurtleBotControl
from asl_tb3_msgs.msg import TurtleBotState

class HeadingController(BaseHeadingController):
    def __init__(self, node_name: str = "heading_controller") -> None:
        super().__init__(node_name)
        self.kp = 2.0
    
    def compute_control_with_goal(self, state: TurtleBotState, goal: TurtleBotState) -> TurtleBotControl:
        err = wrap_angle(goal.theta-state.theta)
        theta = self.kp*err
        turtle=TurtleBotControl()
        turtle.omega = theta
        return turtle


if __name__=="__main__":
    rclpy.init()
    node = HeadingController()
    rclpy.spin(node)
    rclpy.shutdown()