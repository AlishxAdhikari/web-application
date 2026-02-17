from django.test import TestCase
from product_app.models import Products

class ProductTestCase(TestCase):
    def test_create_product(self):
        product = Products.objects.create(name='Test Product', price=9.99)
        product.save()
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.price, 9.99)
    
    def test_update_product(self):
        product = Products.objects.create(name='Initial Product', price=100)
        product.save()
        product.name = 'Updated Product'
        product.price = 200
        product.save()
        updated_product = Products.objects.get(id=product.id)
        self.assertEqual(updated_product.name, 'Updated Product')
        self.assertEqual(updated_product.price, 200)
    
    def test_delete_product(self):
        product = Products.objects.create(name='Delete me', price=600)
        product.delete()
        with self.assertRaises(Products.DoesNotExist):
            Products.objects.get(name='Delete me')