from django.test import TestCase
from django.urls import reverse
from groupdoodles_api.models import User
from datetime import date
import json

class UserViewTestCase(TestCase):
    def date_now(self):
        return date.today().strftime("%Y-%m-%d")
    
    def setUp(self):
        self.user_data = {
            "username": "testuser",
            "uid": "testuid123",
            "email": "test@example.com",
            "date_registered": self.date_now()
        }

    def test_create_user(self):
        response = self.client.post(reverse('user-list'), data=json.dumps(self.user_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.get()
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.uid, 'testuid123')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.date_registered, date.today())
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['uid'], 'testuid123')
        self.assertEqual(response.data['username'], 'testuser')
        self.assertEqual(response.data['email'], 'test@example.com')
        self.assertEqual(response.data['date_registered'], self.date_now())
    
    def test_update_user(self):
        user = User.objects.create(**self.user_data)
        original_date = user.date_registered
        
        update_data = {
            "username": "updateduser",
            "uid": "testuid123",
            "email": "updated@example.com"
        }
        response = self.client.put(reverse('user-detail', args=[user.id]), data=json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 204)
        user.refresh_from_db()
        self.assertEqual(user.username, 'updateduser')
        self.assertEqual(user.uid, 'testuid123')
        self.assertEqual(user.email, 'updated@example.com')
        self.assertEqual(user.date_registered, original_date) 

    def test_delete_user(self):
        user = User.objects.create(**self.user_data)
        response = self.client.delete(reverse('user-detail', args=[user.id]))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(User.objects.count(), 0)

    def test_check_user(self):
        User.objects.create(**self.user_data)
        response = self.client.post(reverse('check_user'), data=json.dumps({"uid": "testuid123"}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'testuser')
        self.assertEqual(response.data['uid'], 'testuid123')
        self.assertEqual(response.data['email'], 'test@example.com')