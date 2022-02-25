from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import user, industry, skill, job

admin.site.register(user)
admin.site.register(industry)
admin.site.register(skill)
admin.site.register(job)