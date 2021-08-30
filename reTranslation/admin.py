from django.contrib import admin
from .models import Program, Payload, Reponse
# Register your models here.


admin.site.register(Program)
admin.site.register(Reponse)

@admin.register(Payload)
class PayloadAdmin(admin.ModelAdmin):
    list_display = ('payloadnumber','programName')