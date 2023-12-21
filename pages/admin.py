from django.contrib import admin
from pages.models import ContactModel, BlogModel, InfoModel


@admin.register(ContactModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']



@admin.register(InfoModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['man']


@admin.register(BlogModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
