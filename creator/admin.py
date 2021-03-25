from django.contrib import admin
from . import models


admin.site.register(models.Doctor)
admin.site.register(models.Skill)
admin.site.register(models.Education)
admin.site.register(models.Sex)
admin.site.register(models.DoctorEducation)
admin.site.register(models.DoctorSkill)
admin.site.register(models.DoctorExperience)


