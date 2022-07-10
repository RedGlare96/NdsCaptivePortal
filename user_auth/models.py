from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

plan_choices = (('free', 'Free plan'), ('paid', 'Paid plan'), ('test', 'debug test plan'))


class Client(models.Model):
    full_name = models.CharField(max_length=300)
    plan = models.CharField(max_length=10, choices=plan_choices, default='free')
    paid_time = models.IntegerField(default=3600)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_time = models.DateTimeField(auto_now=True)
    user_time = models.IntegerField(default=0)
