from math import pi, tan, radians, sqrt


def check_sides(func):
    def wrapper(*args):
        for side in args[1:]:
            assert isinstance(side, (int, float)), 'side must be int or float'
            assert side > 0, 'side must be greater than zero'
        return func(*args)

    return wrapper


def check_n(func):
    def wrapper(*args):
        n = args[1]
        assert isinstance(n, int), 'n must be int'
        assert n > 2, "n must be greater than 2"
        return func(*args)
    return wrapper


def check_coords(func):
    def wrapper(*args):
        for coord in args[1:]:
            assert isinstance(coord, (int, float)), 'coord must be int or float'
        return func(*args)

    return wrapper


class circle:
    r: float

    @check_sides
    def __init__(self, r: float):
        self.r = r

    def area(self):
        """
        Function for calculating the area of circle
        """
        s = pi * self.r ** 2
        return s


class n_gon_figures:
    n: int

    @check_n
    def __init__(self, n: int):
        self.n = n

    @check_coords
    def area_by_coord(self, *args) -> float:
        """
        Function for calculating the area of n-gon figure
        :param args: Vertex coordinates
        """
        assert self.n == len(args) / 2, 'Count of (x, y) pairs must be n'
        x = args[::2]
        y = args[1::2]
        s = 0.5 * ((sum([x[i] * y[i + 1] for i in range(self.n - 1)]) + x[self.n - 1] * y[0]) \
            - (sum([y[i] * x[i + 1] for i in range(self.n - 1)]) + y[self.n - 1] * x[0]))
        return s


class regular_n_gon_figures(n_gon_figures):

    @check_sides
    def area_by_sides(self, a: float) -> float:
        """
        Function for calculating the area of regular n-gon figure
        :param a: Side of figure
        """
        s = self.n * a ** 2 / (4 * tan(radians(180 / self.n)))
        return s


class triangle(n_gon_figures):

    def __init__(self):
        super().__init__(3)

    @check_sides
    def area_by_sides(self, a: float, b: float, c: float) -> float:
        """
        Function for calculating the area of triangle
        :param a: First side
        :param b: Second side
        :param c: Third side
        """
        p = (a + b + c) / 2
        s = sqrt(p * (p - a) * (p - b) * (p - c))
        return s

    @check_sides
    def is_rectangular(self, a: float, b: float, c: float) -> bool:
        """
        Function for checking a triangle for rectangularity
        :param a: First side
        :param b: Second side
        :param c: Third side
        """
        return max(a, b, c) ** 2 == a ** 2 + b ** 2 + c ** 2 - max(a, b, c) ** 2
