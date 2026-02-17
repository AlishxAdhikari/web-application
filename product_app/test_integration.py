from django.test import TestCase
from django.urls import reverse
from product_app.models import Products

#python manage.py test product_app.tests_integration

class ProductIntegrationTestCase(TestCase):
    def test_create_cheap_product(self):
        #test that a cheap product(price <100) is NOT saved via the home view

        response = self.client.post(
            reverse("home"),
            {"name": "Cheap Product", "price": "50"} #price as string
        )
        self.assertEqual(response.status_code, 302) #302 = not found

        #cheap product should NOT exist due to save() logic
        with self.assertRaises(Products.DoesNotExist):
            Products.objects.get(name="Cheap Product")