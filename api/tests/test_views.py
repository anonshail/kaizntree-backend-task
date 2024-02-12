from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Category, Tag, Item
from api.serializers import CategorySerializer, TagSerializer, ItemSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category1 = Category.objects.create(name='Category 1')
        self.tag1 = Tag.objects.create(name='Tag 1')
        self.item1 = Item.objects.create(
            sku='SKU001',
            name='Item 1',
            category=self.category1,
            stock_status='In Stock',
            available_stock=10
        )
        self.item1.tags.add(self.tag1)
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        response = self.client.post('/api/token/', {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)
        self.token = response.data.get('access')
        self.assertIsNotNone(self.token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_category_list(self):
        response = self.client.get(reverse('category-list'))
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_tag_list(self):
        response = self.client.get(reverse('tag-list'))
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_item_list(self):
        response = self.client.get(reverse('item-list'))
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_user_registration(self):
        response = self.client.post(
            reverse('user-registration'),
            {'username': 'test_user', 'password': 'test_password'},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('username', response.data)
        
    def test_create_item(self):
        data = {
            'sku': 'SKU002',
            'name': 'Item 2',
            'category': 1,
            'tags': [1],
            'stock_status': 'In Stock',
            'available_stock': 20
        }
        response = self.client.post(reverse('item-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('sku', response.data)
        
    def test_create_category(self):
        data = {
            'name': 'Category 2'
        }
        response = self.client.post(reverse('category-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('name', response.data)
    
    def test_tag_category(self):
        data = {
            'name': 'Tag 2'
        }
        response = self.client.post(reverse('tag-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('name', response.data)

    
