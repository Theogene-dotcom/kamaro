from django.db import models


class contactmodel(models.Model):
    userFirstName = models.CharField(max_length=100)
    userLastName = models.CharField(max_length=100)
    userEmail = models.CharField(max_length=100)
    contactNumber = models.IntegerField()
    compName = models.CharField(max_length=100)
    projectTitle = models.CharField(max_length=100)
    projectDisp = models.CharField(max_length=100)
    class Meta:
        db_table="contact"