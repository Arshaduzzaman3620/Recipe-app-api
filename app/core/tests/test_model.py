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

