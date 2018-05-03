# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Create your views here.
def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
  #  post_lists = list()
   # for count,post in enumerate(posts):
    #    post_lists.append("No.{}:".format(str(count)) + str(post)+"<hr>")
    #    post_lists.append("<small>" + str(post.body.encode("utf-8")) + "</small><br><br>")
    return HttpResponse(html)
