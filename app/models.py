"""
Definition of models.
"""
import datetime
from django.db import models

# Create your models here.
class test(models.Model):
    def __str__(self):
        return self.test_text
    def  was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    test.text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('data published')
class Choice(models.model):
    question=model.ForeignKey(Question,on_delete)
