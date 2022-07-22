from django.test import TestCase
from audioop import reverse
from django.test import Client, SimpleTestCase, TestCase
from django.urls import reverse,resolve
from django.contrib.auth.models import User
from owner.views import  index, save

# Create your tests here.
class TestUrls(SimpleTestCase):


    def test_save_url(self):
        url=reverse('owner_save')
        print(url)
        self.assertEquals(resolve(url).func,save)
