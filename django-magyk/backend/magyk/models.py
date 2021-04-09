from django.db import models
from djangocms_text_ckeditor.fields import HTMLField


class Article(models.Model):
    title = models.CharField(max_length=200)
    header = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
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
    description = models.TextField(default='')

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=60)
    content = HTMLField(blank=True)
    introduction = HTMLField(blank=True, default='')
    industry = models.CharField(max_length=60, default='')
    _type = models.CharField(max_length=60, default='')
    platforms = models.CharField(max_length=60, default='')
    duration = models.CharField(max_length=60, default='')
    challenge = models.CharField(max_length=60, default='')
    step1 = models.CharField(max_length=60, default='')
    step2 = models.CharField(max_length=60, default='')
    step3 = models.CharField(max_length=60, default='')
    step4 = models.CharField(max_length=60, default='')
    solution = models.CharField(max_length=60, default='')
    image = models.FileField(upload_to='uploads', default='')

    def __str__(self):
        return self.title