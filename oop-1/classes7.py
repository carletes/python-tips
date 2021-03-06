#!/usr/bin/env python2.7

import math
import unittest


class Vector(object):

    def __init__(self, *components):
        self.components = list(components)

    def magnitude(self):
        return math.sqrt(sum(x ** 2 for x in self.components))

    # More operators: Multiplication on the left ..
    def __mul__(self, k):
        components = [x * k for x in self.components]
        return Vector(*components)

    # .. and on the right
    __rmul__ = __mul__

    # That was equivalent to:
    #
    #   def __rmul__(self, k):
    #       return self.__mul__(k)

    def dimension(self):
        return len(self.components)

    def __add__(self, v):
        if not isinstance(v, Vector):
            raise TypeError("%s: not a Vector" % repr(v))

        if self.dimension() != v.dimension():
            raise ValueError("Vectors of different dimension")

        components = [x + y for (x, y) in zip(self.components, v.components)]
        return Vector(*components)

    def __eq__(self, v):
        if not isinstance(v, Vector):
            return False

        if self.dimension() != v.dimension():
            return False

        return all(x == y for (x, y) in zip(self.components, v.components))


class VectorTest(unittest.TestCase):

    def test_magnitude(self):
        v = Vector(0, 0)
        self.assertEqual(0, v.magnitude())

        v = Vector(1, 0)
        self.assertEqual(1, v.magnitude())

        v = Vector(1, 1)
        self.assertEqual(math.sqrt(2), v.magnitude())

    def test_multiply(self):
        v = Vector(0, 0)
        # Voila to the right!
        self.assertEqual(0, (v * 0).magnitude())

        v = Vector(1, 0)
        # Voila to the left!
        self.assertEqual(10, (10 * v).magnitude())

        v = Vector(1, 1)
        # Voila to the right and left!
        self.assertEqual(20 * Vector(1, 1).magnitude(),
                         (2 * v * 10).magnitude())

    def test_sum(self):
        v = Vector(1, 0)
        with self.assertRaises(TypeError) as exc:
            v + 42
        self.assertEqual("42: not a Vector", exc.exception.message)

        v = Vector(1, 0)
        self.assertEqual(Vector(1, 1), v + Vector(0, 1))

        v = Vector(1, 0, 0)
        self.assertEqual(Vector(1, 1, 0), Vector(0, 1, 0) + v)

        with self.assertRaises(ValueError) as exc:
            Vector(1, 1) + Vector(1, 0, 0)
        self.assertEqual("Vectors of different dimension",
                         exc.exception.message)

    def test_dimension(self):
        self.assertEqual(2, Vector(1, 0).dimension())
        self.assertEqual(3, Vector(1, 0, 0).dimension())


if __name__ == "__main__":
    unittest.main()
