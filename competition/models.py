from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Competition(models.Model):
    car_model = models.CharField(max_length=100)
    description = models.TextField()
    specifications = models.TextField()
    rules = models.TextField()
    image = models.ImageField(upload_to='cars/')
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_tickets = models.PositiveIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    max_entries_per_user = models.PositiveIntegerField()

    def total_entries_sold(self):
        return self.entries.count()

    def remaining_entries(self):
        return self.total_tickets - self.total_entries_sold()

    def __str__(self):
        return self.car_model

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, related_name='entries', on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.competition.car_model}"

class Winner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    win_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='winners/', blank=True, null=True)
    testimonial = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.competition.car_model}"

class ContactInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question

