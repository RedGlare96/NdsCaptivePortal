import random
import string
from django.db import models
from django.contrib.auth.models import User

plan_choices = (('free', 'Free plan'), ('paid', 'Paid plan'), ('test', 'debug test plan'))


class Client(models.Model):
    full_name = models.CharField(max_length=300)
    plan = models.CharField(max_length=10, choices=plan_choices, default='free')
    paid_time = models.IntegerField(default=3600)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_time = models.DateTimeField(auto_now=True)
    user_time = models.IntegerField(default=0)


class PlanVoucher(models.Model):
    plan_name = models.CharField(max_length=100, default='Generic voucher')
    plan_code = models.CharField(max_length=20, default='placeholder')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    plan_time = models.IntegerField(default=3600)
    used = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        character_pool = string.ascii_uppercase + string.ascii_lowercase + string.digits
        p_code = 'MRHSE' + ''.join(random.choice(character_pool) for _ in range(15))
        self.plan_code = p_code
        super(PlanVoucher, self).save(*args, **kwargs)
