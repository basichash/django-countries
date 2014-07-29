from django.db import models
from django.test import TestCase
from django_countries.fields import CountryField

class Person(models.Model):
	name 	= models.CharField(max_length=64)
	country = models.CountryField()

class PersonTestCase(TestCase):

	def __init__(self):
		self.person1 = Person.objects.create(name='Chris', country='New Zealand')
		self.person2 = Person.objects.create(name='Justin', country='Canada')

	def test_country_properties:
		self.assertEqual(self.person1.country.name, 'New Zealand')
		self.assertEqual(self.person2.country.name, 'Canada')
		self.assertEqual(self.person1.country.code, 'NZ')
		self.assertEqual(self.person2.country.code, 'CA')
		self.assertEqual(self.person1.country.flag, '/static/flags/nz.gif')
		self.assertEqual(self.person2.country.flag, '/static/flags/ca.gif')