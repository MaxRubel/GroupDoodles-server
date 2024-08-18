from django.test import TestCase
from django.urls import reverse
from groupdoodles_api.models import Doodle, User
from groupdoodles_api.views import DoodleSerializer
from datetime import date
import json
from operator import itemgetter

class DoodleTestCase(TestCase):
    def date_now(self):
        return date.today().strftime("%Y-%m-%d")
    
    def setUp(self):

       self.user_data = {
            "username" : "testuser",
            "uid" : "testuid123",
            "email" : "test@example.com",
            "date_registered" :self.date_now()
       }

       self.user =User.objects.create(**self.user_data)     

       self.doodle_data = {
            "name": "testdoodle",
            "owner": self.user,
            "date_created": self.date_now(),
            "data": {"rectangles": [1,2,3], "image": "12313123123123123123123123123123"},
       }

    def test_create_doodle(self):

        doodle_data = {
            "name": "testdoodle",
            "user_id": 1,
            "date_created": self.date_now(),
            "data": {"rectangles": [1,2,3], "image": "12313123123123123123123123123123"},
       }

        response = self.client.post(reverse('doodle-list'), data=json.dumps(doodle_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        doodle = Doodle.objects.get(pk=1)

        serializer = DoodleSerializer(doodle)
        self.assertEqual(response.data, serializer.data)

        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['name'], 'testdoodle')
        self.assertEqual(response.data['date_created'], self.date_now())
        self.assertEqual(response.data['name'], 'testdoodle')
        self.assertEqual(response.data['data'],  {"rectangles": [1,2,3], "image": "12313123123123123123123123123123"})

    def test_update_doodle(self):
        doodle = Doodle.objects.create(**self.doodle_data)
        update_data = {
            "user_id": 1,
            "name" : "updated_test_name",
            "data" :  {"rectangles": [1,2,3,4,5,6], "image": "123131231231231231231231231asdasdasd23123"},
            "date_created" : self.date_now()
        }
        response = self.client.put(reverse('doodle-detail', args=[doodle.id]), data=json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 204)
        doodle.refresh_from_db()
        self.assertEqual(doodle.owner.id, 1)
        self.assertEqual(doodle.name, "updated_test_name")
        self.assertEqual(doodle.data,  {"rectangles": [1,2,3,4,5,6], "image": "123131231231231231231231231asdasdasd23123"})
        self.assertEqual(doodle.date_created.strftime("%Y-%m-%d"), self.date_now())
    
    def test_get_single_doodle(self):
        doodle = Doodle.objects.create(**self.doodle_data)
        response = self.client.get(reverse('doodle-detail', args=[doodle.id]), content_type='application/json')        

        serializer = DoodleSerializer(doodle)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
    
    def test_doodles_of_user(self):
        doodles = []
        for i in range(10):
            doodle = Doodle.objects.create(**self.doodle_data)
            serializer = DoodleSerializer(doodle)
            doodles.append(serializer)
        
        url = reverse('doodle-get-user-doodles')
        url += f'?user_id={self.user.id}'

        response = self.client.get(url)
        response_doodles = response.data['yourDoodles']
        self.assertEqual(len(response_doodles), len(doodles))

    def test_delete_doodle(self):
        doodle = Doodle.objects.create(**self.doodle_data)
        response = self.client.delete(reverse('doodle-detail', args=[doodle.id]))
        self.assertEqual(response.status_code, 204)


