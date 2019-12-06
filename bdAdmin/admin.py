from django.contrib import admin

# Register your models here.
from django.urls import include, path
from django.http import HttpResponseRedirect

from .models import Country
from .models import Food
from django.contrib.admin import AdminSite

from django.contrib.admin import site



class EventAdminSite(AdminSite):
    site_header = "BD Another Admin"
    site_title = "BD Another Site Admin "
    index_title = "Welcome to BD Another Site"

bd_another = EventAdminSite(name='bd_another')


bd_another.register(Country)
bd_another.register(Food)

MAX_OBJECTS = 1

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    change_list_template = "bdAdmin/countries_changelist.html"
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('world/', self.set_country_name),
        ]
        return my_urls + urls


    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False

        return super().has_add_permission(request)
        
    def set_country_name(self, request):
        self.model.objects.all().update(country_name="World")
        self.message_user(request, "Hello World")
        return HttpResponseRedirect("../")


# admin.site.register(Country)

admin.site.register(Food)

