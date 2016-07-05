from unittest.mock import patch
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

    def test_add_new_information_with_post_mehtod_and_without_full_name(self):
        response = self.client.post(self.url, data=None)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'add new information')

    def test_add_new_informatin_with_post_method_information_save(self):
        full_name = 'pouria eini'

        with patch.object(Information, 'save') as information_mock_save_method:
            response = self.client.post(self.url, data={
                "full_name": full_name
            })
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, full_name)
            self.assertContains(response, 'index')
        assert information_mock_save_method.called


class GetInformaionList(TestCase):
    def test_get_list_of_information(self):
        for _ in range(0, 10):
            Information.objects.create(full_name='full_name %s' % _)
        informations = Information.objects.all()
        response = Client().get('/information/list/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'information list')
        for information in informations:
            self.assertContains(response, information.full_name)
            # self.assertContains(response, information.create_date)
