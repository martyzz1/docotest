from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.test import APIClient

#from django.test.utils import override_settings
#from nose.tools import assert_items_equal, assert_equal


class ResolutionTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.username = 'spam@eggs.com'
        self.email = 'spam@eggs.com'
        self.password = 'insecure'
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.user.password = make_password(self.password)
        self.user.save()

        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)

    def test_create_resolution(self):
        """
        Ensure we can create a new account object.
        """
        self.client = APIClient()
        url = reverse('resolution-list')
        data = {
                    'description': 'This is a test',
                    'author': self.user.id,
                }

        print data
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertDictContainsSubset(data, response.data)
