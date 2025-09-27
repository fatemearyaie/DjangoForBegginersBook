from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CostumUserChangeForm, CostumUserCreationForm
from .models import CostumUser

# Register your models here.
class CostumUserAdmin(UserAdmin):
    form = CostumUserChangeForm
    model = CostumUser
    list_display = [
        'email',
        'username',
        'age',
        'is_staff'
    ]

admin.site.register(CostumUser, CostumUserAdmin)