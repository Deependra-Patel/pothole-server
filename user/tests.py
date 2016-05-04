"""
Tests for user app
"""
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User
from .serializers import UserEntrySerializer


class UserTest(APITestCase):
    """
    All user related tests
    """

    def setUp(self):
        self.data = {
            'Name': 'Deependra Patel',
            'Phone': '9167473834',
            'City': 'mum',
            'Email': 'pateldeependra06@gmail.com',
            'FbId': 'deependra.patel.21',
            'Address': 'hostel 9, iit bombay, powai, mumbai 400076'
        }
        self.user1 = None
        self.user2 = None

    def _create_users(self):
        self.user1 = User.objects.create(Name='Anupreet', Phone='9999999999', City='mum',
                                         Email='anu@gmail.com',
                                         FbId='anupreet', Address='hostel 13, iitb', Rating=78,
                                         DeActivate=False,
                                         Credit=21, HomeLocation=None)
        self.user2 = User.objects.create(Name='Bhushan', Phone='9999999999', City='mum',
                                         Email='bhushan@gmail.com',
                                         FbId='bhushanfb', Address='hostel 12, iitb', Rating=18,
                                         DeActivate=True,
                                         Credit=21, HomeLocation=None)

    def test_add_user(self):
        """
        Ensure we can create a new user
        """
        url = reverse('user:user_list')
        fixed_data = {
            'Rating': 50.0,
            'DeActivate': False,
            'Credit': 0.0,
            'HomeLocation': None,
            'id': 1
        }
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_output = fixed_data
        expected_output.update(self.data)
        self.assertEqual(response.data, expected_output)

    def test_add_user_mobile(self):
        """
        Testing with wrong phone number
        """
        new_data = self.data
        new_data["Phone"] = "+91-9123501172"
        response = self.client.post(reverse('user:user_list'), new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        new_data["Phone"] = "91235+1172"
        response = self.client.post(reverse('user:user_list'), new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        new_data["Phone"] = "91235117212"
        response = self.client.post(reverse('user:user_list'), new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        new_data["Phone"] = "912351172"
        response = self.client.post(reverse('user:user_list'), new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_user(self):
        """
        Get user giving user id
        """
        self._create_users()
        response = self.client.get(reverse('user:user_detail', args=[self.user1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, UserEntrySerializer(self.user1).data)

    def test_update_user(self):
        """
        Updating user data
        """
        self._create_users()
        new_data = UserEntrySerializer(self.user1).data
        new_data["Name"] = "Anupreet Ramteke"
        new_data["Phone"] = "9123501172"
        response = self.client.put(reverse('user:user_detail', args=[self.user1.id]), new_data,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, new_data)

    def test_update_user_with_fail(self):
        """
        Credit/Rating can only be changed from server/admin
        """
        self._create_users()
        old_data = UserEntrySerializer(self.user1).data
        new_data = old_data.copy()
        new_data["Credit"] = "200"
        response = self.client.put(reverse('user:user_detail', args=[self.user1.id]), new_data,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, old_data)

        new_data["Rating"] = "200"
        response = self.client.put(reverse('user:user_detail', args=[self.user1.id]), new_data,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, old_data)

    def test_user_from_email(self):
        """
        Get user given an email
        """
        self._create_users()
        response = self.client.post(reverse('user:user_from_email'), {"Email": self.user1.Email},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, UserEntrySerializer(self.user1).data)

        response = self.client.post(reverse('user:user_from_email'), {"Email": self.user2.Email},
                                    format='json')
        # Deactivated user
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.post(reverse('user:user_from_email'),
                                    {"Email": "arbit121@iitb.ac.in"},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_user_list(self):
        """
        Get all the users
        """
        self._create_users()
        response = self.client.get(reverse('user:user_list'))
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
