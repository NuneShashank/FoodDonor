from django.db import models

class UserInfo(models.Model):
    email= models.EmailField()
    mobile_number=models.CharField(max_length=11)
    address=models.CharField(max_length=130)
    area=models.CharField(max_length=20)

    def __str__(self):
        return self.email