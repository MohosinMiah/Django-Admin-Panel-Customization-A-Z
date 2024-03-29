"""djangoadmin_mohosin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from bdAdmin.admin import bd_another
from django.contrib.auth.models import User, Group



admin.site.site_header = "BD Django Header "
admin.site.site_title = "BD Admin Portal"
admin.site.index_title = "Welcome to BD-Admin Panel"




# Remove Default App From Admin Panel
# admin.site.unregister(User)
# admin.site.unregister(Group)

urlpatterns = [
    path('bdadmin/', include('bdAdmin.urls')),
    path('admin/', admin.site.urls),
    path('bd_another/', bd_another.urls),

]
