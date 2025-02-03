from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import House, Booking, Review

class HouseModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='owner', password='password')
        self.house = House.objects.create(
            owner=self.user,
            title='Test House',
            description='A nice place to stay.',
            address='123 Main St',
            price=100.00,
            available=True
        )

    def test_house_creation(self):
        self.assertEqual(self.house.title, 'Test House')
        self.assertEqual(self.house.owner.username, 'owner')
        self.assertTrue(self.house.available)

class BookingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='tenant', password='password')
        self.house = House.objects.create(
            owner=self.user,
            title='Test House',
            description='A nice place to stay.',
            address='123 Main St',
            price=100.00,
            available=True
        )
        self.booking = Booking.objects.create(
            house=self.house,
            user=self.user,
            start_date='2025-01-10',
            end_date='2025-01-15'
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.house.title, 'Test House')
        self.assertEqual(self.booking.user.username, 'tenant')
        self.assertEqual(self.booking.start_date.strftime('%Y-%m-%d'), '2025-01-10')

class ReviewModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='reviewer', password='password')
        self.house = House.objects.create(
            owner=self.user,
            title='Test House',
            description='A nice place to stay.',
            address='123 Main St',
            price=100.00,
            available=True
        )
        self.review = Review.objects.create(
            house=self.house,
            user=self.user,
            rating=4,
            comment='Great place!',
            created_at='2025-01-10'
        )

    def test_review_creation(self):
        self.assertEqual(self.review.house.title, 'Test House')
        self.assertEqual(self.review.user.username, 'reviewer')
        self.assertEqual(self.review.rating, 4)
        self.assertEqual(self.review.comment, 'Great place!')
from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import House, Booking, Review

class HouseModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='owner', password='password')
        self.house = House.objects.create(
            owner=self.user,
            title='Test House',
            description='A nice place to stay.',
            address='123 Main St',
            price=100.00,
            available=True
        )

    def test_house_creation(self):
        self.assertEqual(self.house.title, 'Test House')
        self.assertEqual(self.house.owner.username, 'owner')
        self.assertTrue(self.house.available)

class BookingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='tenant', password='password')
        self.house = House.objects.create(
            owner=self.user,
            title='Test House',
            description='A nice place to stay.',
            address='123 Main St',
            price=100.00,
            available=True
        )
        self.booking = Booking.objects.create(
            house=self.house,
            user=self.user,
            start_date='2025-01-10',
            end_date='2025-01-15'
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.house.title, 'Test House')
        self.assertEqual(self.booking.user.username, 'tenant')
        self.assertEqual(self.booking.start_date.strftime('%Y-%m-%d'), '2025-01-10')

class ReviewModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='reviewer', password='password')
        self.house = House.objects.create(
            owner=self.user,
            title='Test House',
            description='A nice place to stay.',
            address='123 Main St',
            price=100.00,
            available=True
        )
        self.review = Review.objects.create(
            house=self.house,
            user=self.user,
            rating=4,
            comment='Great place!',
            created_at='2025-01-10'
        )

    def test_review_creation(self):
        self.assertEqual(self.review.house.title, 'Test House')
        self.assertEqual(self.review.user.username, 'reviewer')
        self.assertEqual(self.review.rating, 4)
        self.assertEqual(self.review.comment, 'Great place!')
from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import House, Booking, Review

class HouseModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='owner', password='password')
        self.house = House.objects.create(
            owner=self.user,
            title='Test House',
            description='A nice place to stay.',
            address='123 Main St',
            price=100.00,
            available=True
        )

    def test_house_creation(self):
        self.assertEqual(self.house.title, 'Test House')
        self.assertEqual(self.house.owner.username, 'owner')
        self.assertTrue(self.house.available)

class BookingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='tenant', password='password')
        self.house = House.objects.create(
            owner=self.user,
            title='Test House',
            description='A nice place to stay.',
            address='123 Main St',
            price=100.00,
            available=True
        )
        self.booking = Booking.objects.create(
            house=self.house,
            user=self.user,
            start_date='2025-01-10',
            end_date='2025-01-15'
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.house.title, 'Test House')
        self.assertEqual(self.booking.user.username, 'tenant')
        self.assertEqual(self.booking.start_date.strftime('%Y-%m-%d'), '2025-01-10')

class ReviewModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='reviewer', password='password')
        self.house = House.objects.create(
            owner=self.user,
            title='Test House',
            description='A nice place to stay.',
            address='123 Main St',
            price=100.00,
            available=True
        )
        self.review = Review.objects.create(
            house=self.house,
            user=self.user,
            rating=4,
            comment='Great place!',
            created_at='2025-01-10'
        )

    def test_review_creation(self):
        self.assertEqual(self.review.house.title, 'Test House')
        self.assertEqual(self.review.user.username, 'reviewer')
        self.assertEqual(self.review.rating, 4)
        self.assertEqual(self.review.comment, 'Great place!')
