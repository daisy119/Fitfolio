from django.shortcuts import render
from .models import Activity

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def activity_index(request):
  activities = Activity.objects.all()
  return render(request, 'activities/index.html', { 'activities': activities })

def activity_detail(request, activity_id):
  activity = Activity.objects.get(id=activity_id)
  return render(request, 'activities/detail.html', { 'activity': activity })
