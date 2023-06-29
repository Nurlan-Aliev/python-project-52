from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from task_manager.statuses.models import StatusModel


class StatusesCRUDTest(TestCase):

    def test_create_statuses(self):
        status_data = {

            'name': 'Active'
        }

        response = self.client.post(reverse('create_statuses'), data=status_data)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(StatusModel.objects.filter(name='Active').exists())

    def test_update_statuses(self):
        User.objects.create_user(username='aegon_targaryen', password='referred_to_as_6')
        status = StatusModel.objects.create(name='Active')
        update_data = {
            'name': 'Super_active'
        }

        url = reverse('update_statuses', args=[status.id])

        self.client.login(username='aegon_targaryen', password='referred_to_as_6')
        response = self.client.post(url, data=update_data)
        self.assertEqual(response.status_code, 302)
        status.refresh_from_db()
        self.assertEqual(status.name, 'Super_active')

    def test_delete_statuses(self):
        User.objects.create_user(username='aegon_targaryen', password='referred_to_as_6')
        self.client.login(username='aegon_targaryen', password='referred_to_as_6')
        status = StatusModel.objects.create(name='Active')
        response = self.client.post(reverse('delete_statuses', args=[status.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(username='testuser').exists())
