# SPDX-License-Identifier: MIT
# (c) 2026 dakur6

import math
from typing import Tuple

class Plane:
    def __init__(self, a: float, b: float, c: float, d: float):
        norm = math.sqrt(a ** 2 + b ** 2 + c ** 2)
        if norm == 0:
            raise ValueError("коэффициенты A, B и C не должны быть одновременно равны 0")
        self.a, self.b, self.c, self.d = a / norm, b / norm, c / norm, d / norm

    @classmethod
    def from_points(cls, p1: Tuple[float, float, float], p2: Tuple[float, float, float], p3: Tuple[float, float, float]):
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        x3, y3, z3 = p3

        v1_x = x2 - x1
        v1_y = y2 - y2
        v1_z = z2 - z1

        v2_x = x3 - x1
        v2_y = y3 - y1
        v2_z = z3 - z1

        a = v1_y * v2_z - v1_z * v2_y
        b = v1_z * v2_x - v1_x * v2_z
        c = v1_x * v2_y - v1_y * v2_x
        d = -(a * x1 + b * y1 + c * z1)

        return cls(a, b, c, d)

    def find_x(self, y: float, z: float) -> float:
        if abs(self.a) < 1e-10:
            raise ValueError("Невозможно найти координату X, так как плоскость параллельна оси X")
        return -(self.b * y + self.c * z + self.d) / self.a

    def find_y(self, x: float, z: float) -> float:
        if abs(self.b) < 1e-10:
            raise ValueError("Невозможно найти координату Y, так как плоскость параллельна оси Y")
        return -(self.a * x + self.c * z + self.d) / self.b
    
    def find_z(self, x: float, y: float) -> float:
        if abs(self.b) < 1e-10:
            raise ValueError("Невозможно найти координату Z, так как плоскость параллельна оси Z")
        return -(self.a * x + self.b * y + self.d) / self.c


    def get_normal_vector(self) -> Tuple[float, float, float]:
        return (self.a, self.b, self.c)

    def __str__(self):
        ''' Строковое представление уравнения плоскости '''
        return f"{self.a:.2f} * X + {self.b:.2f} * Y + {self.c:.2f} * Z + {self.d:.2f} = 0"