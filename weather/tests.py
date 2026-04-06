from django.test import TestCase
from django.urls import reverse

class WeatherAppTests(TestCase):
    def test_homepage_status_code(self):
        """Verify the weather app homepage loads correctly."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)