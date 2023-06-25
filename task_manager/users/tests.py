from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class UserCRUDTest(TestCase):
    def test_create_user(self):

        user_data = {'first_name': 'Jon', 'last_name': 'Snow',
                     'username': 'aegon_targaryen', 'password1': 'referred_to_as_6',
                     'password2': 'referred_to_as_6'}

        response = self.client.post(reverse('create_user'), data=user_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='aegon_targaryen').exists())

    def test_update_user(self):
        user = User.objects.create_user(username='aegon_targaryen', password='referred_to_as_6')
        update_data = {
            'first_name': 'Jon',
            'last_name': 'Snow',
            'username': 'stark',
            'password1': 'referred_to_as_6',
            'password2': 'referred_to_as_6'
        }
        url = reverse('update_user', args=[user.id])

        self.client.login(username='aegon_targaryen', password='referred_to_as_6')
        response = self.client.post(url, data=update_data)
        self.assertEqual(response.status_code, 302)
        user.refresh_from_db()
        self.assertEqual(user.username, 'stark')

    def test_delete_user(self):
        user = User.objects.create_user(username='aegon_targaryen', password='referred_to_as_6')
        self.client.login(username='aegon_targaryen', password='referred_to_as_6')
        response = self.client.post(f'/users/{user.id}/delete/')
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(username='testuser').exists())
