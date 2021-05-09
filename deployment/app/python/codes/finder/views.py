from django.shortcuts import render
from . import forms
from creator import models
from django.db.models import Count

from django.shortcuts import render, get_object_or_404, redirect
from creator.models import Doctor
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from json import JSONEncoder
from django.core import serializers
from django.http import JsonResponse


def index(request):
    genders = models.Sex.objects.all()
    skills = models.Skill.objects.all()
    educations = models.Education.objects.all()

    doctor_list = models.Doctor.objects.all()

    # name
    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            doctor_list = doctor_list.filter(name__istartswith=name)

    # family
    if 'family' in request.GET:
        family = request.GET['family']
        if family:
            doctor_list = doctor_list.filter(family__istartswith=family)

    # age
    if 'age' in request.GET:
        age = request.GET['age']
        if age:
            doctor_list = doctor_list.filter(age__lte=int(age))
        # Phone_number
        if 'phone_number' in request.GET:
            phone_number = request.GET['phone_number']
            if phone_number:
                doctor_list = doctor_list.filter(phone_number__lte=int(phone_number))
    # gender
    if 'gender' in request.GET:
        gender = request.GET['gender']
        if gender:
            doctor_list = doctor_list.filter(sex=int(gender))

    # education
    if 'education' in request.GET:
        education = request.GET['education']
        if education:
            doctor_list = doctor_list.distinct().filter(doctor_education__education=int(education))

    # skill
    if 'skill' in request.GET:
        skill = request.GET['skill']
        if skill:
            doctor_list = doctor_list.distinct().filter(doctor_skill__skill=int(skill))

    # company-count
    if 'company_count' in request.GET:
        company_count = request.GET['company_count']
        if company_count:
            doctor_list = doctor_list.annotate(exp_count=
                                               Count('doctor_experience')).filter(exp_count__gte=int(company_count))

    # working-now
    if 'working_now' in request.GET:
        working_now = request.GET['working_now']
        working_now = check_working_now(working_now)
        doctor_list = doctor_list.distinct().filter(doctor_experience__working_now=working_now)

    print(doctor_list)

    search_param = request.GET


    return JsonResponse(list(doctor_list.values()), safe=False)

    return render(request, 'index.html', {'genders': genders,
                                          'skills': skills,
                                          'educations': educations,
                                          'doctor_list': doctor_list,
                                          'search_param': search_param})


def check_working_now(val):
    try:
        return {
            '1': True,
            '0': False,
            '-1': None,
        }[val]
    except KeyError:
        return False


def contact(request):
    form = forms.ContactForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            print("welcome {}".format(form.cleaned_data['name']))
            form.save()
            return JsonResponse(list(contact.values()), safe=False)
    return render(request, 'contact.html', {'form': form})


@login_required
def add_to_favorite(request, doctor_id):
    doctor = get_object_or_404(models.Doctor, id=doctor_id)
    if doctor.favourite.filter(id=request.user.id).exists():
        doctor.favourite.remove(request.user)
        return JsonResponse({'result':'removed'}, safe=False)
    else:
        doctor.favourite.add(request.user)
        return JsonResponse({'result':'add'}, safe=False)
