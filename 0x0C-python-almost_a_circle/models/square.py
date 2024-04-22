#!/usr/bin/python3
"""
defining new class square inherits from rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """new class square inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns string information"""
        return ("{} ({}) {}/{} - {}".format(
            type(self).__name__, self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def _update(self, id=None, size=None, x=None, y=None):
        """updates args"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """updating the class by assigning attributes args and kwargs"""
        if (args):
            self._update(*args)
        elif (kwargs):
            self._update(**kwargs)

    def to_dictionary(self):
        """this will return the dictionary representation of the square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
