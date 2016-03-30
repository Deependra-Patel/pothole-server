from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User
from .serializers import UserEntrySerializer


class AddUserTest(APITestCase):
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

    def _create_users(self):
        self.user1 = User.objects.create(Name='Anupreet', Phone='9999999999', City='mum',
                                         Email='anu@gmail.com',
                                         FbId='anupreet', Address='hostel 13, iitb', Rating=78,
                                         DeActivate=False,
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

    def test_get_user(self):
        self._create_users()
        response = self.client.get(reverse('user:user_detail', args=[self.user1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, UserEntrySerializer(self.user1).data)
