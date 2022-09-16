from django.db import models


class UserConfirm(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=6)
    token = models.UUIDField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.email
