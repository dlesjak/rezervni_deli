from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Owner(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} {self.surname}"
    
class SparePart(models.Model):
    name = models.CharField("naziv", max_length=50)
    type = models.CharField("tip", max_length=20)
    dop = models.DateField("datum nabave")
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name="lastnik")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name="lokacija")

    def __str__(self):
        return f"{self.name} - {self.type}"
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('rd:detail', args=[str(self.id)])
