from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Activity

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def activity_index(request):
  activities = Activity.objects.all()
  return render(request, 'activities/index.html', { 'activities': activities })

def activity_detail(request, activity_id):
  activity = Activity.objects.get(id=activity_id)
  return render(request, 'activities/detail.html', { 'activity': activity })

class ActivityCreate(CreateView):
  model = Activity
  fields = ['date', 'duration', 'calorie_burnt', 'distance', 'city', 'description', 'max_heart_rate', 'activity_type']

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class ActivityUpdate(UpdateView):
  model = Activity
  fields = ['duration', 'description', 'calorie_burnt','distance','city','max_heart_rate','activity_type']

class ActivityDelete(DeleteView):
  model = Activity
  success_url = '/activities/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('activity-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)




