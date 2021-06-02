from django.db import models
from django.contrib.auth.models import User
# Create your models here.


level = (
    ('covid_bed','covid-19 Beds'),
     ('oxygen_bed','covid-19 Oxygen Beds'),
      ('icu_bed','covid-19 ICU Beds'),
       ('icu_ventilator_bed','covid-19 ICU Beds with Ventilators')
)

class Hospital(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=50)
    
    pincode = models.IntegerField()
    patientlevel = models.CharField(choices=level, max_length=50)
    
    
    
    def __str__(self):

        return self.name
