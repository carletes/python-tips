#!/usr/bin/env python2.7

import math
import unittest


# Let's change the internal structure of vecors, so that we can have vectors
# of arbitrary dimensions.
class Vector(object):

    def __init__(self, *components):
        self.components = list(components)

    def magnitude(self):
        return math.sqrt(sum(x ** 2 for x in self.components))

    def multiply_by_scalar(self, k):
        self.components = [x * k for x in self.components]

    def sum(self, v):
        if not isinstance(v, Vector):
            raise TypeError("%s: not a Vector" % repr(v))
        self.components = [x + y
                           for (x, y) in zip(self.components, v.components)]


class VectorTest(unittest.TestCase):

    def test_magnitude(self):
        v = Vector(0, 0)
        self.assertEqual(0, v.magnitude())

        v = Vector(1, 0)
        self.assertEqual(1, v.magnitude())

        v = Vector(1, 1)
        self.assertEqual(math.sqrt(2), v.magnitude())

        # A three-dimensional vector --- v.magnitude() works exactly the same
        # way we expected it to work ...
        v = Vector(1, 1, 1)
        self.assertEqual(math.sqrt(3), v.magnitude())

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
        # .. but this no longer works. Peeking into the *internals* of an
        # object is not a good thing indeed:
        self.assertEqual(1, v.x)
        self.assertEqual(1, v.y)


if __name__ == "__main__":
    unittest.main()
