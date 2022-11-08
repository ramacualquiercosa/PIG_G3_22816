from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'room')

admin.site.register(Page, PageAdmin)
