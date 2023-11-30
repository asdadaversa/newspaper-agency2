from django import forms
from django.contrib.auth import get_user_model

from newspaper.models import Topic, Newspaper


class NewspaperAdminForm(forms.ModelForm):

    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
