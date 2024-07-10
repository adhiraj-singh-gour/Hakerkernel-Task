from django import forms
from .models import User, Task

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'mobile']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_details', 'task_type', 'User']

    # user = forms.ModelChoiceField(queryset=User.objects.all())