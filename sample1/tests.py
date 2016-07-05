from django.test import TestCase

from sample1.models import Information


class InformationTestCase(TestCase):
    def test_information_str_with_full_name(self):
        information = Information(full_name='someone')

        self.assertEqual('someone', str(information))

    def test_information_str_without_full_name(self):
        information = Information()

        self.assertEqual('The man', str(information))

    def test_information_str_with_empty_full_name(self):
        information = Information(full_name='')

        self.assertEqual('The man', str(information))
