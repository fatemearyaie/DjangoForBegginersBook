from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CostumUser

class CostumUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CostumUser
        fields = UserCreationForm.Meta.fields + ('age', )

class CostumUserChangeForm(UserChangeForm):
    class Meta:
        model = CostumUser
        fields = UserChangeForm.Meta.fields