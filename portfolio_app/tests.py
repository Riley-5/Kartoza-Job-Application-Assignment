from django.test import TestCase
from portfolio_app.models import *

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="Joe", home_address="21st Street", phone_number="1234567891", location_latitude="-25.7479", location_longitude="28.2293")
        User.objects.create(username="Kate", home_address="", phone_number="9876543210", location_latitude="-26.1368", location_longitude="28.0157")
        User.objects.create(username="Steve", home_address="22nd Avenue", phone_number="123", location_latitude="-33.9249", location_longitude="18.4241")
        User.objects.create(username="Marlin", home_address="33rd Cove", phone_number="8765432198", location_latitude="-25.9934", location_longitude="27.5437")
        User.objects.create(username="Tom", home_address="55 Gravel", phone_number="5689741265", location_latitude="-29.8587", location_longitude="31.0218")

    def test_user_has_username(self):
        """
            Test that all users have a username
        """
        user1 = User.objects.get(username="Joe")
        user2 = User.objects.get(username="Kate")
        user3 = User.objects.get(username="Steve")
        user4 = User.objects.get(username="Marlin")
        user5 = User.objects.get(username="Tom")

        self.assertTrue(user1.username != "")
        self.assertTrue(user2.username != "")
        self.assertTrue(user3.username != "")
        self.assertTrue(user4.username != "")
        self.assertTrue(user5.username != "")

    def test_user_has_home_adress(self):
        """
            Test that all users have a home address
        """
        user1 = User.objects.get(username="Joe")
        user2 = User.objects.get(username="Kate")
        user3 = User.objects.get(username="Steve")
        user4 = User.objects.get(username="Marlin")
        user5 = User.objects.get(username="Tom")

        self.assertTrue(user1.home_address != "")
        self.assertFalse(user2.home_address != "")
        self.assertTrue(user3.home_address != "")
        self.assertTrue(user4.home_address != "")
        self.assertTrue(user5.home_address != "")

    def test_user_has_valid_phone_number(self):
        """
            Test all users have a valid phone number
            Valid phone number is assumed to have 10 digits no more no less
        """
        user1 = User.objects.get(username="Joe")
        user2 = User.objects.get(username="Kate")
        user3 = User.objects.get(username="Steve")
        user4 = User.objects.get(username="Marlin")
        user5 = User.objects.get(username="Tom")

        self.assertTrue(len(str(user1.phone_number)) == 10)
        self.assertTrue(len(str(user2.phone_number)) == 10)
        self.assertFalse(len(str(user3.phone_number)) == 10)
        self.assertTrue(len(str(user4.phone_number)) == 10)
        self.assertTrue(len(str(user5.phone_number)) == 10)

    def test_user_has_location(self):
        """
            Test all users have a location
        """
        user1 = User.objects.get(username="Joe")
        user2 = User.objects.get(username="Kate")
        user3 = User.objects.get(username="Steve")
        user4 = User.objects.get(username="Marlin")
        user5 = User.objects.get(username="Tom")

        self.assertTrue(user1.location_latitude != "")
        self.assertTrue(user1.location_longitude != "")
        self.assertTrue(user2.location_latitude != "")
        self.assertTrue(user2.location_longitude != "")
        self.assertTrue(user3.location_latitude != "")
        self.assertTrue(user3.location_longitude != "")
        self.assertTrue(user4.location_latitude != "")
        self.assertTrue(user4.location_longitude != "")
        self.assertTrue(user5.location_latitude != "")
        self.assertTrue(user5.location_longitude != "")