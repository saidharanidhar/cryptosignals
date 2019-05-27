# Register your models here.
from django.contrib import admin
from .models import Currency, User


class ReadonlyFields(admin.ModelAdmin):
    readonly_fields = ('updated',)


admin.site.register(Currency, ReadonlyFields)
admin.site.register(User)
