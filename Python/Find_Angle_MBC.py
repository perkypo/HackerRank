"""
ABC is a right triangle at B.

Point M is the midpoint of hypotenuse .

You are given the lengths AB and BC.
Your task is to find angle ACB(angle , as shown in the figure) in degrees and rounded off to the nearest integer.
"""

import math

AB = int(input())
BC = int(input())

hype = math.hypot(AB,BC)

print('{0}{1}'.format(round(math.degrees(math.acos(BC/hype))),chr(176)))