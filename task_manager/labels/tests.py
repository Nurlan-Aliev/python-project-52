from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse_lazy
from task_manager.labels.models import LabelModel
from task_manager.tasks.models import TasksModel
from task_manager.statuses.models import StatusModel


class TestLabelCRUD(TestCase):
    def create_user(self):
        User.objects.create_user(username='JohnSnow',
                                 password='referred_to_as_6')
        self.client.login(username='JohnSnow',
                          password='referred_to_as_6')

    def test_redirect(self):
        response = self.client.get(reverse_lazy('label_list'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.headers.get('Location'), '/login/')

    def test_labels(self):
        self.create_user()

        response = self.client.get(reverse_lazy('label_list'))
        self.assertEqual(response.status_code, 200)

    def test_create_labels(self):
        self.create_user()

        response = self.client.post(reverse_lazy('create_label'),
                                    data={'name': 'testing'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers.get('Location'), '/labels/')

        self.assertTrue(
            LabelModel.objects.filter(name='testing').exists())

    def test_update_labels(self):
        self.create_user()

        self.client.post(reverse_lazy('create_label'),
                                    data={'name': 'testing'})

        label = LabelModel.objects.get(name='testing')

        response = self.client.post(reverse_lazy('update_label', args=[label.id]),
                                    data={'name': 'TESTING'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers.get('Location'), '/labels/')

        self.assertTrue(
            LabelModel.objects.filter(name='TESTING').exists())

        self.assertFalse(
            LabelModel.objects.filter(name='testing').exists())

    def test_delete_labels(self):
        self.create_user()

        self.client.post(reverse_lazy('create_label'),
                         data={'name': 'important'})

        label = LabelModel.objects.get(name='important')

        self.client.post(reverse_lazy('create_status'),
                         data={'name': 'protection'})

        status = StatusModel.objects.get(name='protection')

        self.client.post(reverse_lazy('create_task'),
                         data={
                             'name': 'protect',
                             'description':
                                 'Summon the Northern Houses to defend'
                                 ' against the Army of the Dead.',
                             'status': status.id,
                             'labels': label.id,
                         })

        label = LabelModel.objects.get(name='important')
        response = self.client.post(reverse_lazy('delete_label',
                                                 args=[label.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            LabelModel.objects.filter(name='important').exists())

        task = TasksModel.objects.get(name='protect')
        self.client.post(reverse_lazy('delete_task', args=[task.id]))
        response = self.client.post(reverse_lazy('delete_label',
                                                 args=[label.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            LabelModel.objects.filter(name='important').exists())
