from django.db import models
import datetime

class Project(models.Model):
    name = models.CharField(max_length=120)
    start_date = models.DateField(auto_now_add=True, blank=True)
    end_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Task(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(auto_now_add=True, blank=True)
    end_date = models.DateField(blank=True, null=True)
    hours_worked = models.IntegerField(default='0',blank=True)
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.name
 
    class Meta:
        ordering = ['start_date']

class Counter(models.Model):
    start = models.DateTimeField(null=True,blank=True)
    pause = models.DateTimeField(null=True,blank=True)
    task = models.ForeignKey(Task)
    """docstring for Counter"""
 #   def __unicode__(self):
 #      self
    def hours(self):
        duration = (self.pause - self.start)
        days, seconds = duration.days, duration.seconds
        minutes = (days*24*60) + (seconds%60)
        return minutes

    class Meta:
        ordering = ['pause']