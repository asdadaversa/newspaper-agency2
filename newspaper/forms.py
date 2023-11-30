from django import forms
from django.contrib.auth import get_user_model


class NewspaperAdminForm(forms.ModelForm):

    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        fields = ["title", "content", "topic", "publishers"]
