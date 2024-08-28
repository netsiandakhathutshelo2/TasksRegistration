from django.db import models


class Task(models.Model):
    Tittle = models.CharField(max_length=250)
    Description = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    review_name = models.CharField(max_length=250)
    review_title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    task = models.ForeignKey(Task, on_delete=models.CASCADE)

