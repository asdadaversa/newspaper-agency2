from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

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
