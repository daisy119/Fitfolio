from django.shortcuts import render
from django.http import HttpResponse

class Activity:  
  def __init__(self, time, cal, city, distance, moving_time, avg_heart_rate, description):
    self.time = time
    self.cal = cal
    self.city = city
    self.distance = distance
    self.moving_time = moving_time
    self.avg_heart_rate = avg_heart_rate
    self.description = description

activities = [
  Activity('3/3/2024', '150', 'Philadelphia', '3','1','130','fun walk'),
]


def home(request):
  return HttpResponse('<h1>Hello fit person</h1>')

def about(request):
  return render(request, 'about.html')

def activity_index(request):
  return render(request, 'activities/index.html', { 'activities': activities })
