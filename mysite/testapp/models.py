from django.db import models

# Create your models here.
class students(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    st_id = models.IntegerField()

    def __str__(self):
        return self.firstname