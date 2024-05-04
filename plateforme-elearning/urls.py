from django.urls import include, path

urlpatterns = [
    # Autres URLs 
    path('elearning/', include('elearning.urls')),
]
from django.urls import path
from . import views

urlpatterns = [
    path('courses/create/', views.create_course, name='create_course'),
    path('courses/', views.course_list, name='course_list'),
]