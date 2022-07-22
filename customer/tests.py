from audioop import reverse
from django.test import Client, SimpleTestCase, TestCase
from django.urls import reverse,resolve
from customer.models import Customer
from customer.views import  index, create, saveFn, edit, update, delete
from django.contrib.auth.models import User

# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_index_url(self):
        url=reverse('customer_index')
        print(url)
        self.assertEquals(resolve(url).func,index)

    def test_create_url(self):
        url=reverse('customer_create')
        print(url)
        self.assertEquals(resolve(url).func,create)

    def test_saveFn_url(self):
        url=reverse('customer_saveFn')
        print(url)
        self.assertEquals(resolve(url).func,saveFn)

    def test_edit_url(self):
        url=reverse('customer_edit',args=['2'])
        print(url)
        self.assertEquals(resolve(url).func,edit)

    def test_update_url(self):
        url=reverse('customer_update')
        print(url)
        self.assertEquals(resolve(url).func,update)

    def test_delete_url(self):
        url=reverse('customer_delete')
        print(url)
        self.assertEquals(resolve(url).func,delete)


    



class TestViews(TestCase):
    def test_index(self):
        user=User.objects.create(username="testuser")
        user.set_password("12345")
        user.save()
        client=Client()
        logged_in=client.login(username="testuser",password="12345")
        response=client.get(reverse('index'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'customer/index.html')

    def test_create(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        client=Client()
        logged_in = client.login(username='testuser', password='12345')
        response=client.post(reverse('customer_create'),{
            'firstname':'firstname',
            'lastname':'lastname',
            'username':'username',
            'email':"email",
            'mobile':"mobile",
            'address':'address',
            'zipcode':'zipcode'
        })  

        self.assertEquals(response.status_code,302)
        self.assertRedirects(response,'/customer/index') 

    def test_delete(self):
        client=Client()
        c=Customer.objects.create(
            firstname='firstname',
            lastname='lastname',
            username='username',
            email="email",
            mobile="mobile",
            address='address',
            zipcode='zipcode'
        )

        print("this")
        print(c.customer_id)
        response=client.delete(reverse('customer_delete', args=[3]))

        self.assertEqual(response.status_code,302)

