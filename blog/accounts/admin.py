from django.contrib import admin
from .models import CostumUser
from django.contrib.auth.admin import UserAdmin
from .forms import CostumUserChangeForm, CostumUserCreationForm

# Register your models here.
# وقتی که کاربر سفارشی داریم پنل ادمین پیشفرض فقط فیلدهای کاربر استاندارد رو میشناسه و برای اینکه فیلدهای دلخواه ما رو هم نشون بده باید این قطعه کد رو بنویسیم
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