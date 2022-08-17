import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from driver.models import Driver


class DriverTest(APITestCase):
    def setUp(self):
        self.driver_1 = Driver.objects.create(
            first_name="Test_name1",
            last_name="Test_surname1",
        )
        self.driver_2 = Driver.objects.create(
            first_name="Test_name2",
            last_name="Test_surname2",
        )
        self.driver_3 = Driver.objects.create(
            first_name="Test_name3",
            last_name="Test_surname3",
        )
        self.driver_4 = Driver.objects.create(
            first_name="Test_name4",
            last_name="Test_surname4",
        )
        self.driver_5 = Driver.objects.create(
            first_name="Test_name5",
            last_name="Test_surname5",
        )

    def test_fail_create_driver(self):
        url = reverse('list_drivers')
        json_post = {'first_name': 'Test_patch', 'last_name': 'dddddddddddddddddddddddddddddddddddddddddddddddddd'
                                                              'dddddddddddddddddddddddddddddddddddddddddddddddddd'
                                                              'dddddddddddddddddddddddddddddddddddddddddddddddddd'}
        response = self.client.post(url, data=json_post)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_drivers_list(self):
        url = reverse('list_drivers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_fail_driver_detail(self):
        url = reverse('detail_driver', kwargs={'pk': 50})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_driver_detail(self):
        url = reverse('detail_driver', kwargs={'pk': self.driver_1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('first_name'), 'Test_name1')

    def test_patch_detail(self):
        url = reverse('detail_driver', kwargs={'pk': self.driver_1.pk})
        json_patch = {'first_name': 'Test_patch'}
        response = self.client.patch(url, data=json_patch)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('first_name'), 'Test_patch')

    def test_put_detail(self):
        url = reverse('detail_driver', kwargs={'pk': self.driver_1.pk})
        json_put = {'first_name': 'Test_put_first_name', 'last_name': 'Test_put_last_name'}
        response = self.client.put(url, data=json_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('first_name'), 'Test_put_first_name')
        self.assertEqual(response.json().get('last_name'), 'Test_put_last_name')

    def test_delete_detail(self):
        url = reverse('detail_driver', kwargs={'pk': self.driver_1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_drivers(self):
        url = reverse('list_drivers') + '?created_at__gte=2021-12-14'
        response = self.client.get(url)
        gte_date = datetime.date(2021, 12, 14)
        gte_driver_count = Driver.objects.filter(created_at__gte=gte_date).count()
        self.assertTrue(gte_driver_count, len(response.json()))

