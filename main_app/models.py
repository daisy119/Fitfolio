from django.db import models

class Activity(models.Model):
  date = models.DateField()
  duration = models.DurationField()
  calorie_burnt = models.IntegerField()
  distance = models.FloatField()
  city = models.CharField(max_length=20)
  description = models.TextField(max_length=250)
  max_heart_rate = models.IntegerField()
  activity_type = models.CharField(max_length=20)

  def __str__(self):
    return self.city