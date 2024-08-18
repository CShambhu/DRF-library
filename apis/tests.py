from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from books.models import Book

class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = 'django for APIs',
            subtitle = 'learning django apis ',
            author = 'william st perterson',
            isbn = '124825',
        )

    def test_api_listview(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code,200)
        self.assertEqual(Book.objects.count(),1)
        self.assertContains(response, self.book)