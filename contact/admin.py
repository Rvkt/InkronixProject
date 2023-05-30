from django.contrib import admin
from contact.models import contactDetail


# Register your models here.
class contact(admin.ModelAdmin):
    list_display = ["name", "email", "number","message"]

admin.site.register(contactDetail,contact)