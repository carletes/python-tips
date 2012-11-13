#!/usr/bin/env python2.7

import math
import unittest


class Vector(object):

    def __init__(self, *components):
        self.components = list(components)

    def magnitude(self):
        return math.sqrt(sum(x ** 2 for x in self.components))

    def dimension(self):
        return len(self.components)

    def __add__(self, v):
        if not isinstance(v, Vector):
            raise TypeError("%s: not a Vector" % repr(v))

        if self.dimension() != v.dimension():
            raise ValueError("Vectors of different dimension")

        components = [x + y for (x, y) in zip(self.components, v.components)]
        return Vector(*components)

    def __sub__(self, v):
        if not isinstance(v, Vector):
            raise TypeError("%s: not a Vector" % repr(v))

        if self.dimension() != v.dimension():
            raise ValueError("Vectors of different dimension")

        components = [x - y for (x, y) in zip(self.components, v.components)]
        return Vector(*components)

    def __eq__(self, v):
        if not isinstance(v, Vector):
            return False

        if self.dimension() != v.dimension():
            return False

        return all(x == y for (x, y) in zip(self.components, v.components))

    # Some Python conventions: String representation of Vectors:

    def __repr__(self):
        return "Vector(%s)" % ", ".join((repr(x) for x in self.components))

    __str__ = __repr__

    # Absolute value
    __abs__ = magnitude

    # Length
    __len__ = dimension

    # Comparisons:
    def __lt__(self, v):
        if not isinstance(v, Vector):
            raise TypeError("%s: not a Vector" % repr(v))

        if len(self) != len(v):
            raise ValueError("Vectors of different dimension")

        return abs(self) < abs(v)

    def __le__(self, v):
        if not isinstance(v, Vector):
            raise TypeError("%s: not a Vector" % repr(v))

        if len(self) != len(v):
            raise ValueError("Vectors of different dimension")

        return abs(self) <= abs(v)

    def __nonzero__(self):
        return self.magnitude() != 0

    # Accessing components:
    def __getitem__(self, i):
        try:
            return self.components[i]
        except IndexError:
            raise IndexError("Vector index out of range")

    def __setitem__(self, i, x):
        try:
            self.components[i] = x
        except IndexError:
            raise IndexError("Vector assignment index out of range")

    # Iteration:
    def __iter__(self):
        return iter(self.components)

    # A very sweet one: Reversing a vector:
    def __reversed__(self):
        return Vector(*[-x for x in self.components])

    # Another sweet one: Is one vector a positive multiple of another one?
    def __contains__(self, v):
        if not isinstance(v, Vector):
            raise TypeError("%s: not a Vector" % repr(v))

        if len(self) != len(v):
            raise ValueError("Vectors of different dimension")

        if not self or not v:
            return True

        k = [float(x) / float(y)
             for (x, y) in zip(v.components, self.components) if y]

        k_0 = k[0]
        if k_0 < 0:
            return False
        return all(k_i == k_0 for k_i in k[1:])

    # Even sweeter: Use the ``*`` operator to represent both multiplication by
    # a constant *and* the scalar product of two vectors ..
    def __mul__(self, v):
        if isinstance(v, Vector):
            if len(self) != len(v):
                raise ValueError("Vectors of different dimension")
            return sum(x * y for (x, y) in zip(self.components, v.components))
        else:
            components = [x * v for x in self.components]
        return Vector(*components)

    __rmul__ = __mul__

    # .. and use the above to calculate the angle between two vectors, which
    # is defined by:
    #
    #                    a . b
    #   theta = arc cos -------
    #                   |a|.|b|
    #
    # Compare the mathematic formula with the Python expresion to compute it:
    def __xor__(self, v):
        return math.acos((self * v) / abs(self) / abs(v))

    # Are two vectors aligned?
    def __or__(self, v):
        if not isinstance(v, Vector):
            raise TypeError("%s: not a Vector (%s)" % (repr(v), type(v)))

        if len(self) != len(v):
            raise ValueError("Vectors of different dimension")

        if not self or not v:
            return True

        k = [float(x) / float(y)
             for (x, y) in zip(v.components, self.components) if y]

        k_0 = k[0]
        return all(k_i == k_0 for k_i in k[1:])

    # Rotate a vector so many degrees clockwise ..
    def __lshift__(self, theta):
        return Vector(Vector(math.cos(theta), -math.sin(theta)) * self,
                      Vector(math.sin(theta),  math.cos(theta)) * self)

    # .. and counter-clockwise
    def __rshift__(self, theta):
        return self << (2 * math.pi - theta)


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
        self.assertEqual(0, (v * 0).magnitude())

        v = Vector(1, 0)
        self.assertEqual(10, (10 * v).magnitude())

        v = Vector(1, 1)
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

    def test_repr(self):
        self.assertEqual("Vector(1, 2, 3)",
                         repr(Vector(1, 2, 3)))
        self.assertEqual("Vector(1, 2, 3)",
                         str(Vector(1, 2, 3)))

    def test_comparisons(self):
        self.assertLess(Vector(1, 0), Vector(2, 0))
        self.assertLessEqual(Vector(1, 0), Vector(1, 0))
        self.assertGreater(Vector(2, 0), Vector(1, 0))
        self.assertGreaterEqual(Vector(2, 0), Vector(2, 0))

    def test_bool(self):
        self.assertTrue(Vector(1, 0))

    def test_components(self):
        v = Vector(3, 2, 1)
        self.assertEqual(3, v[0])
        self.assertEqual(2, v[1])
        self.assertEqual(1, v[2])
        with self.assertRaises(IndexError) as exc:
            v[3]
        self.assertEqual("Vector index out of range", exc.exception.message)

        v[0] = 1
        v[1] = 2
        v[2] = 3
        self.assertEqual(1, v[0])
        self.assertEqual(2, v[1])
        self.assertEqual(3, v[2])

        with self.assertRaises(IndexError) as exc:
            v[3] = 4
        self.assertEqual("Vector assignment index out of range",
                         exc.exception.message)

    def test_iteraror(self):
        coordinates = []
        for x in Vector(1, 2, 3):
            coordinates.append(x)
        self.assertEqual([1, 2, 3], coordinates)

    def test_length(self):
        self.assertEqual(2, len(Vector(1, 2)))

    def test_reversed(self):
        self.assertEqual(Vector(-1, -2, 3),
                         reversed(Vector(1, 2, -3)))

        v = Vector(-1, -2, 3)
        self.assertEqual(v, reversed(reversed(v)))

        v = Vector(0, 0, 0, 0)
        self.assertEqual(v, reversed(v))

    def test_aligned(self):
        self.assertFalse(Vector(1, 1) in Vector(1, 2))
        self.assertTrue(Vector(1, 1) in Vector(2, 2))
        self.assertFalse(Vector(1, 1) in Vector(-2, -2))

    def test_angle(self):
        # Sweet!
        self.assertEqual(math.pi / 2,
                         Vector(1, 0) ^ Vector(0, 1))

    def test_aligned(self):
        # Sweet!
        self.assertTrue(Vector(1, 1) | Vector(2, 2))
        self.assertTrue(Vector(1, 1) | Vector(-2, -2))
        self.assertTrue(Vector(1, -1) | Vector(1, -1))

    def test_rotation(self):
        # Sweet!
        self.assertTrue(Vector(1, 0) | (Vector(1, 0) << math.pi))
        self.assertAlmostEqual(Vector(0, 1),
                               Vector(1, 0) << (math.pi / 2))
        self.assertAlmostEqual(Vector(0, 1),
                               Vector(0, 1) << (2 * math.pi))
        self.assertAlmostEqual(Vector(3, 5),
                               (Vector(3, 5) << 0.7) >> 0.7)


if __name__ == "__main__":
    unittest.main()
