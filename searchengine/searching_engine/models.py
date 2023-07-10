from django.db import models

# Create your models here.

class Search_engine(models.Model):
  filename = models.CharField(max_length=255)
  features= models.CharField(max_length=255)

  #change firstname and last name with the features to search 