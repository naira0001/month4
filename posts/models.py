from django.db import models
from django.db.models import SET_NULL

"""
все данные таблицы--Past.object.all()--> select * from posts
один обьект по условию -- Past.object.get(id=1)
несколько обьектов по условию -- Past.object.filter(title="title")
"""
class Category(models.Model):
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=156)
    content = models.CharField(max_length=1056)
    rate = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category,null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
        return f'{self.title} - {self.content}'
