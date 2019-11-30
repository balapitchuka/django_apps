from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=250)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice

class Vote(models.Model):
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'vote'
        verbose_name_plural = 'votes'
        unique_together = ('poll', 'voted_by')
    
    def __str__(self):
        return str(self.voted_by)  +  " "  + str(self.choice)

    


