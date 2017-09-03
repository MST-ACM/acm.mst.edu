# Django
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase

# local Django
from . import actions


class ActionsTestCase(TestCase):
    """
    TODO: Docstring
    """
    def setUp(self):
        """
        TODO: Docstring
        """
        super().setUp()

    def test_actions_functions(self):
        """
        TODO: Docstring
        """
        valid_domains = getattr(settings, 'ENFORCED_EMAIL_DOMAINS', None)
        self.assertIsNotNone(valid_domains)

        for domain in valid_domains:
            self.assertEqual(actions.is_valid_email(r'test@'+domain), True)
            self.assertEqual(actions.is_valid_email(domain), False)
            self.assertEqual(actions.is_valid_email(r'@'+domain), False)

        self.assertEqual(actions.is_valid_email('test@thisisntavalidemail.com'), False)
        self.assertEqual(actions.is_valid_email('test'), False)
        self.assertEqual(actions.is_valid_email('@test.com'), False)
        self.assertEqual(actions.is_valid_email('.com'), False)

        with self.settings(ENFORCED_EMAIL_DOMAINS=None):
            with self.assertRaises(ImproperlyConfigured):
                actions.is_valid_email('test')

        with self.settings(ENFORCED_EMAIL_DOMAINS='test'):
            with self.assertRaises(ImproperlyConfigured):
                actions.is_valid_email('test@test')

        with self.assertRaises(TypeError):
            actions.is_valid_email()

class ViewTestCase(TestCase):
    def setUp(self):
        super().setUp()

    def test_view_integrity(self):
        response = self.client.get('43214321432141')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
