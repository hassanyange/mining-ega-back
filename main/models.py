from django.db import models
from django.contrib.auth.models import User

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



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
    



class Appointment(models.Model):
    CATEGORY_CHOICES = [
        ('1', 'Software issue'),
        ('2', 'Consultation'),
        ('3', 'Blame'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.get_category_display()}"
    

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(default='user@gmail.com')
    coordinates = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='applications/')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')

class Coordinate(models.Model):
    coordinates = models.CharField(max_length=100)
    is_taken = models.BooleanField(default=False)

class Token(models.Model):
    token = models.CharField(max_length=8, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)