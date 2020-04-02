#!/usr/bin/python3
"""test for file storage"""
import unittest
import pep8
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestDBStorage(unittest.TestCase):
    '''Tests the DBStorage storage engine'''

    def setUp(self):
        """SetUp env for test"""
        from models.engine.db_storage import DBStorage
        self.storage = DBStorage()
        self.storage.reload()

    def tearDown(self):
        """teardown"""
        self.storage.save()
        del self.storage

    def test_all(self):
        """Test class method all()"""
        obj = self.storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertEqual(obj, self.storage.all())

    def test_new(self):
        """Test new method"""
        user = User()
        user.id = '12345'
        user.email = "Kevin@hotmail.com"
        user.password = "007"
        self.storage.new(user)
        self.storage.save()
        obj = self.storage.all()
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_save(self):
        """Test save method
        """
        user = User()
        user.id = '000'
        user.email = 'pizza@delivery.com'
        user.password = '000'
        self.storage.new(user)
        self.storage.save()
        self.assertTrue('User.000' in self.storage.all())

    def test_delete(self):
        """Tests delete
        """
        user = User()
        user.id = '666'
        user.email = 'jeffbezos@amazon.com'
        user.password = 'UnionBust'
        self.storage.new(user)
        self.storage.save()
        self.assertTrue('User.666' in self.storage.all())
        self.storage.delete(user)
        self.assertFalse('User.666' in self.storage.all())

    def test_reload(self):
        """Tests reload
        """
        user = User()
        user.id = '54321'
        user.email = 'justin@ded.com'
        user.password = 'enter'
        self.storage.new(user)
        self.storage.save()
        self.storage.reload()
        self.assertTrue('User.54321' in self.storage.all())


classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """ tests to chec docstrings in DBStorage class """

    @classmethod
    def setUpClass(cls):
        """set up for doc tests"""
        from inspect import getmembers, isfunction
        from models.engine.db_storage import DBStorage
        cls.db_functions = getmembers(DBStorage, isfunction)

    def test_db_storage_module_docs(self):
        """ test for docstrings in db_storage.py module """
        from models.engine.db_storage import DBStorage
        self.assertIsNot(DBStorage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "db_storage.py neds a docstring")

    def test_db_storage_class_docs(self):
        """ test for docstrings in DBStorage class """
        from models.engine.db_storage import DBStorage
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                       "DBStorage class needs a docstring")

    def test_dbs_function_docs(self):
        """ test for docstrings in DBStorage methods """
        for func in self.db_functions:
            self.assertIsNot(func[0].__doc__, None,
                            "{:s} method needs a docsting".format(func[0]))
            self.assertTrue(len(func[0].__doc__), None)

    def test_pep8_db_storage(self):
        """test db_storage.py is pep8 compliant """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["models/engine/db_storage.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_db_storage(self):
        """ test test_db_storage for pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["models/engine/db_storage.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
