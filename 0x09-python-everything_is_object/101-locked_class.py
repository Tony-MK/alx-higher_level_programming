#!/usr/bin/python3
"""
This is the LockedClass module
"""


class LockedClass:
    """Defines a LockedClass which only allows first_name to be altered"""
    def __setattr__(self, key, value):
        """Attribute Setter (only first_name is permited)"""
        if key != "first_name":
            raise AttributeError(key, self)
        self.first_name = value
