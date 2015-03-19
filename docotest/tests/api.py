from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from docotest.models.resolution import Resolution

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

        self.retr_description = 'Test description for retreive'
        self.retr_resolution = Resolution.objects.create(author=self.user, description=self.retr_description)
        self.retr_resolution.save()
        self.retr_pk = self.retr_resolution.id

        self.del_description = 'Test description for delete'
        self.del_resolution = Resolution.objects.create(author=self.user, description=self.del_description)
        self.del_resolution.save()
        self.del_pk = self.del_resolution.id

        self.upd_description = 'Test description for update'
        self.upd_resolution = Resolution.objects.create(author=self.user, description=self.del_description)
        self.upd_resolution.save()
        self.upd_pk = self.del_resolution.id

        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)

    def test_create_resolution(self):
        """
        Ensure we can create a new Resolution object.
        """
        self.client = APIClient()
        url = reverse('resolution-list')
        data = {
                    'description': 'This is a test',
                    'author': self.user.id,
                }

        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertDictContainsSubset(data, response.data)

    def test_retrieve_resolutionlist(self):
        """
        Ensure we can Retrieve a ResolutionList.
        """
        self.client = APIClient()
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)
        url = reverse('resolution-list')

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, 'Resolution failed to be Retrieved')

        data = {
                    'description': self.retr_description,
                    'author': self.user.id,
                    'id': self.retr_pk,
                }
        check = 0
        for mydict in response.data['results']:
            if mydict['id'] == self.retr_pk:
                self.assertDictContainsSubset(data, mydict, "Retreived rows doesn't match setup data")
                check = 1

        self.assertEquals(check, 1, "Failed to find my setup data in ResolutionList")

    def test_retrieve_resolution(self):
        """
        Ensure we can Retrieve a Resolution object.
        """
        self.client = APIClient()
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)
        url = reverse('resolution-detail', args=[str(self.retr_pk)])

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, 'Resolution failed to be Retrieved')

        data = {
                    'description': self.retr_description,
                    'author': self.user.id,
                    'id': self.retr_pk,
                }
        self.assertDictContainsSubset(data, response.data, "Retreived row doesn't match setup data")

    def test_delete_resolution(self):
        """
        Ensure we can Delete a Resolution object.
        """
        self.client = APIClient()
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)
        url = reverse('resolution-detail', args=[str(self.del_pk)])

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, 'Deletion of test data Failed')

        #lets doublecheck we now get a 404
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, 'Deletion of test data Failed')

    def test_update_resolution(self):
        """
        Ensure we can Update a Resolution object.
        """
        self.client = APIClient()
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)
        url = reverse('resolution-detail', args=[str(self.upd_pk)])

        # TODO author should be retreived from the request. Not sure why it isn't
        data = {
                    'description': 'Updated description',
                    'author': self.user.id,  # see above TODO
            }
        response = self.client.put(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK, 'Resolution update Failed')
        self.assertDictContainsSubset(data, response.data, "Modified Resolution didn't contain the updated description")

        #lets doublecheck we get updated data back
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, 'Resolution failed to be Retrieved')
        self.assertDictContainsSubset(data, response.data, "Resolution didn't contain the updated description")
