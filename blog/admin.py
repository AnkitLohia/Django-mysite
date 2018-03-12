# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Post

# Register your models here.
admin.site.register(Post)

#Here we are importing admin(system implementation of admin page)
#We are registering our Post model in admin page.
