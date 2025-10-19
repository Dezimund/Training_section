from django.db import models
from members_app.models import Member


class Course(models.Model):
    title = models.CharField(max_length=200)
    info = models.TextField(max_length=200)
    members = models.ManyToManyField(Member, related_name='courses',blank=True)

    def __str__(self):
        return self.title

