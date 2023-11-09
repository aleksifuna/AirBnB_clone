#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from models import storage
"""Classes for testing creation of other classes that inherit from BaseModel
"""


class TestClasses(unittest.TestCase):
    """
    Defines methods that tests creation of subclasses of BaseModel
    """

    def test_state(self):
        """
        tests creation of class state
        """

        my_obj = State()
        self.assertTrue(isinstance(my_obj, State))
        self.assertTrue(isinstance(my_obj.name, str))
        self.assertTrue(issubclass(type(my_obj), BaseModel))

    def test_city(self):
        """
        tests creation of class city
        """

        my_obj = City()
        self.assertTrue(isinstance(my_obj, City))
        self.assertTrue(isinstance(my_obj.name, str))
        self.assertTrue(isinstance(my_obj.state_id, str))
        self.assertTrue(issubclass(type(my_obj), BaseModel))

    def test_amenity(self):
        """
        tests creation of class amenity
        """

        my_obj = Amenity()
        self.assertTrue(isinstance(my_obj, Amenity))
        self.assertTrue(isinstance(my_obj.name, str))
        self.assertTrue(issubclass(type(my_obj), BaseModel))

    def test_place(self):
        """
        tests creation of class place
        """

        my_obj = Place()
        self.assertTrue(isinstance(my_obj, Place))
        self.assertTrue(isinstance(my_obj.city_id, str))
        self.assertTrue(isinstance(my_obj.user_id, str))
        self.assertTrue(isinstance(my_obj.name, str))
        self.assertTrue(isinstance(my_obj.description, str))
        self.assertTrue(isinstance(my_obj.number_rooms, int))
        self.assertTrue(isinstance(my_obj.number_bathrooms, int))
        self.assertTrue(isinstance(my_obj.max_guest, int))
        self.assertTrue(isinstance(my_obj.price_by_night, int))
        self.assertTrue(isinstance(my_obj.latitude, float))
        self.assertTrue(isinstance(my_obj.longitude, float))
        self.assertTrue(isinstance(my_obj.amenity_ids, list))
        self.assertTrue(issubclass(type(my_obj), BaseModel))

    def test_review(self):
        """
        tests creation of class review
        """

        my_obj = Review()
        self.assertTrue(isinstance(my_obj, Review))
        self.assertTrue(isinstance(my_obj.text, str))
        self.assertTrue(issubclass(type(my_obj), BaseModel))
