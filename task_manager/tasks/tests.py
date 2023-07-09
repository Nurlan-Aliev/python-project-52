from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse_lazy
from task_manager.tasks.models import TasksModel
from task_manager.statuses.models import StatusModel
from task_manager.labels.models import LabelModel


class TestTasksCRUD(TestCase):

    def create_user(self):
        User.objects.create_user(username='JohnSnow',
                                 password='referred_to_as_6')
        self.client.login(username='JohnSnow',
                          password='referred_to_as_6')

    def create_tasks(self):
        self.client.post(reverse_lazy('create_status'),
                         data={'name': 'protection'})

        status = StatusModel.objects.get(name='protection')

        response = self.client.post(
            reverse_lazy('create_task'),
            data={
                'name': 'protect',
                'description':
                    'Summon the Northern Houses to defend'
                    ' against the Army of the Dead.',
                'status': status.id})
        return response

    def test_create_task(self):
        self.create_user()
        self.client.post(reverse_lazy('create_status'),
                         data={'name': 'protection'})

        response = self.create_tasks()

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            TasksModel.objects.filter(name='protect').exists())

    def test_update_task(self):
        self.create_user()

        self.client.post(reverse_lazy('create_status'),
                         data={'name': 'protection'})

        status = StatusModel.objects.get(name='protection')

        self.create_tasks()

        task = TasksModel.objects.get(name='protect')

        update_data = {'name': 'protect_north', 'status': status.id}

        response = self.client.post(reverse_lazy('update_task',
                                                 args=[task.id]),
                                    data=update_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            TasksModel.objects.filter(name='protect_north').exists())
        self.assertFalse(TasksModel.objects.filter(name='protect').exists())

    def test_delete_task(self):
        self.create_user()
        self.create_tasks()
        task = TasksModel.objects.get(name='protect')

        self.assertTrue(TasksModel.objects.filter(name='protect').exists())

        response = self.client.post(
            reverse_lazy('delete_task', args=[task.id]))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(TasksModel.objects.filter(name='protect').exists())


class TestFilter(TestCase):
    def create_user(self):
        User.objects.create_user(username='JohnSnow',
                                 password='referred_to_as_6')
        self.client.login(username='JohnSnow',
                          password='referred_to_as_6')

    def create_tasks(self, task_name, status_name, label_name):
        if StatusModel.objects.filter(name=status_name):
            status = StatusModel.objects.get(name=status_name)
        else:
            self.client.post(reverse_lazy('create_status'),
                             data={'name': status_name})
            status = StatusModel.objects.get(name=status_name)

        if LabelModel.objects.filter(name=label_name):

            label = LabelModel.objects.get(name=label_name)
        else:
            self.client.post(reverse_lazy('create_label'),
                             data={'name': label_name})

            label = LabelModel.objects.get(name=label_name)

        self.client.post(reverse_lazy('create_task'),
                         data={
                             'name': task_name,
                             'status': status.id,
                             'labels': label.id})

    def test_view(self):
        self.create_user()
        self.create_tasks('finish the project', 'important', 'soon')
        self.create_tasks('find a job', 'important', 'find')
        self.create_tasks('start a new project', 'new_my_own_status', 'soon')

        status = StatusModel.objects.get(name='important')
        label = LabelModel.objects.get(name='soon')

        response = self.client.get(
            reverse_lazy('task_list'), {'status': status.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'finish the project', html=True)
        self.assertContains(response, 'find a job', html=True)
        self.assertNotContains(response, 'start a new project', html=True)

        response = self.client.get(reverse_lazy('task_list'),
                                   {'status': status.id, 'labels': label.id})
        self.assertContains(response, 'finish the project', html=True)
