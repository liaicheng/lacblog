from django.test import TestCase
from myblog.models import BlogPost
# Create your tests here.
post=BlogPost.objects.all()
print(post)