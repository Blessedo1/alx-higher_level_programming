#!/usr/bin/python3
"""Create a class MyInt that inherits from int"""


class MyInt(int):
    """MyInt rebel class that inverts the == and != operators"""

    def __eq__(self, other):
        """override the == operator"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """override the != operator"""
        return not super().__ne__(other)
