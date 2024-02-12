from django.test import TestCase
from api.models import Category, Tag, Item
from api.serializers import CategorySerializer, TagSerializer, ItemSerializer

class SerializersTestCase(TestCase):
    def setUp(self):
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

    def test_category_serializer(self):
        serializer = CategorySerializer(instance=self.category1)
        self.assertEqual(serializer.data, {'id': self.category1.id, 'name': 'Category 1'})

    def test_tag_serializer(self):
        serializer = TagSerializer(instance=self.tag1)
        self.assertEqual(serializer.data, {'id': self.tag1.id, 'name': 'Tag 1'})

    def test_item_serializer(self):
        serializer = ItemSerializer(instance=self.item1)
        expected_data = {
            'id': self.item1.id,
            'sku': 'SKU001',
            'name': 'Item 1',
            'category': self.category1.id,
            'tags': [self.tag1.id],
            'stock_status': 'In Stock',
            'available_stock': 10
        }
        self.assertEqual(serializer.data, expected_data)
