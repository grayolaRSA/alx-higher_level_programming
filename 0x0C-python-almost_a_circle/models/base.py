#!/usr/bin/python3
"""module for base class"""
import json
import os.path
import csv

class Base:
    """
    base class for all other classes
    Args:
    nb_objects(int): number of objects
    id(int): identifier of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialise instances
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        converts list to JSON string
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        method to save object in a file
        """
        file_name = cls.__name__ + ".json"
        list_dict = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())

        list_new = cls.to_json_string(list_dict)

        with open(file_name, 'w') as f:
            f.write(list_new)

    @staticmethod
    def from_json_string(json_string):
        """
        JSON string to dictionary
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        method to create a new instance by updating current instance
        """
        if cls.__name__ == "Rectangle":
            new_inst = cls(7, 7)
        else:
            new_inst = cls(7)
        new_inst.update(**dictionary)
        return new_inst

    @classmethod
    def load_from_file(cls):
        """
        method that returns a list of instances from a class
        """
        file_name = cls.__name__ + ".json"

        if os.path.exists(file_name) is False:
            return []

        with open(file_name, 'r') as f:
            list_inst = f.read()

        list_class = cls.from_json_string(list_inst)
        list_in = []

        for index in range(len(list_class)):
            list_in.append(cls.create(**list_class[index]))

        return list_in

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        class method that serialises/saves to CSV file
        """
        filename = cls.__name__ + ".csv"

        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dic = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']

        matrix_dict = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for k in range(len(list_keys)):
                    list_dic[k] = obj.to_dictionary()[list_keys[k]]
                matrix_dict.append(list_dic[:])

        with open(filename, 'w') as write_File:
            writer = csv.writer(write_File)
            writer.writerows(matrix_dict)

    @classmethod
    def load_from_file_csv(cls):
        """
        class method that deserialises/loads from CSV file
        """
        file_name = cls.__name__ + ".csv"

        if os.path.exists(file_name) is False:
            return []

        with open(file_name, 'r') as read_File:
            reader = csv.reader(read_File)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        for elem in csv_list:
            dict_csv = {}
            for k in enumerate(elem):
                dict_csv[list_keys[k[0]]] = int(k[1])
            matrix.append(dict_csv)

        list_ins = []

        for index in range(len(matrix)):
            list_ins.append(cls.create(**matrix[index]))

        return list_ins
