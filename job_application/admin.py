from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
    # modify the parameters to make interface more customizable, showing more
    # relevant data or adding search_fields for example
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name")
    list_filter = (["date"])
    ordering = (["first_name"])

admin.site.register(Form, FormAdmin)