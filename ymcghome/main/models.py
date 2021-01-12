from django.db import models
from markdownx.models import MarkdownxField


# Create your models here.

class RecruitingBanner(models.Model):
    recruiting_term = models.BooleanField(null=False, default=False)    
    title = models.CharField(max_length=50)
    message = models.TextField()
    brochure = models.FileField(upload_to='uploads/', null=True)
    application_form_eng = models.FileField(upload_to='uploads/', null=True)
    application_form_kor = models.FileField(upload_to='uploads/', null=True)
    application_collection_email = models.EmailField()

class Introduction(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()

class Youtube(models.Model):
    share_embed_url_not_normal_url = models.URLField()

class Logo(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField()
    order = models.IntegerField(default=0, unique=True, null=False)

class Elements(models.Model):
    content = MarkdownxField()

class About(models.Model):
    content = MarkdownxField()

class Activities(models.Model):
    content = MarkdownxField()

class Join(models.Model):
    content = MarkdownxField()

class KeyValue(models.Model):
    value = models.CharField(max_length=20)
    description = models.TextField()
    order = models.IntegerField(default=0, null=False, unique=True)

class Footer(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

class Greeting(models.Model):
    name = models.CharField(max_length=20)
    description_1 = models.CharField(max_length = 50)
    description_2 = models.CharField(max_length=50)
    profile_photo = models.ImageField()
    greeting = MarkdownxField()
    order = models.IntegerField(null=False, default=0, unique=True)