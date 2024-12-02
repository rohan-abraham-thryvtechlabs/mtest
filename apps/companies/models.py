from django.db import models

# Create your models here.
class Companies(models.Model):
    company_name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.id