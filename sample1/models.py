from django.db import models


class Information(models.Model):
    full_name = models.CharField(max_length=64)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        if self.full_name and not self.full_name == '':
            return self.full_name
        else:
            return 'The man'
