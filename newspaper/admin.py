from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models


from newspaper import models
from newspaper.forms import NewspaperAdminForm
from newspaper.models import Topic, Redactor, Newspaper

from django.forms import CheckboxSelectMultiple


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("years_of_experience",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("first_name", "last_name", "email", "years_of_experience",)}),
    )
    list_filter = ["years_of_experience", ]
    search_fields = ["username", ]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    list_filter = ["id", ]
    search_fields = ["name", ]


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date",)
    list_filter = ["published_date", ]
    search_fields = ["title", ]
    form = NewspaperAdminForm


