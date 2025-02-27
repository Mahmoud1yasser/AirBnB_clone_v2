#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            dictionary = self.__objects
            for key_11 in dictionary:
                partition = key_11.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dic[key_11] = self.__objects[key_11]
            return (dic)
        else:
            return self.__objects

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key_11 = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key_11] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dic1 = {}
        for key_11, value in self.__objects.items():
            my_dic1[key_11] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dic1, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key_11, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key_11] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ delete an existing element
        """
        if obj:
            key_11 = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key_11]

    def close(self):
        """ calls reload()
        """
        self.reload()
