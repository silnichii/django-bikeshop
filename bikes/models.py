from django.db import models


class Types(models.Model):
    
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Types"



class Bikes(models.Model):
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, default="Unknown brand")
    price = models.IntegerField()
    type_name = models.ForeignKey(to = Types, on_delete = models.CASCADE, default=1)
    photo = models.ImageField(upload_to="photos", default="none")
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Bikes"

