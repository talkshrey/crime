from django.contrib import admin
from .models import Helpline, Report, Vote

# Register your models here.
admin.site.register(Helpline)
admin.site.register(Report)
admin.site.register(Vote)