from django.contrib import admin

# Register your models here.

from .models import Country
from .models import Food
from django.contrib.admin import AdminSite


class EventAdminSite(AdminSite):
    site_header = "BD Another Admin"
    site_title = "BD Another Site Admin "
    index_title = "Welcome to BD Another Site"

bd_another = EventAdminSite(name='bd_another')


bd_another.register(Country)
bd_another.register(Food)


admin.site.register(Country)
admin.site.register(Food)
