# coding=utf8
from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import Post


def home(request):
    posts = Post.get_recent_posts()

    ctx = RequestContext(request)
    ctx.update({
        'posts': [{
            'title': p.title,
            'content': p.content,
            'author': p.author,
            'pub_date': p.get_pub_date_display(),
        } for p in posts]
    })
    return render_to_response("home.html", ctx)
