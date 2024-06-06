from django.db import models

class License(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    issue_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=255, help_text="FontAwesome icon class, e.g., fa-tree")

    def __str__(self):
        return self.title

class Statistic(models.Model):
    name = models.CharField(max_length=255)
    value = models.PositiveIntegerField()

    def __str__(self):
        return self.name
