#!/usr/bin/python
""" test db storage"""

import unittest
from unittest import inspect
import pep8
import models
from models.engine import db_storage
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.user import User
import os


DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place", Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.Testcase):
    """ tests to chec docstrings in DBStorage class """
    @classmethod
    def setupclass(class):
        """set up for doc tests"""
        class.db_functions = getmembers(DBStorage, isfucntion)

    def test_db_storage_module_docs(self):
        """ test for docstrings in db_storage.py module """
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py neds a docstring")

    def test_db_storage_class_docs(self):
        """ test for docstrings in DBStorage class """
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.asserTrue(len(DBStorage.__doc__), >= 1,
                       "DBStorage class needs a docstring")

    def test_dbs_function_docs(self):
        """ test for docstrings in DBStorage methods """
        for func in self.db_functions:
            self.asserIsNot(func[0].__doc__, None,
                            "{:s} method needs a docsting".format(func[0]))
            self.assertTrue(len(func[0].__doc__), None,
                            "{:s} method needs a docstring".format(func[0]))

    def test_pep8_db_storage(self):
        """test db_storage.py is pep8 compliant """
        pep8style = pep8.Styleguide(quiet=True)
        result = pep8style.check_files(
            ["models/engine/db_storage.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_db_storage(self):
        """ test test_db_storage for pep8 """
        pep8style = pep8.Styleguide(quiet=True)
        result = pep8style.check_files(
            ["tests/test_models/test_engine/test_db_storage.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")
