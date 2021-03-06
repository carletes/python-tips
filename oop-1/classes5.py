#!/usr/bin/env python2.7

import math
import unittest


class Vector(object):

    def __init__(self, *components):
        self.components = list(components)

    def magnitude(self):
        return math.sqrt(sum(x ** 2 for x in self.components))

    def multiply_by_scalar(self, k):
        self.components = [x * k for x in self.components]

    def dimension(self):
        return len(self.components)

    def sum(self, v):
        if not isinstance(v, Vector):
            raise TypeError("%s: not a Vector" % repr(v))

        if self.dimension() != v.dimension():
            raise ValueError("Vectors of different dimension")

        self.components = [x + y
                           for (x, y) in zip(self.components, v.components)]

    # A nice thing of Python: We can define how Vectors behave with the ``=``
    # operator
    def __eq__(self, v):
        if not isinstance(v, Vector):
            return False

        if self.dimension() != v.dimension():
            return False

        return all(x == y for (x, y) in zip(self.components, v.components))

        # Alternatively:
        #
        #   def __eq__(self, v):
        #       if not isinstance(v, Vector):
        #           return False
        #
        #       return self.components == v.components


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
        # Voila!
        self.assertTrue(Vector(1, 1) == v)
        self.assertTrue(v == Vector(1, 1))
        self.assertEqual(Vector(1, 1), v)

        v = Vector(1, 0, 0)
        v.sum(Vector(0, 1, 0))
        # Voila!
        self.assertEqual(Vector(1, 1, 0), v)

        with self.assertRaises(ValueError) as exc:
            Vector(1, 1).sum(Vector(1, 0, 0))
        self.assertEqual("Vectors of different dimension",
                         exc.exception.message)

    def test_dimension(self):
        self.assertEqual(2, Vector(1, 0).dimension())
        self.assertEqual(3, Vector(1, 0, 0).dimension())


if __name__ == "__main__":
    unittest.main()
