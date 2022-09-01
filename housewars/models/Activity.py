from django.db import models


class Activity(models.Model):
    class Meta:
        verbose_name_plural = "Activities"

    TimeslotChoices = [
        (30, '30'),
        (60, '60')
    ]

    name = models.CharField(max_length=100)
    quota = models.IntegerField()
    time = models.IntegerField(
        choices=TimeslotChoices, blank=True, null=True, default=None)
    password = models.CharField(
        max_length=100, blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.name} ({self.time})"

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
