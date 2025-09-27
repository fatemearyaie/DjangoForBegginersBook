from django.contrib import admin
from .models import CostumUser
from django.contrib.auth.admin import UserAdmin
from .forms import CostumUserChangeForm, CostumUserCreationForm

# Register your models here.
class CostumUserAdmin(UserAdmin):
    add_form = CostumUserCreationForm
    form = CostumUserChangeForm
    model = CostumUser
    list_display = [
        'email',
        'username',
        'age',
        'is_staff',
    ]

admin.site.register(CostumUser, CostumUserAdmin)