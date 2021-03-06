from __future__ import division
import math


class Coordinates(object):
    """ This object represent machine coordinates.
        Machine supports 3 axis, so there are X, Y and Z.
    """
    def __init__(self, x, y, z, e, p):
        """ Create object.
        :param x: x coordinated.
        :param y: y coordinated.
        :param z: z coordinated.
        """
        self.x = round(x, 10)
        self.y = round(y, 10)
        self.z = round(z, 10)
        self.e = round(e, 10)
        self.p = round(p, 10)


    def is_zero(self):
        """ Check if all coordinates are zero.
        :return: boolean value.
        """
        return (self.x == 0.0 and self.y == 0.0 and self.z == 0.0
                and self.e == 0.0, self.p == 0.0)

    def is_in_aabb(self, p1, p2):
        """ Check coordinates are in aabb(Axis-Aligned Bounding Box).
            aabb is specified with two points. E is ignored.
        :param p1: First point in Coord object.
        :param p2: Second point in Coord object.
        :return: boolean value.
        """
        min_x, max_x = sorted((p1.x, p2.x))
        min_y, max_y = sorted((p1.y, p2.y))
        min_z, max_z = sorted((p1.z, p2.z))
        min_e, max_e = sorted((p1.e, p2.e))
        min_p, max_p = sorted((p1.p, p2.p))
        if self.x < min_x or self.y < min_y or self.z < min_z or self.e < min_e or self.p < min_p:
            return False
        if self.x > max_x or self.y > max_y or self.z > max_z or self.e > max_e or self.p > max_p:
            return False
        return True

    def length(self):
        """ Calculate the length of vector.
        :return: Vector length.
        """
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z + self.e * self.e + self.p * self.p)

    def round(self, base_x, base_y, base_z, base_e, base_p):
        """ Round values to specified base, ie 0.49 with base 0.25 will be 0.5.
        :param base_x: Base for x axis.
        :param base_y: Base for y axis.
        :param base_z: Base for z axis.
        :param base_e: Base for e axis.
        :param base_p: Base for p axis.
        :return: New rounded object.
        """
        return Coordinates(round(self.x / base_x) * base_x,
                           round(self.y / base_y) * base_y,
                           round(self.z / base_z) * base_z,
                           round(self.e / base_e) * base_e,
                           round(self.p / base_p) * base_p)

    def find_max(self):
        """ Find a maximum value of all values.
        :return: maximum value.
        """
        return max(self.x, self.y, self.z, self.e, self.p)

    # build in function implementation
    def __add__(self, other):
        return Coordinates(self.x + other.x, self.y + other.y,
                           self.z + other.z, self.e + other.e,
                           self.p + other.p)

    def __sub__(self, other):
        return Coordinates(self.x - other.x, self.y - other.y,
                           self.z - other.z, self.e - other.e,
                           self.p - other.p)

    def __mul__(self, v):
        """
        @rtype: Coordinates
        """
        return Coordinates(self.x * v, self.y * v, self.z * v, self.e * v, self.p * v)

    def __div__(self, v):
        """
        @rtype: Coordinates
        """
        return Coordinates(self.x / v, self.y / v, self.z / v, self.e / v, self.p / v)

    def __truediv__(self, v):
        """
        @rtype: Coordinates
        """
        return Coordinates(self.x / v, self.y / v, self.z / v, self.e / v, self.p / v)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z \
               and self.e == other.e and self.p == other.p

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) \
               + ', ' + str(self.e) + ', ' + str(self.p) + ')'

    def __abs__(self):
        return Coordinates(abs(self.x), abs(self.y), abs(self.z),  abs(self.e), abs(self.p))
