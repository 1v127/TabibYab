from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BaseModel(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Education(BaseModel):
    pass


class Skill(BaseModel):
    pass


class Sex(BaseModel):
    pass


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    address = models.CharField(max_length=200, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True)
    sex = models.ForeignKey(Sex, on_delete=models.SET_NULL, null=True, related_name='sex')
    linkedin_url = models.URLField(blank=True)

    def __str__(self):
        return str(self.user.id)


class DoctorEducation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_education')
    education = models.ForeignKey(Education, on_delete=models.CASCADE, related_name='education')
    title = models.CharField(max_length=50)
    start_year = models.PositiveIntegerField(blank=True)
    end_year = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return self.title


class DoctorSkill(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_skill')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='skill')
    level = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.skill.title


class DoctorExperience(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_experience')
    company = models.CharField(max_length=50)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    working_now = models.BooleanField(default=False)
