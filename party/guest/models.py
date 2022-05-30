from django.db import models
from django.contrib.auth import get_user_model


class Guest(models.Model):
    name = models.CharField(max_length= 40)
    age = models.IntegerField(null= False , default= 18)
    invited_by= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    def __str__(self):
        # x = str(self.name) + ' by '+ str(self.invited_by)
        return self.name
