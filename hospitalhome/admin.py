from django.contrib import admin

# Register your models here.

from .models import Hospital_Information, Patient, User

admin.site.register(User)
admin.site.register(Hospital_Information)
admin.site.register(Patient)

