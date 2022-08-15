from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from driver.models import Driver


class DriverTest(APITestCase):
    def setUp(self):
        self.one_driver = Driver.objects.create(
            first_name="Test_name",
            last_name="Test_surname"
        )

    def test_drivers_list(self):
        url = reverse('list_drivers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_fail_driver_detail(self):
        url = reverse('detail_driver', kwargs={'pk': 50})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_driver_detail(self):
        url = reverse('detail_driver', kwargs={'pk': self.one_driver.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('first_name'), 'Test_name')

    def test_patch_detail(self):
        url = reverse('detail_driver', kwargs={'pk': self.one_driver.pk})
        json_patch = {'first_name': 'Test_patch'}
        response = self.client.patch(url, data=json_patch)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('first_name'), 'Test_patch')

    def test_put_detail(self):
        url = reverse('detail_driver', kwargs={'pk': self.one_driver.pk})
        json_put = {'first_name': 'Test_put_first_name', 'last_name': 'Test_put_last_name'}
        response = self.client.put(url, data=json_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('first_name'), 'Test_put_first_name')
        self.assertEqual(response.json().get('last_name'), 'Test_put_last_name')

    def test_delete_detail(self):
        url = reverse('detail_driver', kwargs={'pk': self.one_driver.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)