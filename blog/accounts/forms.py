from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CostumUser

# این دوتا فرم رو برای زمانی که کاربر سفارشی داریم لازم داریم
class CostumUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CostumUser
        fields = UserCreationForm.Meta.fields + ('age', 'email',)

class CostumUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CostumUser
        fields = UserChangeForm.Meta.fields