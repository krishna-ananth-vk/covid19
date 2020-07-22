from django.contrib import admin

from .models import Case, District, DateReport, TestReport


# Register your models here.

admin.site.register(Case)
admin.site.register(District)
admin.site.register(DateReport)
admin.site.register(TestReport)
