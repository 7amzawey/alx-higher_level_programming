#!/usr/bin/pyton3
"""this model is for a class called Rectangle inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """this class inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing the class methods
        Args:
            @width: is the width
            @height: is the height
            @x: is the x
            @y: is the way
            @id: is the id
        Returns: all the attributes
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self.validate_integer("width", value)
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        self.validate_integer("height", value)
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value):
        """valiate_integers"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if (name == "width") or (name == "height"):
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        if (name == "x") or (name == "y"):
            if value < 0:
                raise ValueError("{} must be => 0".format(name))

    def area(self):
        """calculate area"""
        return (self.width * self.height)

    def display(self):
        """display rectangle"""
        for lines in range(self.y):
            print()
        for h in range(self.height):
            print((" " * self.x) + ("#" * self.width))

    def __str__(self):
        """print info"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.x, self.y, self.width, self.height))

    def _update(self, id=None, width=None, height=None, x=None, y=None):
        """update info"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """super update info"""
        if args:
            self._update(*args)
        elif kwargs:
            self._update(**kwargs)

    def to_dictionary(self):
        """this one is going to return the
        representation of a class to dictionary"""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
