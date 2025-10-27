# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementationS

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(10,10,10),'Equilateral','10,10,10 should be equilateral')

    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(5,5,3),'Isosceles','5,5,3 should be isosceles')
        self.assertEqual(classifyTriangle(5,3,5),'Isosceles','5,3,5 should be isosceles')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(4,5,6),'Scalene','4,5,6 should be scalene')
        self.assertEqual(classifyTriangle(6,4,5),'Scalene','6,4,5 should be scalene')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1,3,2),'NotATriangle','1,3,2 is not a triangle')
        self.assertEqual(classifyTriangle(2,3,5),'NotATriangle','2,3,5 is not a triangle')
        self.assertEqual(classifyTriangle(5,11,4),'NotATriangle','5,11,4 is not a triangle')

    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(-1,2,3),'InvalidInput','-1,2,3 is invalid input')
        self.assertEqual(classifyTriangle(1,0,1),'InvalidInput','1,0,1 is invalid input')
        self.assertEqual(classifyTriangle(201,100,100),'InvalidInput','201,100,100 is invalid input')
        self.assertEqual(classifyTriangle(100,100,250),'InvalidInput','100,100,250 is invalid input')
        self.assertEqual(classifyTriangle(3.5,4,5),'InvalidInput','3.5,4,5 is invalid input')
        self.assertEqual(classifyTriangle("a",4,5),'InvalidInput','a,4,5 is invalid input')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

