"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'amir.moshi.ded@gmail.com'
        password = '1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample_emails = [
            ['example@GMAIL.com', 'example@gmail.com'],
            ['Example2@GMAIL.com', 'Example2@gmail.com'],
            ['EXAMPLE3@GMAIL.COM', 'EXAMPLE3@gmail.com'],
            ['example4@gmail.COM', 'example4@gmail.com']
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, '1234')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', '1234')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            'example@gmail.com',
            '1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)