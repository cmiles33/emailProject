from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Program(models.Model):
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
    firstname = models.CharField(max_length=40,null=False,default="")
    lastname = models.CharField(max_length=40, null=False,default="")
    created = models.DateTimeField(auto_now_add=True)
    startTime = models.TimeField(default=timezone.now)
    endTime = models.TimeField(default=timezone.now)
    active = models.BooleanField(default=False)
    served = models.BooleanField(default=False)
    totalCount = models.IntegerField(default=0)
    totalComplete = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='programs/', blank=True)

    def get_absolute_url(self):
        return reverse('retranslation:program_detail',args=[
            self.member.username,
            self.programName,
        ])

    def get_next_payload_url(self):
        return reverse('retranslation:response_detail',args=[
            self.member.username,
            self.programName,
            self.programCount
        ])


    def __str__(self):
        return self.member.username + "'s " + self.programName + " program"

class Payload(models.Model):
    program_choices = (
        ('french','French'),
        ('spanish','Spanish'),
        ('none','None'),
    )
    payloadnumber = models.IntegerField()
    content = models.TextField(default=None)
    programName = models.CharField(max_length=40,
                                   choices=program_choices,
                                   default='none')

    class Meta:
        ordering = ['programName','payloadnumber']

    def __str__(self):
        return self.programName + " " + str(self.payloadnumber)

class Reponse(models.Model):
    program = models.ForeignKey(Program,
                                on_delete=models.CASCADE,
                                related_name='reponses')
    payload = models.ForeignKey(Payload,
                                on_delete=models.PROTECT,
                                related_name='reponses')
    textresponse = models.TextField(max_length=1000,
                                    default=None,verbose_name="Your Translation")
    finished = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['payload__payloadnumber',]

    def get_absolute_url(self):
        return reverse('retranslation:response_detail', args=[
            self.program.member.username,
            self.program.programName,
            self.payload.payloadnumber
        ])

    def __str__(self):
        return self.program.member.username + "'s " + \
            self.program.programName + " translation #" +\
            str(self.payload.payloadnumber)
