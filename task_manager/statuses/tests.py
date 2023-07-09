from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse_lazy
from task_manager.statuses.models import StatusModel


class TestStatusesCRUD(TestCase):

    def create_user(self):
        User.objects.create_user(username='JohnSnow',
                                 password='referred_to_as_6')
        self.client.login(username='JohnSnow',
                          password='referred_to_as_6')

    def test_statuses(self):
        response = self.client.get(reverse_lazy('status_list'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers.get('Location'), '/login/')

    def test_create_statuses(self):
        self.create_user()
        status_data = {
            'name': 'Active'
        }
        response = self.client.post(reverse_lazy('create_status'),
                                    data=status_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers.get('Location'), '/statuses/')

        self.assertTrue(
            StatusModel.objects.filter(name='Active').exists())

    def test_update_statuses(self):
        self.create_user()
        self.client.post(reverse_lazy('create_status'),
                         data={'name': 'Active'})
        status = StatusModel.objects.get(name='Active')
        update_data = {'name': 'Super_active'}

        url = reverse_lazy('update_status', args=[status.id])

        response = self.client.post(url, data=update_data)
        self.assertEqual(response.status_code, 302)
        status.refresh_from_db()
        self.assertTrue(StatusModel.objects.filter(
            name='Super_active').exists())

    def test_delete_statuses(self):
        self.create_user()

        self.client.post(reverse_lazy('create_status'),
                         data={'name': 'Active'})

        status = StatusModel.objects.get(name='Active')
        response = self.client.post(reverse_lazy('delete_status',
                                                 args=[status.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            StatusModel.objects.filter(name='Active').exists())
