from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from . import models


class DoctorForm(forms.ModelForm):
    class Meta:
        model = models.Doctor
        exclude = ('user', 'name', 'family',)


class DoctorEducationForm(forms.ModelForm):
    class Meta:
        model = models.DoctorEducation
        exclude = ('doctor',)


class DoctorSkillForm(forms.ModelForm):
    class Meta:
        model = models.DoctorSkill
        fields = ('skill', 'level',)


class DoctorExperienceForm(forms.ModelForm):
    class Meta:
        model = models.DoctorExperience
        fields = ('company', 'start_date', 'end_date', 'working_now',)
        widgets = {
            'working_now': forms.NullBooleanSelect
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )

"""
class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'role'
        )
"""