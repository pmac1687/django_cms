from django.db import models
from djangocms_text_ckeditor.fields import HTMLField


class Article(models.Model):
    title = models.CharField(max_length=200)
    #date, header
    content = HTMLField(blank=True)

    def __str__(self):
        """A string representation of the model."""
        return self.title


class Cards(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    tag = models.CharField(max_length=200, default='', help_text='format: #word , #word_2; seperate by comma')
    color = models.CharField(max_length=20, default='red',help_text='format: ex. blue')

    def __str__(self):
        return self.name

class MarketSegments(models.Model):
    name = models.CharField(max_length=20)
    svg = models.FileField(upload_to='uploads', default='')

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.FileField(upload_to='uploads', default='')
    background = models.FileField(upload_to='uploads', default='')

    def __str__(self):
        return self.title