from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class TestUserCRUD(TestCase):
    user_data = {'first_name': 'Jon', 'last_name': 'Snow',
                 'username': 'aegon_targaryen',
                 'password1': 'referred_to_as_6',
                 'password2': 'referred_to_as_6'}

    def test_create_user(self):

        response = self.client.post(reverse_lazy('create_user'), data=self.user_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            User.objects.filter(username='aegon_targaryen').exists())

    def test_update_user(self):
        self.client.post(reverse_lazy('create_user'), data=self.user_data)

        user = User.objects.get(username='aegon_targaryen')
        update_data = {
            'first_name': 'Jon',
            'last_name': 'Snow',
            'username': 'stark',
            'password1': 'referred_to_as_6',
            'password2': 'referred_to_as_6'
        }
        url = reverse_lazy('update_user', args=[user.id])

        self.client.login(username='aegon_targaryen',
                          password='referred_to_as_6')
        response = self.client.post(url, data=update_data)
        self.assertEqual(response.status_code, 302)
        user.refresh_from_db()
        self.assertTrue(User.objects.filter(username='stark').exists())
        self.assertFalse(User.objects.filter(username='aegon_targaryen').exists())

    def test_delete_user(self):
        self.client.post(reverse_lazy('create_user'), data=self.user_data)

        user = User.objects.get(username='aegon_targaryen')

        self.client.login(username='aegon_targaryen',
                          password='referred_to_as_6')

        response = self.client.post(reverse_lazy('delete_user', args=[user.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(username='aegon_targaryen').exists())
