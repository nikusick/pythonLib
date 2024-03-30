import unittest
from GeometryLib import *


class TestFiguresMethods(unittest.TestCase):

    def test_circle_assert(self):
        with self.assertRaises(AssertionError):
            circle(-1)
        with self.assertRaises(AssertionError):
            circle('1')

    def test_circle_area(self):
        pi = 3.14159
        self.assertAlmostEqual(circle(1).area(), pi, 4)
        self.assertAlmostEqual(circle(1.5).area(), 2.25 * pi, 4)
        self.assertAlmostEqual(circle(2).area(), 4 * pi, 4)
        self.assertAlmostEqual(circle(2.5).area(), 6.25 * pi, 4)

    def test_n_gon_figures_asserts(self):
        with self.assertRaises(AssertionError):
            n_gon_figures(1)
        with self.assertRaises(AssertionError):
            n_gon_figures('1')
        with self.assertRaises(AssertionError):
            n_gon_figures(3).area_by_coord(1, 2)

    def test_n_gon_figures_area(self):
        self.assertEqual(n_gon_figures(4).area_by_coord(0, 0, 1, 0, 1, 1, 0, 1), 1)
        self.assertEqual(n_gon_figures(4).area_by_coord(4, 1, 7, 4, 6, 6, 2, 4), 12.5)

    def test_regular_n_gon_figures_asserts(self):
        with self.assertRaises(AssertionError):
            regular_n_gon_figures(3).area_by_sides(-1)
        with self.assertRaises(AssertionError):
            regular_n_gon_figures(3).area_by_sides('-1')

    def test_regular_n_gon_figures_area(self):
        self.assertAlmostEqual(
            regular_n_gon_figures(3).area_by_sides(1), 3 ** 0.5 / 4, 4)
        self.assertAlmostEqual(
            regular_n_gon_figures(4).area_by_sides(1.5), 2.25, 4)

    def test_triangle_asserts(self):
        with self.assertRaises(AssertionError):
            triangle().area_by_sides(-1, -2, 1)
        with self.assertRaises(AssertionError):
            triangle().area_by_sides('1', '2', 1)
        with self.assertRaises(AssertionError):
            triangle().is_rectangular(-1, -2, 1)
        with self.assertRaises(AssertionError):
            triangle().is_rectangular('1', '2', 1)

    def test_triangle_area(self):
        self.assertEqual(triangle().area_by_sides(3, 4, 5), 6)
        self.assertEqual(triangle().area_by_sides(13, 14, 15), 84)

    def test_triangle_is_rectangular(self):
        self.assertTrue(triangle().is_rectangular(3, 4, 5))
        self.assertFalse(triangle().is_rectangular(13, 14, 15))