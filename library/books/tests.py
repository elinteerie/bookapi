from django.test import TestCase
from django.urls import reverse

from .models import Book

# Create your tests here.


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
            cls.book = Book.objects.create(title ='A good title',
                                       subtitle ='An Excellent Subtitle',
                                       author ='Igwe U',
                                       isbn='1233455677')
        
        
        def test_book_content(self):
            self.assertEqual(self.book.title, 'A good title')
            self.assertEqual(self.book.subtitle, 'An Excellent Subtitle')
            self.assertEqual(self.book.author, 'Igwe U')
            self.asserrtEqual(self.book.isbn, '1233455677')
            
            
        def test_book_listview(self):
            response = self.client.get(reverse('home'))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response, 'excellent subtitle')
            self.assertEqaul(response, 'books/book_list.html')
            
