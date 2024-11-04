import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Product

@pytest.mark.django_db
class TestProductViews:
    client = APIClient()

    @pytest.fixture
    def sample_product(self):
        product = Product.objects.create(
            name="Test Product",
            price=99.99,
            description="A product for testing."
        )
        return product

    def test_list_products(self, sample_product):
        response = self.client.get(reverse('product-list'))  # Replace with your actual URL name
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) > 0

    def test_create_product(self):
        data = {
            "name": "New Product",
            "price": 49.99,
            "description": "A new product.",
            "brand_name": "anjsos."
        }
        response = self.client.post(reverse('product-list'), data)
        print(response.json())
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] == data['name']

    def test_retrieve_product(self, sample_product):
        response = self.client.get(reverse('product-detail', args=[sample_product.id]))  # Replace with your actual URL name
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == sample_product.name

    def test_update_product(self, sample_product):
        data = {
            "name": "Updated Product",
            "price": 89.99,
            "description": "An updated product.",
            "brand_name": "anjsos."
        }
        response = self.client.put(reverse('product-detail', args=[sample_product.id]), data)
        print(response.json())
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == data['name']

    def test_delete_product(self, sample_product):
        response = self.client.delete(reverse('product-detail', args=[sample_product.id]))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Product.objects.count() == 0
