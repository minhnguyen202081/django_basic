from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework import status
from memories_api import models,serializers
from django.utils import timezone

# list all urls of memory_api??????????????????
LIST_URL_MEMORY_API=reverse('memory-list')
class PublicUnitTest(TestCase):
    def setUp(self):
        self.client=APIClient()
    def test_login_access(self):
        res = self.client.get(LIST_URL_MEMORY_API)
        self.assertEqual(res.status_code,status.HTTP_401_UNAUTHORIZED)
class PrivateUnitTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'fakeuser@gmail.com',
            'password123'
        )
        self.client.force_authenticate(self.user)
    def test_list_memory(self):
        models.Tag.objects.create(tag="new tagss")
        tag= models.Tag.objects.get(pk='1')
        memory=models.Memory.objects.create(
            title='title', 
            description='description', 
            owner=self.user,
            date=timezone.now()
            
        )
        memory.tags.add(tag)