from django.db import models

"""
все данные таблицы--Past.object.all()--> select * from posts
один обьект по условию -- Past.object.get(id=1)
несколько обьектов по условию -- Past.object.filter(title="title")
"""

class Post(models.Model):
    title = models.CharField(max_length=156)
    content = models.CharField(max_length=1056)
    rate = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.content}'