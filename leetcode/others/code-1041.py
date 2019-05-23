# 1041. Robot Bounded In Circle On an infinite plane, a robot initially stands at(0, 0) and faces north.
# The robot can receive one of three instructions: "G": go straight 1 unit; "L": turn 90 degrees to the left;
# "R": turn 90 degress to the right. The robot performs the instructions given in order, and repeats them forever.
# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
# Example 1:
# Input: "GGLLGG"
# Output: true
# Explanation: The robot moves from (0, 0) to(0, 2),turns 180 degrees, and then returns to(0, 0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.


def isRobotBounded(instructions: str) -> bool:
    x = 0 + 0j
    d = 0 + 1j
    for i in instructions:
        if i == "G":
            x += d
        elif i == "L":
            d = d * 1j
        elif i == "R":
            d = d * -1j

    return x == 0 + 0j or d != 0 + 1j


print(isRobotBounded("GGLLGG"))