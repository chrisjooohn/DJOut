from django.contrib import admin
from .models import PORTAL_TBL

class Portal_Admin(admin.ModelAdmin):
    list_display = ("TITLE", "DESCRIPTION")

admin.site.register(PORTAL_TBL,Portal_Admin)