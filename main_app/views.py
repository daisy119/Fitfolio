from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Activity, Photo
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'jw-fit-collector'

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def activity_index(request):
  activities = Activity.objects.filter(user=request.user)
  return render(request, 'activities/index.html', { 'activities': activities })

@login_required
def activity_detail(request, activity_id):
  activity = Activity.objects.get(id=activity_id)
  return render(request, 'activities/detail.html', { 'activity': activity })

class ActivityCreate(LoginRequiredMixin, CreateView):
  model = Activity
  fields = ['date', 'duration', 'calorie_burnt', 'distance', 'city', 'description', 'max_heart_rate', 'activity_type']

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class ActivityUpdate(LoginRequiredMixin, UpdateView):
  model = Activity
  fields = ['duration', 'description', 'calorie_burnt','distance','city','max_heart_rate','activity_type']

class ActivityDelete(LoginRequiredMixin, DeleteView):
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


def add_photo(request, activity_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, activity_id=activity_id)
      activity_photo = Photo.objects.filter(activity_id=activity_id)
      if activity_photo.first():
        activity_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('activity-detail', activity_id=activity_id)




