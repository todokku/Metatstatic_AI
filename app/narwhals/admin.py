from django.contrib import admin
from .models import Doctor, Patient #Add Doctor DB Model

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
