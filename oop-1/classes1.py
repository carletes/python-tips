#!/usr/bin/env python2.7

import math
import unittest


# This is a class.
class Vector(object):

    def __init__(self, x, y):
        # Classes group together *state* ...
        self.x = x
        self.y = y

    # .. and *functionallity* ..
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def multiply_by_scalar(self, k):
        self.x *= k
        self.y *= k

    def sum(self, v):
        if not isinstance(v, Vector):
            raise TypeError("%s: not a Vector" % repr(v))
        self.x += v.x
        self.y += v.y


# .. so that we may forget about the internals of the class, and focus on its
# behaviour
class VectorTest(unittest.TestCase):

    def test_magnitude(self):
        v = Vector(0, 0)
        self.assertEqual(0, v.magnitude())

        v = Vector(1, 0)
        self.assertEqual(1, v.magnitude())

        v = Vector(1, 1)
        self.assertEqual(math.sqrt(2), v.magnitude())

    def test_multiply_scalar(self):
        v = Vector(0, 0)
        v.multiply_by_scalar(10)
        self.assertEqual(0, v.magnitude())

        v = Vector(1, 0)
        v.multiply_by_scalar(10)
        self.assertEqual(10, v.magnitude())

        v = Vector(1, 1)
        v.multiply_by_scalar(10)
        self.assertEqual(10 * Vector(1, 1).magnitude(),
                         v.magnitude())

    def test_sum(self):
        v = Vector(1, 0)
        with self.assertRaises(TypeError) as exc:
            v.sum(42)
        self.assertEqual("42: not a Vector", exc.exception.message)

        v = Vector(1, 0)
        v.sum(Vector(0, 1))
        # Peeking inside the object --- not a very good thing! We should not
        # need to look *into* the internals of the object in order to use it
        self.assertEqual(1, v.x)
        self.assertEqual(1, v.y)


if __name__ == "__main__":
    unittest.main()
