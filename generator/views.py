from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from creator import models


@login_required
def generate_doctor(request):
    doctor = get_object_or_404(models.Doctor, user=request.user)
    print(doctor.id)
    doctor_skills = models.DoctorSkill.objects.filter(doctor=doctor)
    doctor_educations = models.DoctorEducation.objects.filter(doctor=doctor)
    doctor_experiences = models.DoctorExperience.objects.filter(doctor=doctor)
    return render(request, 'generate_doctor.html', {'doctor': doctor,
                                                    'doctor_skills': doctor_skills,
                                                    'doctor_educations': doctor_educations,
                                                    'doctor_experiences': doctor_experiences})

