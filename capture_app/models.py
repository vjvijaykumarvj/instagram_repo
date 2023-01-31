from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    message  = models.TextField()
    recaptcha  = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name