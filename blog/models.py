# coding=utf8
from django.db import models
from django.contrib.auth.models import User
import misaka


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    author = models.ForeignKey(User)
    pub_date = models.DateTimeField(db_index=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = u'文章'
        verbose_name_plural = u'文章'

    def __unicode__(self):
        return self.title

    @classmethod
    def add_post(cls, title, content, author, pub_date):
        new_post = cls(
            title=title,
            content=content,
            author=author,
            pub_date=pub_date)
        new_post.save()
        return new_post

    @classmethod
    def get_recent_posts(cls, limit=10):
        return cls.objects.all()[:limit]

    def get_pub_date_display(self):
        return self.pub_date.strftime("%Y-%m-%d %H:%m")

    def get_content_display(self):
        return misaka.html(self.content)
