from django.db import models

# Create your models here.
# Create your models here.
class Signup(models.Model):
    
     Email= models.EmailField()
     Passwd = models.CharField(max_length =30)


class Application(models.Model):
    
     firstname= models.CharField(max_length=50)
     lastname= models.CharField(max_length = 100)
     email_address= models.EmailField(max_length=100)
     phone = models.IntegerField(blank=True)
     address= models.TextField (max_length = 30)
     zip_code = models.IntegerField( default="")
     state = models.CharField(max_length=150)
     city = models.CharField(max_length=150)
     business_strategy = models.FileField(upload_to='documents/')
     identity_card = models.FileField(upload_to= 'documents/')
     social_security_number = models.FileField(upload_to= 'documents/')
     
     def __str__(self):
        return str(self.firstname)
