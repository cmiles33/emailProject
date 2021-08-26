from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Programs(models.Model):
    program_choices = (
        ('french','French'),
        ('spanish','Spanish',)
    )

    programName = models.CharField(max_length=40,
                                   choices=program_choices,
                                   default='spanish')
    programCount = models.IntegerField(default=0)
    member = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='programs')
    created = models.DateTimeField(auto_now_add=True)
    startTime = models.TimeField(default=timezone.now)
    endTime = models.TimeField(default=timezone.now)
    active = models.BooleanField(default=False)
    served = models.BooleanField(default=False)

class Payload(models.Model):
    program_choices = (
        ('french','French'),
        ('spanish','Spanish',
         'none','None')
    )
    payloadnumber = models.IntegerField()
    payloadpath = models.CharField(max_length=300)
    programName = models.CharField(max_length=40,
                                   choices=program_choices,
                                   default='none')
