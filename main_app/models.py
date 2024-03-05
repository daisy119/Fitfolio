from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

ACTIVITY_TYPE = (
  ('W', 'Walk'),
  ('R', 'Run'),
  ('B', 'Bike'),
  ('RO', 'Rollerblade'),
)

class Activity(models.Model):
  date = models.DateField('Activity date')
  duration = models.DurationField('Activity duration')
  calorie_burnt = models.IntegerField()
  distance = models.FloatField()
  city = models.CharField(max_length=20)
  description = models.TextField(max_length=250)
  max_heart_rate = models.IntegerField()
  activity_type = models.CharField(
    max_length=20,
    choices=ACTIVITY_TYPE,
    default=ACTIVITY_TYPE[0][0]
    )
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_activity_type_display()} in {self.city} on {self.date}"   
  
  def get_absolute_url(self):
    return reverse('activity-detail', kwargs={'activity_id': self.id})
  
class Photo(models.Model):
  url = models.CharField(max_length=250)
  activity = models.OneToOneField(Activity, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for activity_id: {self.activity_id} @{self.url}"