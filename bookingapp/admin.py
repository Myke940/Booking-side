from django.contrib import admin

# Register your models here.
from .models import Problem, Meeting 

admin.site.register(Problem)
admin.site.register(Meeting)