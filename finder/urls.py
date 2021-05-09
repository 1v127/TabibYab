from django.urls import path
from . import views

app_name = 'finder'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),




    path('add_to_favourite/<int:doctor_id>/', views.add_to_favorite, name='add_to_favorite'),

]
