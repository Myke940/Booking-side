from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Problem(models.Model):
    nameofproblem = models.CharField(max_length = 20)
    descriptionofproblem = models.CharField(max_length = 200)
    cgcs = [('windows', 'Windows'), ('account', 'Account'), ('connection', 'Connection lost'), ('updates', 'Updates'), ('virus', 'Virus'), ('other', 'Others')]
    categoryofproblem = models.CharField(max_length = 13, choices = cgcs )
    def __str__(self):
        return self.nameofproblem



class Meeting(models.Model):
    time = models.DateTimeField(auto_now_add = True)
    usedproblem = models.ForeignKey(Problem, on_delete = models.SET_NULL, null = True, related_name = 'Meetings')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'Meetings')
    ss = [('new', 'new'), ('old', 'old'), ('in_progress', 'In Progress'), ('closed_session', 'Closed Session'), ('blocked/reported', 'Blocked')]
    status = models.CharField(max_length = 20, choices = ss, default = 'new')
    datetimemeet = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username}: {self.usedproblem.nameofproblem}'

