from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    CHOICES = (
        (2, 'Coach'),
        (3, 'Player'),
    )
    user_type = forms.RadioSelect(choices=CHOICES)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'user_type')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        choices = (
            (2, 'Coach'),
            (3, 'Player'),
        )
        self.fields['user_type'] = forms.ChoiceField(choices=choices)
