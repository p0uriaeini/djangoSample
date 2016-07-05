from django.core.urlresolvers import reverse
from django.test import TestCase
from sample1.models import Information
from django.test.client import Client


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


class AddNewInformationTestCase(TestCase):
    def setUp(self):
        self.url = '/information/add/'
        self.client = Client()

    def test_add_new_infromatin_with_get_method(self):
        response = self.client.get(path=self.url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'add new information')

    def test_add_new_information_with_post_method_and_full_name(self):
        full_name = 'pouria eini'

        response = self.client.post(self.url, data={
            'full_name': full_name
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'index')
        self.assertContains(response, full_name)

    # def test_add_new_information_with_post_mehtod_and_without_full_name(self):
    #     # import pdb;pdb.set_trace()
    #     response = self.client.post(self.url, data=None)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'add new information')
