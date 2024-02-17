#!/usr/bin/python3
"""Module to represent Base object to be extended by Square and Rectangle."""
import json
import csv
import turtle


class Base:
    """Base class to be subclassed by Square and Rectangle."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize new Base instance.

        Args:
            id (int): Identifier for instance. If None, use current object count.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Serialize a list of dictionary objects into a JSON string.

        Args:
            list_dictionaries (list of dicts): List of dictionaries
                of attribute, value pairs for serialization into JSON
                representation.

        Returns:
            str: JSON string representation of `list_dictionaries`.
        """
        return json.dumps(list_dictionaries or [])

    @staticmethod
    def from_json_string(json_string):
        """Deserialize a JSON string into Python objects.

        Args:
            json_string (str): String representation of objects.

        Returns:
            list: Python objects represented by `json_string`.
        """
        return json.loads(json_string or "[]")

    @classmethod
    def save_to_file(cls, list_objs):
        """Convert `list_objs` to a JSON string and save it in a file.

        Args:
            list_objs (list): List of objects of the class from which
                this method is called.
        """
        list_objs = list_objs or []
        list_dicts = [obj.to_dictionary() for obj in list_objs]

        with open('{}.json'.format(cls.__name__), 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance directly from the class.

        Mainly for use by subclasses of Base.

        Args:
            dictionary (dict): Dictionary of attributes, value pairs
                with which to set attributes for a new instance.

        Returns:
            cls: New instance of class from which `create` was called.
        """
        new_instance = cls(1, 1) if cls.__name__ == 'Rectangle' else cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Load a file containing JSON serialized objects.

        Returns:
            list: List of objects of the class from which this method is called.
        """
        try:
            with open('{}.json'.format(cls.__name__), 'r',
                      encoding='utf-8') as f:
                obj_list_dicts = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []

        return [cls.create(**d) for d in obj_list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Convert `list_objs` to CSV format and save it in a file.

        Args:
            list_objs (list): List of objects of the class from which
                this method is called.
        """
        list_objs = list_objs or []
        fieldnames = cls._get_fieldnames()

        with open('{}.csv'.format(cls.__name__), 'w', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(obj.to_dictionary() for obj in list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Load a file containing CSV representation of objects.

        Returns:
            list: List of objects of the class from which this method is called.
        """
        try:
            with open('{}.csv'.format(cls.__name__), 'r', encoding='utf-8') as f:
                obj_list_dicts = list(csv.DictReader(f))
        except FileNotFoundError:
            return []

        return [cls.create(**d) for d in obj_list_dicts]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using Turtle.

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.
        """
        try:
            turtle._Screen._root
        except turtle.Terminator:
            turtle.Screen()
        turtle.speed(2)
        turtle.hideturtle()
        turtle.penup()
        turtle.pensize(3)
        turtle.color('green', 'blue')

        for i, rect in enumerate(list_rectangles):
            turtle.setx(i * 50)
            turtle.pendown()
            turtle.write(rect.__str__())
            turtle.dot()
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.right(-90)
                turtle.forward(rect.height)
                turtle.right(-90)
            turtle.end_fill()
            turtle.penup()

        turtle.color('orange', 'purple')
        for j, square in enumerate(list_squares):
            turtle.setx(j * 50)
            turtle.pendown()
            turtle.write(square.__str__())
            turtle.dot()
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(-90)
            turtle.end_fill()
            turtle.penup()

        turtle.exitonclick()

    @classmethod
    def _get_fieldnames(cls):
        """Helper method to get fieldnames for CSV.

        Returns:
            list: List of fieldnames for CSV representation.
        """
        if cls.__name__ == "Rectangle":
            return ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == "Square":
            return ['id', 'size', 'x', 'y']
        else:
            return ['id']


