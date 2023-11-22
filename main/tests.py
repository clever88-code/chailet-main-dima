from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from core.models import Hall, booking, News, Menu

class HallModelTest(TestCase):
    def setUp(self):
        self.hall = Hall.objects.create(hall='Зал 1')

    def test_hall_str(self):
        self.assertEqual(str(self.hall), 'Зал 1')

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.hall = Hall.objects.create(hall='Зал 1')
        self.booking = booking.objects.create(
            date=timezone.now(),
            auth_user=self.user,
            hall_booking=self.hall,
            description='Тестовый комментарий',
            date_booking=timezone.now()
        )

    def test_booking_str(self):
        expected_str = f'№{self.booking.id} Зал.{self.booking.hall_booking} Дата {self.booking.date}'
        self.assertEqual(str(self.booking), expected_str)

class NewsModelTest(TestCase):
    def setUp(self):
        self.news = News.objects.create(
            date=timezone.now(),
            title='Тестовая новость',
            description='Тестовый текст новости'
        )

    def test_news_str(self):
        expected_str = f'Название новости Тестовая новость'
        self.assertEqual(str(self.news), expected_str)

class MenuModelTest(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(
            title='Тестовое блюдо',
            content='Тестовый состав',
            price=10.99
        )

    def test_menu_str(self):
        expected_str = f'Название блюда Тестовое блюдо'
        self.assertEqual(str(self.menu), expected_str)
