from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
  """Test models"""
  def test_create_user_with_email_successful(self):
    """Test creating a user with an email is successful"""
    email = "test@example.com"
    password = "test1234"
    user = get_user_model().objects.create_user(
      email=email,
      password=password
    )
    self.assertEqual(user.email, email)
    self.assertTrue(user.check_password(password))

  def test_new_user_email_normalized(self):
    """Test the email for a new user is normalized"""
    sample_emails = [
      ['test@EXAMPLE.COM','test@example.com'],
      ['Test2@Example.com','Test2@example.com'],
      ['Test3@Example.com','Test3@example.com'],
      ['test4@Example.com','test4@example.com'],

    ]
    for email,expected in sample_emails:
      user = get_user_model().objects.create_user(email, 'sample1234')
      self.assertEqual(user.email, expected)
  def test_new_user_without_email_raises_error(self):
    """Test creating user without an email raises error"""
    with self.assertRaises(ValueError):
      with self.assertRaises(ValueError):
        get_user_model().objects.create_user('','test123')

  def test_create_superuser(self):
    """Test creating a superuser"""
    user = get_user_model().objects.create_superuser(
      'test@example.com'
      'test1234'
    )
    self.assertTrue(user.is_superuser)
    self.assertTrue(user.is_staff)
