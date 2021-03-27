from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from . import forms
from . import models
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.generic import CreateView
from django.contrib.auth.hashers import check_password


class CreateDoctor(LoginRequiredMixin, CreateView):
    form_class = forms.DoctorForm
    template_name = 'create_doctor.html'

    def get_success_url(self):
        return reverse('creator:edit_doctor', args=(self.object.id,))

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.name = self.request.user.first_name
        form.instance.family = self.request.user.last_name
        return super().form_valid(form)


@login_required()
def edit_doctor(request, doctor_id):
    doctor = get_object_or_404(models.Doctor, id=doctor_id)
    form = forms.DoctorForm(instance=doctor)
    return render(request, 'create_doctor.html', {'form': form})


@login_required()
def create_doctor_education(request, doctor_id):
    doctor = get_object_or_404(models.Doctor, id=doctor_id)
    educations = models.DoctorEducation.objects.filter(doctor=doctor)
    print(educations)
    form = forms.DoctorEducationForm()
    if request.method == 'POST':
        form = forms.DoctorEducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.doctor = doctor
            education.save()
            form = forms.DoctorEducationForm()

    return render(request, 'create_doctor_education.html',
                  {'form': form,
                   'educations': educations,
                   'doctor_id': doctor.id})


@login_required()
def create_doctor_skill(request, doctor_id):
    doctor = get_object_or_404(models.Doctor, id=doctor_id)
    skills = models.DoctorSkill.objects.filter(doctor=doctor)
    print(skills)
    doctor_skill_formset = formset_factory(forms.DoctorSkillForm, extra=3)
    formset = doctor_skill_formset()
    if request.method == 'POST':
        formset = doctor_skill_formset(request.POST)
        if formset.is_valid():
            for form in formset:
                skill = form.save(commit=False)
                skill.doctor = doctor
                skill.save()
                formset = doctor_skill_formset()

    return render(request, 'create_doctor_skill.html',
                  {'formset': formset,
                   'skills': skills,
                   'doctor_id': doctor.id})


@login_required()
def create_doctor_experience(request, doctor_id):
    doctor = get_object_or_404(models.Doctor, id=doctor_id)
    experiences = models.DoctorExperience.objects.filter(doctor=doctor)
    print(experiences)
    form = forms.DoctorExperienceForm()
    if request.method == 'POST':
        form = forms.DoctorExperienceForm(request.POST)
        if form.is_valid():
            print("form is valid")
            experience = form.save(commit=False)
            experience.doctor = doctor
            experience.save()
            form = forms.DoctorExperienceForm()

    return render(request, 'create_doctor_experience.html',
                  {'form': form,
                   'experiences': experiences,
                   'doctor_id': doctor.id})


@login_required()
def logout_view(request):
    logout(request)
    return redirect('/')


def register_view(request):
    form = forms.RegisterForm()
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('creator:login'))
    return render(request, 'registration/register.html', {'form': form})


@login_required()
def view_profile(request):
    user = request.user
    return render(request, 'registration/profile.html', {'user': user})


@login_required()
def edit_profile(request):
    form = forms.EditProfileForm(instance=request.user)
    if request.method == 'POST':
        form = forms.EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('creator:profile'))
    return render(request, 'registration/edit_profile.html', {'form': form})


@login_required()
def change_password(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(reverse('creator:profile'))
    return render(request, 'registration/change_password.html', {'form': form})

"""
def login_view(request):
    this_username = request.POST.get('username')
    this_password = request.POST.get('password')
    # role=user or role=doctor
    #if request.POST['role'] == 'user':
    this_user = User.objects.get(username=this_username)
    if check_password(this_user.password, this_password):
        return redirect('/')
    else:
        return 'error: login agin'
    #else:
    #    return 'role:doctor , can not login!!'
"""