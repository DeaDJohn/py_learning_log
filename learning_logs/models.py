from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Topic(models.Model):
    """Un tema sobre lo que ha aprendido el usuario."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Devuelve una representación del modelo como cadena."""
        return self.text


class Entry(models.Model):
    """Algo especifico aprendido en un tema."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.TextField(default="Título")
    text = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='uploads/%Y/%m/', height_field=None, width_field=None, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self) :
        if(len(self.title) < 50) :
            return self.title
        else :
            return f"{self.title[:50]}..."

