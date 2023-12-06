from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from newspaper.forms import RedactorCreationForm
from newspaper.models import Topic, Newspaper


newspaper_url = reverse("newspaper:newspaper-list")


class FormSearchTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpass"
        )
        self.client.force_login(self.user)

    def test_search_newspaper_by_title(self):
        topic = Topic.objects.create(name="New topic")
        Newspaper.objects.create(
            title="test news",
            topic=topic,
            content="happy_content"
        )
        searched_name = "new"
        response = self.client.get(newspaper_url, {"title": searched_name})
        self.assertEqual(response.status_code, 200)
        context = Newspaper.objects.filter(
            title__icontains=searched_name
        )
        self.assertEqual(
            list(response.context["newspaper_list"]), list(context)
        )


class FormsTest(TestCase):
    def test_redactor_creation_form(self):
        form_data = {
            "username": "new_user",
            "password1": "user1test",
            "password2": "user1test",
            "first_name": "firsttest",
            "last_name": "lasttest",
            "years_of_experience": 10,
        }
        form = RedactorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="testadmin",
        )
        self.client.force_login(self.admin_user)
        self.redactor = get_user_model().objects.create_user(
            username="redactor",
            password="testredactor",
            years_of_experience="10",
        )

    def test_redactor_years_of_experience_listed(self):
        url = reverse("admin:newspaper_redactor_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.redactor.years_of_experience)

    def test_redactor_detail_years_of_experience_listed(self):
        url = reverse(
            "admin:newspaper_redactor_change",
            args=[self.redactor.id]
        )
        res = self.client.get(url)
        self.assertContains(res, self.redactor.years_of_experience)

    def test_redactor_years_of_experience_fieldsets(self):
        url = reverse("admin:newspaper_redactor_add")
        res = self.client.get(url)
        self.assertContains(res, self.redactor.years_of_experience)


class ModelsTests(TestCase):

    def test_create_newspaper_with_additional_topic(self):
        topic1 = Topic.objects.create(name="topic1")
        topic2 = Topic.objects.create(name="topic2")
        title = "test_title"
        content = "test content"
        newspaper = Newspaper.objects.create(
            title=title,
            content=content,
            topic=topic1,
        )
        newspaper.additional_topics.add(topic2)

        self.assertEqual(newspaper.title, title)
        self.assertEqual(newspaper.content, content)
        self.assertTrue(newspaper.topic, topic1)
        self.assertTrue(newspaper.additional_topics, topic2)
