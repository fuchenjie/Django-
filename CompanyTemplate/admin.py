from django.contrib import admin
from CompanyTemplate.models.Active import Active as ActiveSet,ActiveType
# Register your models here.
admin.site.register(ActiveType)
admin.site.register(ActiveSet)
