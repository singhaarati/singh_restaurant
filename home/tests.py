from django.test import TestCase
from audioop import reverse
from django.test import Client, SimpleTestCase, TestCase
from django.urls import reverse,resolve
from django.contrib.auth.models import User
from home.views import  buy_page, index

# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_index_url(self):
        url=reverse('buy_index')
        print(url)
        self.assertEquals(resolve(url).func,index)

    def test_buy_url(self):
        url=reverse('buy_product')
        print(url)
        self.assertEquals(resolve(url).func,buy_page)
