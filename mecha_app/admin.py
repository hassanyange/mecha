from django.contrib import admin

from mecha_app.models import userEmail, userForm

# Register your models here.
admin.site.register(userForm)
admin.site.register(userEmail)