from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CostumUser

class CostumUserCreationForm(UserCreationForm):
    class Meta:
        model = CostumUser
        fields = UserCreationForm.Meta.fields + ("email",)
class CostumUserChangeForm(UserChangeForm):
    class Meta:
        model = CostumUser
        fields = UserChangeForm.Meta.fields