from django.db import models
import numpy as np

class predict(models.Model):
    name = models.CharField(max_length=50)
    img_input = models.ImageField(upload_to='images/')
