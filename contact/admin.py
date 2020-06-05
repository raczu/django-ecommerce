from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email']
    list_display = ['name', 'email', 'message']
    readonly_fields = ['name', 'email', 'message','date']

    fieldsets = [
        ('FORM INFORMATIONS', {'fields' : ['name', 'email', 'message']}),
        ('DATE INFORMATIONS', {'fields' : ['date']})
    ]

admin.site.register(Contact, ContactAdmin)