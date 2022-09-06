from .models import login,Customer
from django.core.exceptions import ValidationError
from django.forms import ModelForm
class LoginForm(ModelForm):
    class Meta:
        model = login
        fields = '__all__'