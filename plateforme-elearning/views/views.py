from django.shortcuts import render, redirect
from .models import Course

def create_course(request):
    if request.method == 'POST':
        # Traitement du formulaire de création de cours
        return redirect('course_list')  # Redirection vers la liste des cours
    else:
        # Affichage du formulaire de création de cours
        return render(request, 'create_course.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})