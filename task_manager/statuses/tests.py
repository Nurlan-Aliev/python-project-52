from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from task_manager.statuses.models import StatusModel
from django.test import Client


def create_login_user():
    user = User.objects.create_user(username='JohnSnow', password='referred_to_as_6')

    user.first_name = 'John'
    user.last_name = 'Doe'
    user.save()

    client = Client()

    logged_in = client.login(username='JohnSnow', password='referred_to_as_6')

    if logged_in:
        return client
    else:
        return None


class StatusesCRUDTest(TestCase):

    def test_create_statuses(self):
        status_data = {
            'name': 'Active'
        }
        self.client = create_login_user()
        response = self.client.post(reverse('create_status'), data=status_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(StatusModel.objects.filter(name='Active').exists())

    def test_update_statuses(self):
        status = StatusModel.objects.create(name='Active')
        update_data = {
            'name': 'Super_active'
        }

        url = reverse('update_status', args=[status.id])

        self.client = create_login_user()
        response = self.client.post(url, data=update_data)
        self.assertEqual(response.status_code, 302)
        status.refresh_from_db()
        self.assertTrue(StatusModel.objects.filter(name='Super_active').exists())

    def test_delete_statuses(self):
        self.client = create_login_user()
        status = StatusModel.objects.create(name='Active')
        response = self.client.post(reverse('delete_status', args=[status.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(username='testuser').exists())
