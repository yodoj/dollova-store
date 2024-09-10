from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from .models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_product_name(self):
        product = Product.objects.create(
            name ="Teddy bear",
            price = 100000,
            description = "Cute and huggable teddy bear with premium materials for ultimaze coziness.",
            stock = 8
        )
        self.assertTrue(product)
