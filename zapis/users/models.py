from django.db import models
from authentication.models import People

class User(models.Model):
    # other fields related to student ...
    user_id = models.CharField(max_length=10, unique=True)
    people = models.OneToOneField(People, on_delete=models.CASCADE, related_name="student_account")