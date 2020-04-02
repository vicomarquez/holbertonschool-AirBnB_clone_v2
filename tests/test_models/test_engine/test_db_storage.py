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
# from models.engine import DBStorage


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

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

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

if __name__ == "__main__":
    unittest.main()
