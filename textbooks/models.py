from django.db import models

# Create your models here.
class Textbook(models.Model):
    NEW = 'New'
    OLD = 'Old'
    WRITTEN = 'Written'

    CONDITION_CHOICES = [
        (NEW, NEW),
        (OLD, OLD),
        (WRITTEN, WRITTEN),
    ]

    course = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    edition = models.CharField(max_length=50)
    condition = models.CharField(
        max_length=20,
        choices=CONDITION_CHOICES,
        default=NEW,
    )
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.title