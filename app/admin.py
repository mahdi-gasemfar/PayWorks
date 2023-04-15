from django.contrib import admin
from app.models import JobPost


class JobAdmin(admin.ModelAdmin):
    list_display = ("__str__", "title", "date", "salary",)


admin.site.register(JobPost, JobAdmin)
