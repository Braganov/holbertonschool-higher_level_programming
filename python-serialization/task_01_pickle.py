#!/usr/bin/python3
"""
This module defines a CustomObject class that can be serialized and
deserialized using the pickle module.

Class:
    CustomObject: A class with attributes name, age, and is_student.
                  Provides methods to serialize and deserialize objects.
"""


# import pickle


class CustomObject:
    """
    A class representing a custom object with name, age, and is_student
    attributes.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Whether the person is a student.
    """

    def __init__(self, name: str, age: int, is_student: bool):
        """
        Initialize the CustomObject with name, age, and is_student.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        # Vérification des types
        # if not isinstance(name, str):
        #    raise TypeError(f"Name must be a string, not {type(
        #        name).__name__}")
        # if not isinstance(age, int):
        #    raise TypeError(f"Age must be an integer, not {type(
        #        age).__name__}")
        # if not isinstance(is_student, bool):
        #    raise TypeError(f"Is Student must be a boolean, not {type(
        #        is_student).__name__}")

        self.name = name
        self.age = age
        self.is_student = is_student

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        self._age = value

    @property
    def is_student(self):
        return self._is_student

    @is_student.setter
    def is_student(self, value):
        if not isinstance(value, bool):
            raise TypeError("Is Student must be a boolean")
        self._is_student = value

    def display(self):
        """
        Display the object's attributes in a formatted string.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object and save it to the specified file using
        pickle.

        Args:
            filename (str): The name of the file where the object will be
            serialized.

        Returns:
            None
        """
        try:
            import pickle
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
            return True
        except (pickle.PickleError, IOError, Exception) as e:
            # Handle file-related errors (OSError) or pickling errors
            return False

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize and load an object from the specified file using pickle.

        Args:
            filename (str): The name of the file from which to deserialize the
            object.

        Returns:
            CustomObject: The deserialized object, or None if there was an
            error.
        """
        try:
            import pickle
            with open(filename, 'rb') as f:
                # obj = pickle.load(f)
                return pickle.load(f)
            # return obj
        except (FileNotFoundError, pickle.PicklingError,
                Exception, IOError) as e:
            # Handle file not found, unpickling errors, and general I/O errors
            return None
