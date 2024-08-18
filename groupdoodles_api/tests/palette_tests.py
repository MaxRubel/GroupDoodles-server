from django.test import TestCase
from django.urls import reverse
from groupdoodles_api.models import User, Palette
from groupdoodles_api.views import PaletteSerializer
from datetime import date
import random
import json

class PaletteTestCase(TestCase):
    def date_now(self):
        return date.today().strftime("%Y-%m-%d")
    
    def setUp(self):

       self.user_data = {
            "username" : "testuser",
            "uid" : "testuid123",
            "email" : "test@example.com",
            "date_registered": self.date_now()
       }

       self.user = User.objects.create(**self.user_data)     

       self.palette_data = {
            "name": "testpalette",
            "owner": self.user,
            "colors": [1,2,3,4,5,6,7,8,9],
            "date_created": self.date_now(),
       }
    
    def test_create_palette(self):
        create_palette_data = {
            "name": "testpalette",
            "user_id": 1,
            "colors": [1,2,3,4,5,6,7,8,9],
            "date_created": self.date_now(),
        }
        response = self.client.post(reverse('palette-list'), data=json.dumps(create_palette_data), content_type='application/json')
        palette = Palette.objects.get(pk=1)
        serializer = PaletteSerializer(palette)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 201)

    def test_update_palette(self):
        palette = Palette.objects.create(**self.palette_data)        
        
        update_data = {
            "user_id": 1,
            "name": "Updated Name",
            "colors": [1, 3, 4, 5, 6, 67],
            "date_created": palette.date_created.strftime("%Y-%m-%d")
        }
        
        url = reverse('palette-detail', args=[palette.id])
        response = self.client.put(url, data=json.dumps(update_data), content_type='application/json')
        
        self.assertEqual(response.status_code, 204)
        palette.refresh_from_db()

        self.assertEqual(palette.name, update_data['name'])
        self.assertEqual(palette.colors, update_data['colors'])
        self.assertEqual(palette.owner.id, update_data['user_id'])
        self.assertEqual(palette.date_created.strftime("%Y-%m-%d"), update_data["date_created"])

    def test_delete_palette(self):
        palette = Palette.objects.create(**self.palette_data)
        response = self.client.delete(reverse('palette-detail', args=[palette.id]))
        self.assertEqual(response.status_code, 204)
    
    def test_get_user_palettes(self):
        palettes = []
        for i in range(15):
            palette = Palette.objects.create(**self.palette_data)
            palettes.append(palette)
        
        url = reverse('palette-get-user-palettes')
        url += f'?user_id={self.user.id}'

        response = self.client.get(url)
        response_palettes = response.data
        self.assertEqual(len(palettes), len(response_palettes))

    def test_get_50_palettes(self):
        for i in range(100):
            Palette.objects.create(
                owner= self.user,
                name= "testpalette",
                colors= [1,2,3,4],
            )

        response = self.client.get(reverse("palette-list"))
        self.assertEqual(len(response.data), 50)